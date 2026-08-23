# The Fifth Ledger project home

The Fifth Ledger helps people and coding agents keep consequential project work
truthful, reviewable, and within authority. This repository is its durable project
home: it holds product direction, source ownership, decisions, research boundaries,
pilot policy, review expectations, and release/publication gates.

The plugin implementation lives in a separate repository. That repository remains the
only source for plugin code, skills, package metadata, implementation architecture,
templates, and implementation tests. This project home must route to that source, not
copy it.

## What it helps answer

- Who may decide or change this?
- Which source owns the truth?
- What evidence applies to the exact current state?
- Which documents, product surfaces, and records must agree?
- What has actually been proposed, implemented, validated, published, deployed, or
  released?

## Current maturity

The project home has an initial private Git baseline. At this point:

- `main` is the canonical private project-home branch;
- the private GitHub remote provides continuity but is not public publication;
- Senyo (`senyo888`) is the identified project owner and has accepted the project
  profile;
- the accepted profile's tracked placement is validated against the initial baseline;
- ADR-0003 records the accepted execution-envelope model; the first read-only pilot
  has reached synthesis, with exact evidence retained privately and no target or plugin
  change accepted;
- no publication, installation, marketplace registration, deployment, or release is
  claimed here;
- product positioning is a working direction, not a verified market claim.

Current Git state always overrides this dated orientation when they diverge.

## Repository split

| Repository | Owns | Must not own |
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
- [Roadmap](docs/roadmap.md) — current and future gates, never action authority.
- [Decision records](docs/decisions/README.md) — accepted durable choices.
- [Execution charter template](docs/execution-charter-template.md) — make one bounded
  approval operational without turning a document into authority.
- [Pilot policy](docs/pilots/README.md) — evidence ownership and privacy.
- [Release and publication gates](docs/release-publication-gates.md) — proof required
  before external claims or actions.

## Working model

1. Start with [AGENTS.md](AGENTS.md) and prove the current target and authority.
2. Use the [source map](docs/source-ownership.md) to find the owning source.
3. Apply the [adoption strategy](docs/adoption-strategy.md) before adding governance
   weight to another project.
4. Record durable product choices as [ADRs](docs/decisions/README.md).
5. Keep exact adopter evidence in the ignored local lane defined by the
   [pilot policy](docs/pilots/README.md).
6. Treat the [roadmap](docs/roadmap.md) as planning, not approval.
7. Run the local validator before handing off project-home changes.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_project.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
```

## Next gates

1. Review the first pilot at Checkpoint 2 and choose independently among early close,
   documentation-only follow-up, another pilot, a bounded private plugin proposal, or
   optional distribution research.
2. Keep the exact pilot packet private; only generalized, evidence-bounded learning may
   enter tracked documentation.
3. If another pilot is chosen, define its evidence owner, privacy lane, success
   criteria, retention, and stop rule before collecting evidence.
4. Reconcile any accepted product or workflow change into the implementation repository only
   through separately authorised implementation work.
5. Consider publication only after the gates in
   [release and publication](docs/release-publication-gates.md) are evidenced.

No license or security contact is declared in this repository. Do not infer reuse
rights or a reporting channel until those decisions are made explicitly.
