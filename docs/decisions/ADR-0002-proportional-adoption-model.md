# ADR-0002: Project-owned, proportional adoption

- Status: accepted
- Date: 2026-08-23
- Decision authority: Senyo (`senyo888`), project owner

## Context

New projects created after the original Fifth Ledger work have materially different
risk and repository structures. Repeating a large governance loop in every project
would add friction, while centralizing their truth in this project home would create
shadow authority.

## Decision

Use a proportional adoption model:

- no profile when existing routing is already sufficient;
- a minimal target-owned profile for modest source-routing needs;
- a full target-owned profile for multiple truth lanes, sensitive evidence, external
  systems, safety or commercial gates, or several lifecycle surfaces;
- a blocked assessment when ownership, privacy, repository boundaries, or precedence
  is unresolved.

Keep exact cross-project assessments in this project home's ignored private lane. The
target project retains profile acceptance authority and all project truth.

Prefer independently versioned implementation repositories as siblings rather than
ambiguous nested Git roots. Any migration remains a separate decision and action.

## Consequences

- The Fifth Ledger project home becomes a coordination and learning surface, not a
  portfolio-wide authority database.
- New projects receive only the governance weight justified by risk.
- High-risk projects can use full profiles without forcing the same ceremony onto
  simple repositories.
- Existing project structure is not changed by a suitability review.
- Profile creation, staging, commit, remote work, and publication remain separate
  authority gates.

## Validation and next gate at acceptance

Maintain private, evidence-bound suitability records and update public strategy only
with generalized conclusions. At acceptance, the next implementation candidate was the
project whose owner approved the highest-value unblocked adoption. Current gates are
recorded in the roadmap.
