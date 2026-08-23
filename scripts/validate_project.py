#!/usr/bin/env python3
"""Validate the portable Fifth Ledger project-home contract."""

from __future__ import annotations

import re
import subprocess
import sys
import tomllib
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
PROFILE = ROOT / ".fifth-ledger" / "project.toml"
REQUIRED_FILES = (
    ".fifth-ledger/project.toml",
    ".gitignore",
    "AGENTS.local.md.example",
    "AGENTS.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "README.md",
    "docs/README.md",
    "docs/adoption-strategy.md",
    "docs/decisions/ADR-0001-project-home-boundary.md",
    "docs/decisions/ADR-0002-proportional-adoption-model.md",
    "docs/decisions/README.md",
    "docs/pilots/README.md",
    "docs/product-direction.md",
    "docs/release-publication-gates.md",
    "docs/roadmap.md",
    "docs/source-ownership.md",
    "local/README.md",
    "scripts/README.md",
    "scripts/validate_project.py",
    "tests/README.md",
    "tests/test_validate_project.py",
)
FORBIDDEN_IMPLEMENTATION_PATHS = (
    ".codex-plugin/plugin.json",
    "references/five-ledger-model.md",
    "skills/adopt-fifth-ledger/SKILL.md",
)
IGNORE_PROBES = (
    "AGENTS.local.md",
    "local/private-evidence.json",
    "work/scratch.txt",
    "tmp/transient.txt",
    "__pycache__/module.pyc",
    ".pytest_cache/state",
)
MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
UUID = re.compile(
    r"(?i)\b[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}\b"
)


def run_git(*args: str) -> subprocess.CompletedProcess[bytes]:
    """Run one read-only Git query against the declared project root."""
    return subprocess.run(
        ["git", "-C", str(ROOT), *args],
        check=False,
        capture_output=True,
    )


def public_candidates() -> list[Path]:
    """Return tracked and untracked non-ignored public candidate files."""
    result = run_git("ls-files", "--cached", "--others", "--exclude-standard", "-z")
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="replace").strip())
    return sorted(
        ROOT / raw.decode("utf-8")
        for raw in result.stdout.split(b"\0")
        if raw and (ROOT / raw.decode("utf-8")).is_file()
    )


def validate_required_files(errors: list[str]) -> None:
    """Require the documented project-home structure."""
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            errors.append(f"missing or empty required file: {relative}")


def validate_no_implementation_copy(errors: list[str]) -> None:
    """Reject known plugin-canon paths in the project home."""
    for relative in FORBIDDEN_IMPLEMENTATION_PATHS:
        if (ROOT / relative).exists():
            errors.append(f"implementation-canon path must remain external: {relative}")


def validate_profile(errors: list[str]) -> int:
    """Check profile syntax and route reachability without claiming schema authority."""
    try:
        data = tomllib.loads(PROFILE.read_text(encoding="utf-8"))
    except (OSError, UnicodeError, tomllib.TOMLDecodeError) as exc:
        errors.append(f"invalid project profile TOML: {exc}")
        return 0

    if data.get("schema") != "fifth-ledger.project.v1":
        errors.append("project profile must declare fifth-ledger.project.v1")
    if data.get("profile_path") != ".fifth-ledger/project.toml":
        errors.append("project profile path declaration is inconsistent")
    if data.get("status") not in {"proposed", "accepted"}:
        errors.append("project profile status is unsupported")
    if data.get("visibility") not in {
        "tracked-public",
        "ignored-local",
        "external-private",
    }:
        errors.append("project profile visibility is unsupported")

    routes = data.get("routed_paths")
    if not isinstance(routes, list) or not routes:
        errors.append("project profile routed_paths must be a nonempty array")
        return 0

    seen: set[Path] = set()
    valid = 0
    for raw in routes:
        if not isinstance(raw, str) or not raw or raw.startswith("/") or ".." in Path(raw).parts:
            errors.append(f"invalid routed path syntax: {raw!r}")
            continue
        candidate = ROOT / raw
        try:
            resolved = candidate.resolve(strict=True)
            resolved.relative_to(ROOT.resolve())
        except (OSError, RuntimeError, ValueError):
            errors.append(f"routed path does not resolve below project root: {raw!r}")
            continue
        if resolved == ROOT.resolve():
            errors.append(f"routed path must resolve below project root: {raw!r}")
        elif resolved in seen:
            errors.append(f"routed paths alias the same target: {raw!r}")
        else:
            seen.add(resolved)
            valid += 1
    return valid


def markdown_target(raw: str) -> str:
    """Return the path portion of a simple Markdown destination."""
    target = raw.strip()
    if target.startswith("<") and ">" in target:
        target = target[1 : target.index(">")]
    elif " " in target:
        target = target.split(" ", 1)[0]
    return unquote(target)


