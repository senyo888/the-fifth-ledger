# Release and publication gates

This project home records gates; it does not grant the authority they require.

## Separate lifecycle facts

Keep these facts distinct:

1. project-home decision accepted;
2. implementation change authored;
3. exact implementation identity validated;
4. project-home and implementation surfaces reconciled;
5. candidate package produced;
6. provider or marketplace validation completed;
7. human publication or release decision recorded;
8. artifact published;
9. installation or deployment observed;
10. post-publication behavior reviewed.

Evidence for one fact cannot stand in for another.

## Pre-publication gate

Before any public repository, listing, submission, or release action, require:

- explicit authority for the exact external action;
- current project-home and implementation repository identities;
- an accepted scope and source-ownership decision;
- a license decision and an explicit security/contact decision;
- current platform requirements verified from authoritative sources;
- implementation tests and package validation against the exact candidate;
- project-home link, privacy, path-leak, and claim checks;
- sanitized evidence supporting every material public claim;
- compatibility, migration, support, and rollback statements;
- unresolved disagreements and unavailable validation kept visible;
- a separate human publication/release decision.

## Repository and remote gate

Creating a remote, pushing history, opening a pull request, changing visibility, or
configuring branch protection are separate external actions. The local repository's
existence and readiness do not authorise them.

## Marketplace or provider gate

Registration, submission, review, publication, installation, and provider validation
remain distinct. Recheck current provider documentation when this gate becomes active;
do not rely on a historical research note.

## Release evidence record

Record at minimum:

- candidate version and exact source identity;
- package or artifact identity;
- test commands and results;
- provider validation identity, time, and result;
- documentation and public-claim review;
- privacy and secret scan result;
- known limitations and rollback path;
- human decision, decision owner, and actions still unauthorised.

## Stop conditions

Stop and report rather than publish when ownership, authority, source precedence,
candidate identity, license, privacy, current provider requirements, validation, or
rollback is unavailable or contradictory.
