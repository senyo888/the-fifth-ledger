# Project-home tests

The tests exercise the local project validator, profile reachability, ignore boundary,
and no-shadow implementation boundary using only Python's standard library.

Run without bytecode output:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 -m unittest discover -s tests -v
```

These tests validate the project home only. They do not validate the separate plugin
implementation, provider state, publication, installation, deployment, or release.
