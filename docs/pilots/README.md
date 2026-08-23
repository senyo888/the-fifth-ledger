# Pilot and evidence policy

Pilots exist to test a bounded product hypothesis, not to manufacture adoption proof.

## Before a pilot

Record:

- target class and decision question;
- adopter/evidence owner and permitted action level;
- canonical sources and exact target identity method;
- private evidence lane, retention, and deletion authority;
- success, failure, friction, and stop criteria;
- validation coverage and known unavailable checks;
- whether a sanitized public summary is wanted at all.

If identity, authority, privacy, or evidence ownership is unresolved, do not collect
real adopter evidence.

## Evidence lanes

- Exact adopter evidence belongs in `local/pilots/` or another explicitly authorised
  private lane. It must not be staged.
- Public-ready summaries may be proposed under `docs/pilots/` only after a separate
  privacy and truth review.
- Any summary intended for the implementation repository must meet that repository's
  current pilot-evidence contract. Do not copy the contract here or assume it has not
  changed.
- Research notes that contain identities, raw quotes, repository evidence, or local
  paths belong in `local/research/`.

## Minimum evidence record

- bounded objective and authority;
- exact or explicitly unavailable identity;
- observation time and commands or methods;
- findings separated into confirmed, contradicted, incomplete, and unavailable;
- validator side effects and mutation parity;
- public/private classification;
- decision state, unresolved risk, and next gate;
- actions not performed.

## Public-summary rules

A public summary must not include personal or adopter identity, local paths, task
identifiers, credentials, private repository identity, raw reports, exact unpublished
evidence, or claims that exceed the observed scope. Target class, generalized behavior,
material friction, coverage limitations, decision state, and the location class of exact
private evidence are usually sufficient.

Public information is not automatically owned by this project. Publication requires
separate authority and current sanitization review.

## Lifecycle

Keep pilot proposed, authorised, running, stopped, validated, reviewed, accepted,
rejected, and archived states distinct. A successful pilot does not approve an
implementation change or public release. A stopped or contradicted pilot remains useful
evidence and must not be rewritten into a pass.
