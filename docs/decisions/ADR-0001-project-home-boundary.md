# ADR-0001: Separate project home and implementation repository

- Status: accepted
- Date: 2026-08-23
- Decision authority: explicit project-home setup authority

## Context

The Fifth Ledger already has a separate plugin implementation repository. A durable
saved project is needed for product direction, governance, decisions, research, pilots,
and private continuity. Duplicating implementation source here would create shadow
canon, unclear release ownership, and avoidable drift.

## Decision

Use this repository as the project home and control workspace. Keep the separate plugin
repository as the canonical implementation source.

- Project-home files may describe the relationship and route local workers to the
  implementation source through ignored continuity.
- Plugin code, skills, templates, package metadata, implementation architecture,
  validators, and implementation tests remain in the implementation repository.
- No files are moved, duplicated, staged, committed, published, installed, or deployed
  by this decision.
- Any future consolidation or migration requires a new proposed ADR, exact identity
  checks, privacy review, migration plan, rollback plan, and explicit authority.

## Considered alternatives

### Duplicate implementation into the project home

Rejected. It creates two plausible sources for the same product behavior and release
state.

### Move implementation into the project home now

Rejected for this setup. Migration was not authorised and would alter the established
implementation repository.

### Keep only informal notes with no durable project home

Rejected. Product direction, evidence policy, and decisions need a stable source-owned
workspace distinct from task history.

## Consequences

- Workers must prove which repository owns each requested change before editing.
- Cross-repository changes require separately bounded authority and validation in each
  source-owning repository.
- Machine-local implementation routing stays ignored and cannot be required for public
  review.
- The project profile routes only project-home paths and cannot encode the external
  implementation location.
- Publication and release state cannot be inferred across the repository boundary.

## Validation and next gate at acceptance

Validate the project-home source map, profile reachability, privacy boundary, and absence
of copied plugin package paths. The next decision is ownership and profile acceptance,
not repository migration. That decision was later completed; the current next gates
are recorded in the roadmap.
