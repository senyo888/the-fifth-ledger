# Architecture and source ownership

## Repository architecture

The Fifth Ledger uses a split repository model:

```text
project home
├── product direction and roadmap
├── governance and authority boundaries
├── decisions and review policy
├── pilot/evidence policy
└── private continuity routing

implementation repository
├── plugin package and metadata
├── skills and templates
├── implementation architecture and references
├── validators
└── implementation tests
```

The repositories are peers. Neither is a generated mirror of the other. Moving,
combining, or publishing them as one unit requires a later explicit decision and a
migration plan; this setup performs no migration.

## Topic ownership

| Topic | Canonical source | Notes |
| --- | --- | --- |
| Current task authority | Explicit user or external authority for that task | A repository file cannot grant permission. |
| Project-home operating rules | `AGENTS.md` | Local overrides may narrow, not broaden, tracked policy. |
| Purpose and maturity | `README.md` | Live Git and provider state override stale prose. |
| Repository split | This document and accepted ADRs | ADR-0001 establishes the current split. |
| Product direction | `docs/product-direction.md` | Working direction until accepted decisions refine it. |
| Cross-project adoption strategy | `docs/adoption-strategy.md` | Target projects retain their own canon and acceptance authority. |
| Plans | `docs/roadmap.md` | Planning only; no action or release authority. |
| Decisions | Accepted records under `docs/decisions/` | Newer accepted decisions supersede conflicting older ones. |
| Pilot and adopter evidence | `docs/pilots/README.md` plus the authorised private evidence lane | Public summaries never replace exact evidence. |
| Contribution and review | `CONTRIBUTING.md` | Does not create a remote or provider workflow. |
| Publication and release | `docs/release-publication-gates.md` plus current external evidence | Candidate, published artifact, provider validation, and human decision stay separate. |
| Plugin behavior and packaging | Separate implementation repository | Its current source and tests override project-home summaries. |
| Project routing | `.fifth-ledger/project.toml` | Flat reachability only; not ownership or precedence. |

## Precedence rules

1. Explicit current authority controls allowed action.
2. Accepted ADRs control durable project-home decisions.
3. The source-owning repository controls its implementation or project-home domain.
4. Fresh identity-bound evidence controls observed state.
5. Documentation and reports summarize the sources above and must not invent truth.
6. Roadmaps, proposals, memory, and local continuity remain advisory until accepted.

When two sources at the same level conflict, preserve the conflict and request or record
a decision. Do not resolve it by copying one source into another repository.

## Profile boundary

The project profile routes only to paths inside this project home because its structural
format is target-root-relative. It cannot route directly to a machine-local external
repository without leaking a path or misrepresenting scope. The external implementation
route therefore lives in ignored `AGENTS.local.md`, while this document records its
topic ownership in portable terms.

The profile is accepted by project owner Senyo (`senyo888`) but its tracked placement
remains unverified. Its route syntax and reachability may be checked without staging.
Tracked-public placement cannot be proved until staging is separately authorised, and
acceptance does not imply staging.

## Surface ownership

- Project-home surfaces: README, governance docs, ADRs, pilot policy, contribution
  policy, release gates, and private continuity routing.
- Implementation surfaces: plugin metadata, skill instructions, templates,
  validators, implementation documentation, and tests.
- External surfaces: plugin listing, marketplace record, remote repository, provider
  validation, published artifact, installation, deployment, and release evidence.

An external surface becomes current truth only through its own evidence and authority.
