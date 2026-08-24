# The 5th Ledger project home

The 5th Ledger helps people and coding agents keep consequential project work
truthful, reviewable, and within authority. This repository is its durable project
home: it holds product direction, source ownership, decisions, research boundaries,
pilot policy, review expectations, and release/publication gates.

The plugin implementation lives in a separate repository. That repository remains the
only source for plugin code, skills, package metadata, implementation architecture,
templates, and implementation tests. This project home routes to that source and keeps
implementation truth there.

`The 5th Ledger` is the customer-facing display name. The stable technical slug,
repository identities, and historical decision titles retain `the-fifth-ledger` or
`The Fifth Ledger`; package and repository identities remain unchanged.

## What it helps answer

- Who may decide or change this?
- Which source owns the truth?
- What evidence applies to the exact current state?
- Which documents, product surfaces, and records must agree?
- What has actually been proposed, implemented, validated, published, deployed, or
  released?

## Current maturity

The project home is public and The 5th Ledger `0.1.0` is published in OpenAI's
universal Plugins Directory for ChatGPT and Codex. At this point:

- `main` remains the canonical project-home branch;
- Senyo (`senyo888`) is the identified project owner and has accepted the project
  profile;
- the accepted profile's tracked placement is validated against the initial baseline;
- ADR-0003 owns the execution-envelope model and ADR-0004 owns the skills-only
  publication direction;
- two read-only pilots have examined bounded authority and split-repository
  portability, with exact evidence kept private;
- the exact publication candidate, private installation, Platform draft, review
  submission, approval, and publication remain separately evidenced lifecycle facts;
- the public listing is available at
  [The 5th Ledger in the Plugins Directory](https://chatgpt.com/plugins/plugins_6a8c4d64d6588191acd217005a66224d);
- authenticated ChatGPT installation and bounded fresh-chat smoke tests passed after
  publication, and authenticated installed state was observed again on 2026-08-24;
- one fresh Codex desktop task registered all eight public `0.1.0` skills and the named
  workflows behaved safely; a separate fresh ephemeral Codex context lacked one named
  skill, so cross-context propagation remains an open post-publication observation;
- fresh ChatGPT message behavior, anonymous listing detail, visible support-link
  presentation, and current Platform containment controls remain open evidence from the
  later observation;
- the implementation repository remains private and continues to own implementation
  and candidate truth;
- the public promise stays within observed procedural behavior, while market demand,
  compliance, enforcement, and guaranteed outcomes remain outside its claims.

Current Git state always overrides this dated orientation when they diverge.

## Repository split

| Repository | Owns | Owned elsewhere |
| --- | --- | --- |
| Project home | Direction, governance, ADRs, research, pilots, review policy, private continuity routing, publication gates | Plugin source, package metadata, skill behavior, implementation tests, release artifacts |
| Implementation repository | Plugin package, skills, templates, implementation architecture, validators, implementation tests | Adopter truth, raw pilot evidence, project-home decisions, private continuity |

See [source ownership](docs/source-ownership.md) and
[ADR-0001](docs/decisions/ADR-0001-project-home-boundary.md) for the controlling
boundary.

## Where to look

- [Documentation index](docs/README.md) — choose the right source by question.
- [Source ownership](docs/source-ownership.md) — repository split and precedence.
- [Product direction](docs/product-direction.md) — working purpose, audience, and
  non-goals.
- [Roadmap](docs/roadmap.md) — current and future gates; explicit owner decisions
  provide action authority.
- [Decision records](docs/decisions/README.md) — accepted durable choices.
- [Execution charter template](docs/execution-charter-template.md) — make one bounded
  owner approval operational while authority stays with that decision.
- [Pilot policy](docs/pilots/README.md) — evidence ownership and privacy.
- [Release and publication gates](docs/release-publication-gates.md) — proof required
  before external claims or actions.
- [Plugin Directory publication record](docs/publication/plugin-directory-0.1.0.md) —
  accepted public promise and exact lifecycle boundary for `0.1.0`.
- [Support](SUPPORT.md), [security](SECURITY.md), [privacy](PRIVACY.md), and
  [terms](TERMS.md) — public owner-operated policy and reporting surfaces.

## Working model

1. Start with [AGENTS.md](AGENTS.md) and prove the current target and authority.
2. Use the [source map](docs/source-ownership.md) to find the owning source.
3. Apply the [adoption strategy](docs/adoption-strategy.md) before adding governance
   weight to another project.
4. Record durable product choices as [ADRs](docs/decisions/README.md).
5. Keep exact adopter evidence in the ignored local lane defined by the
   [pilot policy](docs/pilots/README.md).
6. Use the [roadmap](docs/roadmap.md) for planning and explicit owner decisions for
   approval.
7. Run the local validator before handing off project-home changes.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_project.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
```

## Post-publication follow-up

1. Run a separately authorised seven-day manual observation across 5–10 non-sensitive
   ChatGPT and Codex uses, recording activation precision, safe handling, usefulness,
   and cross-client consistency in the ignored evidence lane.
2. Select one later low-risk, non-sensitive, read-only adoption pilot whose target
   project retains its own Canon and decision owner.
3. Propose `0.1.1` only when identity-bound evidence supports a defect or a coherent
   high-value improvement; each later candidate, review, submission, and publication
   action receives its own identity and owner decision.
4. Run a lightweight monthly read-only check of listing visibility, policy routes,
   vulnerability reporting, support issues, provider requirements, and observed
   containment controls.
5. Route ordinary support through [SUPPORT.md](SUPPORT.md) and vulnerabilities through
   the private path in [SECURITY.md](SECURITY.md).

The project is licensed under [Apache-2.0](LICENSE). Support is English and best effort;
service-level commitments remain a future decision. Use
[public support](SUPPORT.md) for non-sensitive questions and the
[private security route](SECURITY.md) for vulnerabilities.
