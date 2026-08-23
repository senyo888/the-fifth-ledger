# ADR-0003: Decision-backed execution authority envelopes

- Status: accepted
- Date: 2026-08-23
- Decision authority: Senyo (`senyo888`), project owner

## Context

Treating every edit, validation, stage, commit, push, and private review step as a new
decision creates avoidable interruptions. Treating one broad approval as permanent
authority creates the opposite problem: scope, identity, evidence, and lifecycle gates
can drift while work continues.

The project needs a calm middle path that makes owner decisions less frequent without
weakening source ownership, privacy, or the separation between proposal,
implementation, validation, publication, installation, deployment, and release.

## Decision

Use explicit, expiring execution authority envelopes for bounded phases.

Each envelope must name its decision owner, question, exact targets and starting state,
concrete allowed and excluded actions, source owners, evidence lanes, validation,
review, retention, rollback, stop conditions, early-close paths, and expiry. Exact
private identity belongs in the authorised private record.

The operating route has at most three material checkpoints:

1. operating charter and bounded private pilot;
2. evidence-backed product decision and, only when accepted, a private candidate;
3. an exact frozen release and enumerated external actions, only if distribution is
   pursued.

Private-only, no-change, documentation-only, another-pilot, and deferred outcomes may
close earlier. Distribution is optional and is not coupled to a successful pilot.

Material work is branch-first. Direct changes to private `main` are disabled by
default and require an exact mechanical-maintenance allowlist. Private pushes and draft
pull requests are provider actions and must be listed even though they are not public
publication.

Escalation is stop-only within an approved envelope. A stop preserves evidence and
returns a concise blocker; it does not broaden authority. An envelope expires at its
next checkpoint, on identity or scope drift, when a stop condition fires, or at its
stated maximum duration.

For durable high-impact decisions, independent reviewers receive the same preserved
packet before synthesis. One substantive cross-review round is sufficient; disagreement
is recorded rather than converted into a vote.

An ADR, roadmap, proposal, template, or repository instruction records the operating
model but cannot grant permission. Only an explicit decision for the concrete envelope
authorises its listed actions.

## Considered alternatives

### Request approval for every mechanical action

Rejected as the default. It obscures the few decisions that genuinely require owner
judgment and makes a well-bounded phase unnecessarily slow.

### Grant permanent standing authority by action class

Rejected. A label cannot safely capture target identity, private evidence, provider
state, expiry, or a future action whose consequences are not yet known.

### Approve the complete private-to-public lifecycle in advance

Rejected. Pilot findings, public claims, licenses, provider requirements, release
bytes, installation targets, and rollback evidence are not known at the first gate.

## Consequences

- One owner decision may cover branch creation, bounded editing, validation, staging,
  atomic commits, private pushes, draft review, and merge when each action is stated.
- Workers stop only for a listed condition or a genuinely new decision, not for an
  already approved mechanical step.
- Dirty or concurrently active targets can be observed only when the envelope records
  that state, fingerprints it privately, forbids mutation, and stops on byte drift.
- No pilot result can silently authorise plugin behavior, public claims, provider
  mutation, installation, deployment, or release.
- Public disclosure remains an exact owner checkpoint because returning a repository
  to private cannot retract earlier copies or caches.
- The reusable format lives in the
  [execution charter template](../execution-charter-template.md).

## Runtime, UI, migration, and release impact

Runtime impact: none. Entity, service, package, provider, and UI semantics are
unchanged.

Migration or restart: none.

Publication and release: none. This decision creates no public visibility, license,
security contact, installation, deployment, marketplace action, or release authority.

## Validation and next gate

Validate project-home structure, links, profile routing, privacy boundaries, and exact
Git state. The next gate is an evidence-bound product decision; no plugin change or
distribution step is implied.
