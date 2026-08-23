# The Fifth Ledger project-home contract

## Purpose

This repository is the durable project home for The Fifth Ledger. It owns product
direction, governance, decisions, research, pilot policy, review records, and private
continuity boundaries. It does not own the plugin implementation.

The separate implementation repository remains canonical for plugin code, package
metadata, skills, templates, implementation architecture, and implementation tests.
Its machine-local location belongs only in `AGENTS.local.md`. Never copy that source
into this repository or treat a routed profile as a second implementation canon.

## Authority boundary

- User instructions for the current task define action authority.
- Reading, assessment, planning, proposal, implementation, staging, commit, remote
  creation, push, publication, installation, deployment, marketplace registration,
  and release are separate actions.
- Do not infer a later lifecycle action from authority for an earlier one.
- Do not mutate the implementation repository or another project unless that exact
  target and action are separately authorised.
- Treat validators as potential writers. Use no-cache modes where practical and
  inspect resulting state before claiming parity.

## Canonical source map

| Topic | Project-home source | Precedence |
| --- | --- | --- |
| Operating and authority rules | `AGENTS.md` | Current user authority still controls the task. |
| Local private routing | ignored `AGENTS.local.md` | Supplements but never overrides tracked policy. |
| Purpose and maturity | `README.md` | Current live Git state overrides stale status text. |
| Repository split and source ownership | `docs/source-ownership.md` and accepted ADRs | The implementation repository owns implementation truth. |
| Product direction and positioning | `docs/product-direction.md` | Accepted ADRs supersede working direction. |
| Cross-project adoption strategy | `docs/adoption-strategy.md` | Projects retain their own truth and adoption authority. |
| Planned work | `docs/roadmap.md` | A roadmap is not approval or release truth. |
| Decisions | `docs/decisions/` | Newer accepted ADRs supersede older conflicting decisions. |
| Pilot and evidence handling | `docs/pilots/README.md` | Exact adopter evidence stays in its authorised private lane. |
| Contribution and review | `CONTRIBUTING.md` | Applies only within separately granted action authority. |
| Execution-envelope format | `docs/execution-charter-template.md` | Records an explicit approval; it never creates one. |
| Publication and release gates | `docs/release-publication-gates.md` | External state requires current external evidence and explicit authority. |
| Structural routing | `.fifth-ledger/project.toml` | Reachability only; it does not encode topic ownership or precedence. |

If these sources conflict, preserve the contradiction and resolve it through an ADR
or explicit authority decision. Do not silently choose the most convenient statement.

## Privacy and lane separation

- Tracked files must be portable and public-ready.
- Keep secrets, credentials, personal data, exact adopter evidence, raw pilot data,
  machine-local paths, task or thread identifiers, private repository identities, and
  unpublished operational truth out of tracked files.
- Store local continuity and exact evidence only under ignored `local/` paths or in an
  explicitly authorised external private lane.
- Use `work/` for disposable scratch and generated intermediates. It is ignored and
  is not evidence or canon.
- Public summaries must be sanitized, evidence-bounded, and separately reviewed.
- Never use public documentation to imply publication, installation, adoption,
  validation, or release that has not occurred.

## Working model

1. Prove the target, Git identity, applicable source map, and action authority.
2. Classify the requested outcome and proportional governance level.
3. Work in the smallest correct source-owning repository.
4. For a multi-action phase, use an explicitly approved, expiring
   [execution charter](docs/execution-charter-template.md); the template itself grants
   nothing.
5. Keep proposals, decisions, implementation, validation, publication, and release
   distinct.
6. Update every affected project-home surface in one coherent change.
7. Run `PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_project.py` and the relevant
   tests. Report checks that were unavailable or intentionally not run.
8. Re-prove Git status and list actions not performed.

## Validation expectations

For project-home changes, validate at least:

- required files and routed paths;
- TOML, JSON, or YAML syntax when those formats are changed;
- relative Markdown links;
- tracked/public candidates for common local-path, task-identifier, and secret leaks;
- ignored local, work, and cache boundaries;
- absence of copied plugin package or skill canon;
- `git diff --check`, plus exact branch, commit, upstream, remote, tracked, ignored,
  and untracked state as relevant.

Passing local checks proves only the checked project-home bytes. It does not validate
the separate implementation repository, a provider, a publication, a deployment, or a
release.

## No-shadow-authority rule

This repository may record decisions about product direction and governance, and may
route workers to the implementation repository. It must not duplicate implementation
skills, schemas, package files, or release truth. The Fifth Ledger is procedural
governance, not access control and not proof of its own compliance.
