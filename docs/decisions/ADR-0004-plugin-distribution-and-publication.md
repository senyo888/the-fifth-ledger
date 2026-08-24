# ADR-0004: Skills-only distribution and public publication path

- Status: accepted
- Date: 2026-08-24
- Decision authority: Senyo (`senyo888`), project owner

## Context

The 5th Ledger has an accepted split-repository architecture and a private skills-only implementation at version `0.1.0`. Publication requires a durable product promise, publisher and licence decisions, coherent public policy/support surfaces, exact candidate evidence, private installation testing, and separate external review and publication gates.

The current OpenAI publication model accepts uploaded skills-only plugins and separates draft creation, review submission, approval, and publication. A public listing does not require an MCP server or a public implementation repository.

## Decision

Prepare version `0.1.0` as a skills-only plugin for the universal Plugins Directory shared by ChatGPT and Codex. Use **The 5th Ledger** as the customer-facing display name while retaining the stable technical slug `the-fifth-ledger`, existing repository identities, and historical decision titles.

- Keep the product local-first, with no MCP server, hooks, apps, connectors, authentication, telemetry, UI, hosted/background runtime, or publisher-operated network service.
- Skills may guide user-authorized local commands, bounded writes, Git operations, or provider reads under the host and project's existing permissions. The plugin grants none of those permissions.
- Use Senyo's exact verified individual OpenAI developer identity initially, if the Platform confirms that identity and it matches the public listing and policy surfaces. Use a business identity only after a separate owner decision confirms an already-verified intended publisher and matching ownership.
- License the public project home and distributed plugin bytes under Apache-2.0. The complete histories identify Senyo as the sole contributor, and the candidate must contain no unlicensed third-party material.
- Keep the implementation repository private through initial OpenAI review. Make only this project home public, and only after its complete Git tree, history, author data, branches, tags, pull requests, comments, issues, releases, and binary metadata pass disclosure review.
- Use this project home as the product website and owner of support, security, privacy, terms, public listing policy, and durable publication decisions.
- Create no additional repository, domain, MCP server, or hosted service for `0.1.0`.
- Provide English product copy and support initially on a best-effort basis with no localization claim or service-level agreement. Use public GitHub issues for non-sensitive support and GitHub private vulnerability reporting for security reports.
- Select every region the current OpenAI Platform permits for this plugin and verified publisher. Do not impose an additional United Kingdom or English-speaking-country restriction; language coverage and geographic availability are separate facts. Stop only if the Platform requires a materially different legal, publisher, support, or regional commitment.

## Public promise

> Structured governance workflows for consequential agentic project work.

The 5th Ledger helps users establish action boundaries, trace claims to project-owned sources, review truth drift across implementation and documentation, structure independent challenge, draft durable decisions, and assess release evidence. It provides procedural guidance only: it does not grant access, enforce policy, certify compliance, connect to a publisher service, or publish, deploy, or release work.

## Non-goals

- access control, runtime orchestration, autonomous approval, or lifecycle automation;
- security scanning, legal advice, or compliance certification;
- external data connection, authentication, telemetry, or publisher data collection;
- guaranteed correctness, adoption, demand, or operational outcomes;
- consolidation or public disclosure of the private implementation repository.

## Source ownership

- This project home owns product direction, public claims, publisher strategy, licence, support, security, privacy, terms, public URLs, lifecycle gates, and durable decisions.
- The implementation repository owns the manifest, skills, packaged assets, compatibility, tests, build tooling, candidate bytes, and release notes.
- Exact repository, candidate, installation, account, and Platform evidence remains in the authorised ignored/private evidence lane.

## Lifecycle and gates

The accepted decision authorizes only the actions separately enumerated in the approved execution charter. Candidate preparation, validation, private installation, Platform draft creation, `Submit for Review`, OpenAI approval, `Publish`, and post-publication observation remain separate facts.

Two later owner gates remain:

1. explicit authority to select `Submit for Review` for one exact reconciled draft;
2. explicit authority to select `Publish` for the exact OpenAI-approved candidate after containment is confirmed.

## Maintenance and containment

Every revised candidate receives a new source and bundle identity and repeats affected validation. Local testing is contained by uninstalling the exact candidate and restoring preflight configuration. Repository changes are reverted additively. A Platform draft may be abandoned. After publication, withdrawal, unpublish, or supersession may be used only when the Platform capability is confirmed; returning a public repository to private cannot retract copied history.

## Consequences

- Public copy must stay within the supported procedural promise and name limitations plainly.
- Project-home disclosure is intentionally late and cannot occur until the complete repository-disclosure review passes.
- A private implementation repository reduces unnecessary history disclosure but does not relax uploaded-bundle review.
- There is no publisher-operated kill switch, telemetry signal, or server-side containment path.

## Validation and next gate

Validate both source-owning repositories, deterministic candidate construction, reviewer-runnable tests, fresh ChatGPT and Codex behavior, exact private installation identity, public links, provider scanning, and draft reconciliation. Stop before `Submit for Review`; that action requires the later exact owner gate.