def validate_markdown_links(paths: list[Path], errors: list[str]) -> int:
    """Resolve local Markdown links in public candidate files."""
    checked = 0
    for path in paths:
        if path.suffix.lower() != ".md":
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (OSError, UnicodeError) as exc:
            errors.append(f"cannot read Markdown file: {path.relative_to(ROOT)}: {exc}")
            continue
        for match in MARKDOWN_LINK.finditer(text):
            target = markdown_target(match.group(1))
            parsed = urlsplit(target)
            if not target or target.startswith("#") or parsed.scheme or parsed.netloc:
                continue
            destination = (path.parent / parsed.path).resolve()
            checked += 1
            try:
                destination.relative_to(ROOT.resolve())
            except ValueError:
                errors.append(
                    f"Markdown link escapes project root: {path.relative_to(ROOT)} -> {target}"
                )
                continue
            if not destination.exists():
                errors.append(
                    f"broken Markdown link: {path.relative_to(ROOT)} -> {target}"
                )
    return checked


def leak_patterns() -> tuple[tuple[str, re.Pattern[str]], ...]:
    """Build leak patterns without embedding a match for the validator itself."""
    mac_root = "/" + "Users" + "/"
    linux_root = "/" + "home" + "/"
    file_uri = "file" + "://"
    private_key = "BEGIN" + r"[^\n]{0,40}" + "PRIVATE" + r"\s+" + "KEY"
    task_field = "source_" + "thread_id"
    token_prefix = "gh" + "p_"
    api_prefix = "sk" + "-"
    return (
        ("macOS absolute user path", re.compile(re.escape(mac_root))),
        ("Linux absolute user path", re.compile(re.escape(linux_root))),
        ("Windows absolute user path", re.compile(r"(?i)\b[A-Z]:\\Users\\")),
        ("local file URI", re.compile(re.escape(file_uri), re.IGNORECASE)),
        ("task/thread identifier field", re.compile(re.escape(task_field), re.IGNORECASE)),
        ("UUID-like task identifier", UUID),
        ("private key material", re.compile(private_key, re.IGNORECASE)),
        ("GitHub token prefix", re.compile(re.escape(token_prefix))),
        ("API key prefix", re.compile(r"\b" + re.escape(api_prefix) + r"[A-Za-z0-9_-]{16,}")),
    )


def validate_public_candidates(paths: list[Path], errors: list[str]) -> int:
    """Scan public candidates for common local, task, and secret leakage."""
    checked = 0
    patterns = leak_patterns()
    for path in paths:
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        except OSError as exc:
            errors.append(f"cannot inspect public candidate: {path.relative_to(ROOT)}: {exc}")
            continue
        checked += 1
        if text and not text.endswith("\n"):
            errors.append(f"missing final newline: {path.relative_to(ROOT)}")
        for line_number, line in enumerate(text.splitlines(), 1):
            if line != line.rstrip(" \t"):
                errors.append(
                    f"trailing whitespace in public candidate: {path.relative_to(ROOT)}:{line_number}"
                )
            for label, pattern in patterns:
                if pattern.search(line):
                    errors.append(
                        f"{label} in public candidate: {path.relative_to(ROOT)}:{line_number}"
                    )
    return checked


def validate_ignore_policy(errors: list[str]) -> int:
    """Confirm local, work, and cache probes are ignored while the boundary README is public."""
    checked = 0
    for relative in IGNORE_PROBES:
        result = run_git("check-ignore", "--quiet", "--", relative)
        checked += 1
        if result.returncode != 0:
            errors.append(f"expected ignored path is not ignored: {relative}")
    readme = run_git("check-ignore", "--quiet", "--", "local/README.md")
    checked += 1
    if readme.returncode == 0:
        errors.append("local/README.md must remain a public boundary document")
    return checked


def main() -> int:
    """Run all project-home checks and return a deterministic exit status."""
    errors: list[str] = []
    validate_required_files(errors)
    validate_no_implementation_copy(errors)
    routes = validate_profile(errors)
    try:
        candidates = public_candidates()
    except RuntimeError as exc:
        errors.append(f"cannot enumerate public candidates: {exc}")
        candidates = []
    links = validate_markdown_links(candidates, errors)
    public_files = validate_public_candidates(candidates, errors)
    ignore_checks = validate_ignore_policy(errors)

    if errors:
        for error in sorted(set(errors)):
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(
        "PASS: "
        f"{len(REQUIRED_FILES)} required files, "
        f"{routes} routed paths, "
        f"{links} local Markdown links, "
        f"{public_files} public candidates, and "
        f"{ignore_checks} ignore-policy checks are coherent"
    )
    print("NOTE: profile schema authority and tracked placement require the canonical implementation validator")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
