# Release-Candidate Reproducibility

## Method

The builder stages a declared source snapshot, creates a canonical manifest, obtains two-of-three release approvals, and writes the ZIP in sorted path order with fixed timestamps and normalized file modes.

Two clean staging directories are built during validation.

The build passes only when both archives have the same SHA-256 digest.

## Included material

- implementation source;
- consolidated and hardening schemas;
- standalone witness and release verifiers;
- scripts and synthetic example input;
- core architecture and review documentation;
- independently signed J.2 witness.

## Excluded material

- identity private keys;
- gate signing secrets;
- witness private key;
- release-custodian private keys;
- SQLite run databases;
- local queue database;
- production or real participant data.

## Reproducibility boundary

The test proves deterministic packaging from the same source and evidence snapshot. It does not yet prove bit-for-bit reproduction across different operating systems, Python distributions, compression libraries, or dependency-resolved build environments.
