# The Fifth Ledger project home

This repository is the durable control workspace for The Fifth Ledger: an
evidence-first governance workflow for agentic project work. It holds product
direction, source ownership, decisions, research boundaries, pilot policy, review
expectations, and release/publication gates.

The plugin implementation lives in a separate repository. That repository remains the
only source for plugin code, skills, package metadata, implementation architecture,
templates, and implementation tests. This project home must route to that source, not
copy it.

## Current maturity

The project home has an initial private Git baseline. At this point:

- `main` is the canonical private project-home branch;
- the private GitHub remote provides continuity but is not public publication;
- Senyo (`senyo888`) is the identified project owner and has accepted the project
  profile;
- the accepted profile's tracked placement is validated against the initial baseline;
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

1. Use the accepted Mail Handler adoption as the first bounded pilot, with exact
   evidence retained in its private lane.
2. Record only generalized, public-safe learning in this project home after review.
3. Select the next bounded pilot objective and define its evidence owner, privacy lane,
   success criteria, and stop rule before collecting real adopter evidence.
4. Reconcile any product or workflow changes into the implementation repository only
   through separately authorised implementation work.
5. Consider publication only after the gates in
   [release and publication](docs/release-publication-gates.md) are evidenced.

No license or security contact is declared in this repository. Do not infer reuse
rights or a reporting channel until those decisions are made explicitly.
