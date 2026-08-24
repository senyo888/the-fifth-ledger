# The 5th Ledger project home

The 5th Ledger helps people and coding agents keep consequential project work
truthful, reviewable, and within authority. This repository is its durable project
home: it holds product direction, source ownership, decisions, research boundaries,
pilot policy, review expectations, and release/publication gates.

The plugin implementation lives in a separate repository. That repository remains the
only source for plugin code, skills, package metadata, implementation architecture,
templates, and implementation tests. This project home must route to that source, not
copy it.

`The 5th Ledger` is the customer-facing display name. The stable technical slug,
repository identities, and historical decision titles retain `the-fifth-ledger` or
`The Fifth Ledger`; no package or repository migration is implied.

## What it helps answer

- Who may decide or change this?
- Which source owns the truth?
- What evidence applies to the exact current state?
- Which documents, product surfaces, and records must agree?
- What has actually been proposed, implemented, validated, published, deployed, or
  released?

## Current maturity

The project home has a private Git baseline and an accepted `0.1.0` distribution
decision. At this point:

- `main` remains the canonical project-home branch;
- Senyo (`senyo888`) is the identified project owner and has accepted the project
  profile;
- the accepted profile's tracked placement is validated against the initial baseline;
- ADR-0003 owns the execution-envelope model and ADR-0004 owns the skills-only
  publication direction;
- two read-only pilots have examined bounded authority and split-repository
  portability, with exact evidence kept private;
- the publication candidate, private installation, Platform draft, review submission,
  approval, and directory publication remain separately evidenced lifecycle facts;
- no Plugins Directory availability, deployment, or release is claimed here;
- the public promise is evidence-bounded and does not claim market demand, compliance,
  enforcement, or guaranteed outcomes.

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
6. Treat the [roadmap](docs/roadmap.md) as planning, not approval.
7. Run the local validator before handing off project-home changes.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 scripts/validate_project.py
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
git diff --check
```

## Next gates

1. Prepare and validate one exact implementation-owned `0.1.0` candidate.
2. Install that exact bundle privately, test it in fresh ChatGPT and Codex contexts,
   then uninstall it and restore the preflight configuration.
3. Complete one validated OpenAI Platform draft and stop before `Submit for Review`.
4. Require Senyo's later exact authority for `Submit for Review`.
5. After confirmed OpenAI approval and containment verification, require Senyo's
   separate exact authority for `Publish`.

The project is licensed under [Apache-2.0](LICENSE). Support is English and best effort
with no service-level agreement; use [public support](SUPPORT.md) for non-sensitive
questions and the [private security route](SECURITY.md) for vulnerabilities.
