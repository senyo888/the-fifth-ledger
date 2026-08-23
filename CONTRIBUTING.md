# Contributing

The Fifth Ledger project home accepts small, source-owned changes to product direction,
governance, decisions, research policy, pilot design, review expectations, and
publication gates. Plugin implementation changes belong in the separate implementation
repository.

## Before changing files

1. Read `AGENTS.md` and `docs/source-ownership.md`.
2. Prove the current repository, branch, commit state, remote, upstream, and working
   tree.
3. State the requested outcome and exact mutation authority.
4. Identify the canonical source for the topic. If ownership or precedence is unclear,
   record the gap rather than creating a second policy source.

## Change rules

- Keep each change bounded to one clear decision or maintenance objective.
- Use an ADR for durable choices that change ownership, product direction, lifecycle
  gates, compatibility, or repository structure.
- Update affected documentation and validation in the same coherent change.
- Keep tracked content portable and public-ready.
- Do not add raw pilot evidence, personal data, credentials, local paths, adopter
  identities, private repository evidence, or task identifiers.
- Do not copy plugin code, skills, schema validators, templates, or package metadata
  into this repository.
- Preserve unknown, proposed, unavailable, contradicted, and deferred states.

## Review expectations

Every review should state:

- bounded files and decision being reviewed;
- canonical sources and assumptions;
- authority granted and actions not authorised;
- public/private and lifecycle impact;
- validation actually run, with unavailable checks explicit;
- contradictions, residual risk, rollback or supersession path, and next gate.

Use one focused review for low-risk documentation. Require separate-context review only
when the decision's impact or uncertainty justifies it; never label shared-context
role-play as independent.

## Execution charters

For a bounded phase with several pre-agreed actions, use the
[execution charter template](docs/execution-charter-template.md). The concrete charter
must list exact targets and permissions for editing, validation, staging, commit, push,
private review, merge, or external action. Its explicit owner approval is the authority;
the template and [ADR-0003](docs/decisions/ADR-0003-decision-backed-authority-envelopes.md)
are not.

Stop when the observed identity changes, the work needs an unlisted action, a privacy
boundary is threatened, or a required check fails. Do not request a fresh decision for
an already listed mechanical step while the charter remains valid.

## Validation

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_project.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
git status --short --branch
```

If the Fifth Ledger implementation repository is available read-only, also run its
canonical profile validator against `.fifth-ledger/project.toml`. For a newly authored
tracked-public profile, an expected placement failure must remain visible until staging
is separately authorised; do not stage merely to make validation pass.

## External actions

Staging, commit, remote creation, push, pull request creation, publication,
installation, marketplace registration, deployment, release, and external
communication each require explicit authority. A private continuity remote exists; no
public contribution channel is currently declared.

No license or security contact is currently declared. Do not infer reuse rights or a
private reporting address.
