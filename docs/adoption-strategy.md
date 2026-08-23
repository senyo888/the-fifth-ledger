# Proportional adoption strategy

## Decision

The most effective operating model is project-owned governance with a small central
coordination lane:

- each target project owns its authority, canon, evidence rules, surfaces, lifecycle,
  and accepted profile;
- The Fifth Ledger project home owns the reusable product direction, adoption method,
  private assessments, and cross-project learning;
- the plugin implementation repository owns skills, schemas, validators, templates,
  and implementation tests;
- no repository becomes a portfolio-wide shadow canon.

## Adoption levels

Choose the lightest level that resolves a real problem.

### No profile

Use when one repository has a clear root contract, one source hierarchy, low-risk local
work, and no meaningful public/private or lifecycle split.

### Minimal profile

Use when a project needs a small reachability router across a few existing sources but
already has clear ownership and precedence. Do not restate those sources in the profile.

### Full profile

Use when a project has several truth lanes, sensitive evidence, external systems,
multiple repositories, safety or commercial authority, or separate implementation,
publication, deployment, and release gates.

### Blocked

Use when ownership, repository boundary, source precedence, privacy placement, or the
profile acceptance authority is unresolved. Resolve that decision before authoring a
profile that would make the ambiguity look settled.

## Efficient workflow

1. Prove the target repository or bounded artifact and current state.
2. Read the smallest source set that owns authority, architecture, validation, privacy,
   surfaces, and lifecycle.
3. Record one adoption assessment: `none`, `minimal`, `full`, or `blocked`.
4. Keep exact paths, identities, and adopter evidence in ignored local assessment
   records.
5. If adoption is approved, edit only the target project and use its existing
   conventions. Do not copy project truth into this project home.
6. Validate routing and placement. Preserve an expected untracked-profile limitation
   until staging is separately authorised.
7. Escalate review only for material risk. A focused owner review is enough for normal
   local documentation; separate-context review is reserved for high-risk, public,
   privileged, deployment, or release work.

## Portfolio registry boundary

The project home may keep an ignored registry of assessments and last observations.
That registry is discovery and continuity evidence only. It cannot approve a target
profile, override target canon, grant permissions, or establish current deployment and
release state.

## Repository architecture rule

Prefer one clear Git root per independently versioned implementation. A private control
workspace may coordinate several sibling implementation repositories, but nested Git
repositories should be used only after an explicit ownership and staging decision.
Otherwise they make public/private classification, commits, and status claims harder to
reason about.

Moving or splitting an existing repository requires a separately approved migration
with path, history, privacy, rollback, and tooling checks. An adoption review may
recommend that structure but must not perform the migration.
