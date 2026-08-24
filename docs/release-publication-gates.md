# Release and publication gates

This project home records gates; it does not grant the authority they require.

An explicitly approved [execution charter](execution-charter-template.md) may enumerate
several private or external actions in one ordered phase. Each target, identity,
permission, intervening stop condition, and rollback must still be stated. The charter
cannot borrow release authority from an earlier pilot or product decision.

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

For the accepted `0.1.0` path, one bounded execution charter may cover product-decision
reconciliation, exact candidate preparation, private installation, private Git review,
late project-home disclosure, and one complete Platform draft. It must stop before
`Submit for Review`. OpenAI approval does not authorize `Publish`; each action requires
its own exact owner statement.

The implementation repository remains private. Uploaded candidate bytes still require
the same validation, rights, security, privacy, and provider review as public source.

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

## Public repository disclosure gate

Before changing project-home visibility, inspect the current tree and complete Git
history, author identities, every live branch and tag, pull request bodies and comments,
issues and comments, releases, and binary ancillary metadata. A passing current-tree
secret scan is insufficient. Stop on any private identifier, local path, unpublished
evidence, unlicensed material, ambiguous provider object, or need for history rewrite.

Returning a repository to private is containment only and cannot retract copies or
caches. The private implementation repository must not be made public through this
gate.

## Post-publication containment gate

Before final publication, confirm the Platform's current withdrawal, unpublish, or
supersession capability. If none can be confirmed, require an explicit owner decision
accepting supersession as the containment path. Do not advertise a rollback control
that has not been observed.
