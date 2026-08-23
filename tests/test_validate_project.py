from __future__ import annotations

import subprocess
import sys
import tomllib
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


class ProjectHomeValidationTests(unittest.TestCase):
    def test_validator_passes_current_public_candidates(self) -> None:
        result = subprocess.run(
            [sys.executable, str(ROOT / "scripts" / "validate_project.py")],
            cwd=ROOT,
            check=False,
            capture_output=True,
            text=True,
        )
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
        self.assertIn("PASS:", result.stdout)

    def test_profile_routes_are_concrete_and_inside_project(self) -> None:
        profile = tomllib.loads(
            (ROOT / ".fifth-ledger" / "project.toml").read_text(encoding="utf-8")
        )
        root = ROOT.resolve()
        routes = profile["routed_paths"]
        self.assertEqual(len(routes), len(set(routes)))
        for route in routes:
            resolved = (ROOT / route).resolve(strict=True)
            self.assertNotEqual(resolved, root)
            resolved.relative_to(root)

    def test_private_and_work_boundaries_are_ignored(self) -> None:
        for relative in (
            "AGENTS.local.md",
            "local/pilots/exact-evidence.json",
            "local/research/raw-notes.md",
            "work/scratch.txt",
            "__pycache__/module.pyc",
        ):
            with self.subTest(relative=relative):
                result = subprocess.run(
                    ["git", "check-ignore", "--quiet", "--", relative],
                    cwd=ROOT,
                    check=False,
                )
                self.assertEqual(result.returncode, 0)

    def test_known_plugin_canon_paths_are_absent(self) -> None:
        for relative in (
            ".codex-plugin/plugin.json",
            "references/five-ledger-model.md",
            "skills/adopt-fifth-ledger/SKILL.md",
        ):
            with self.subTest(relative=relative):
                self.assertFalse((ROOT / relative).exists())

    def test_execution_charter_keeps_lifecycle_permissions_separate(self) -> None:
        charter = (ROOT / "docs" / "execution-charter-template.md").read_text(
            encoding="utf-8"
        )
        for action in (
            "Create or change a remote",
            "Mutate a provider or account",
            "Mutate a runtime",
            "Change a UI",
            "Change repository or artifact visibility",
            "Communicate externally",
            "Publish",
            "Install",
            "Deploy",
            "Register or submit to a marketplace",
            "Release or promote",
            "Rewrite history or force-push",
        ):
            with self.subTest(action=action):
                self.assertIn(f"| {action} |", charter)


if __name__ == "__main__":
    unittest.main()
