# Execution charter template

Use this template when one decision should authorise a bounded phase without requiring
approval for every mechanical step. Keep exact private identities and evidence in the
authorised private lane; tracked summaries must remain portable and public-ready.

Completing this template does not grant authority. Work may begin only after the named
decision owner explicitly approves the concrete charter. A repository file, ADR,
roadmap, proposal, or action-class label cannot substitute for that approval.

## 1. Decision and duration

- Charter ID:
- Phase and bounded question:
- Decision owner:
- Evidence owner:
- Explicit approval record and time:
- Starts:
- Expires: at the next checkpoint, on a stated date, or when a stop condition fires,
  whichever comes first.
- Early-close outcomes:

## 2. Targets and starting state

For every repository, provider account, environment, or other target, record:

- role and source ownership;
- exact identity method and observation time;
- branch, upstream, remote, account, and environment where applicable;
- whether a clean or deliberately observed dirty state is permitted;
- concurrent-work policy and the change that invalidates the observation.

Put machine-local paths, private repository identities, account details, and exact
adopter evidence only in the private record.

## 3. Concrete permissions

Mark each action `allowed`, `not allowed`, or `not applicable`, then state its exact
target and limit. Do not use a broad class label in place of this list.

| Action | State | Exact target and limit |
| --- | --- | --- |
| Inspect or research |  |  |
| Create ignored-local evidence |  |  |
| Create a branch |  |  |
| Edit named surfaces |  |  |
| Run named validators or tests |  |  |
| Stage |  |  |
| Commit |  |  |
| Push to an existing private remote |  |  |
| Open or update a private draft pull request |  |  |
| Merge the named source branch into its approved base and push that base |  |  |
| Create or change a remote |  |  |
| Mutate a provider or account |  |  |
| Mutate a runtime |  |  |
| Change a UI |  |  |
| Change repository or artifact visibility |  |  |
| Communicate externally |  |  |
| Publish |  |  |
| Install |  |  |
| Deploy |  |  |
| Register or submit to a marketplace |  |  |
| Release or promote |  |  |
| Delete, revoke, unpublish, or remove |  |  |
| Rewrite history or force-push |  |  |

List actions that remain expressly excluded, including credentials, billing, legal
acceptance, external communication, destructive operations, and scope outside the
named source-owning repositories.

## 4. Change and evidence budget

- Permitted files and product surfaces:
- Runtime, entity, service, UI, migration, and release impact allowed:
- Maximum duration, commits, or other useful change budget:
- Private evidence lane:
- Public-summary rule and sanitisation reviewer:
- Retention period:
- Deletion authority:

Exact evidence must identify confirmed, contradicted, incomplete, and unavailable
facts. It must record validator side effects and actions not performed.

## 5. Required validation and review

For each check, name the exact command or method, target identity, expected result, and
whether the check may write caches or other files. State which unavailable result must
stop the phase.

If independent review is proportionate, give each reviewer the same preserved input
before synthesis. Keep initial findings separate, allow one substantive cross-review
round, preserve disagreements, and state what final artifact each reviewer actually
reviewed.

## 6. Stop conditions

Stop and preserve evidence when any applicable condition occurs:

- target, branch, remote, account, environment, or candidate identity drifts;
- unexplained or concurrent work changes the observed bytes;
- the needed action is not explicitly allowed;
- private evidence, credentials, adopter identity, or local paths risk entering a
  public candidate;
- required validation fails or is materially unavailable;
- source ownership, lifecycle truth, privacy, rollback, or reviewer findings conflict;
- provider permissions, terms, costs, authentication, or publication semantics differ
  from the accepted sequence;
- a runtime, UI, deployment, provider, or external action exceeds the charter;
- rollback is destructive or unavailable;
- the checkpoint, early-close outcome, or expiry is reached.

A stop permits read-only evidence preservation and a blocker report. It does not permit
improvisation or a broader action.

## 7. Rollback, closeout, and next decision

- Reversible local rollback or additive-revert method:
- Automatic containment allowed:
- Destructive actions requiring a new decision:
- Exit evidence:
- Required lifecycle and source-map reconciliation:
- Actions confirmed not performed:
- Next owner decision, including valid no-change and defer options:

Close the charter when its question is answered, even when the answer is no change,
defer, or another pilot. Completion does not imply implementation, merge, publication,
installation, deployment, promotion, or release.
