# Project-home scripts

`validate_project.py` performs dependency-free checks for this project home's required
structure, Markdown references, profile reachability, ignored boundaries, common public
path/privacy leaks, and accidental plugin-canon duplication.

It intentionally does not reimplement the Fifth Ledger profile schema validator. Run
the canonical validator from the separate implementation repository when that source is
available. A new tracked-public profile will retain an expected placement failure until
staging is separately authorised.
