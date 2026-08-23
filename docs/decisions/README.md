# Decision records

Use an architecture decision record (ADR) for a durable choice that changes product
direction, source ownership, lifecycle gates, privacy, compatibility, repository
structure, or governance weight.

## Index

| ADR | Status | Decision |
| --- | --- | --- |
| [ADR-0001](ADR-0001-project-home-boundary.md) | Accepted | Keep the project home separate from the plugin implementation repository. |
| [ADR-0002](ADR-0002-proportional-adoption-model.md) | Accepted | Use project-owned, risk-proportional adoption with private central coordination only. |

## Record format

Each ADR should include:

- status: proposed, accepted, superseded, or rejected;
- date and decision authority;
- decision question and bounded context;
- canonical sources and evidence;
- considered options and trade-offs;
- decision and consequences;
- public/private, migration, compatibility, and lifecycle impact;
- validation and next gate;
- supersession link when relevant.

Acceptance records a decision; it does not authorise implementation, staging, commit,
publication, deployment, or release unless that exact action is stated by the deciding
authority.
