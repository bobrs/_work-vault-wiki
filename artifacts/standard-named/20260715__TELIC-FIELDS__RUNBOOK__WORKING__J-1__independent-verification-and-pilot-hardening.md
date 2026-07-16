# J.1 Runbook

## Requirements

- Python 3.11 or later;
- `jsonschema`;
- `cryptography`.

## Set up

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run all tests

```bash
./scripts/run_tests.sh
```

## Run the deterministic demo

```bash
./scripts/run_demo.sh
```

The script writes:

- `demo/run/pilot.sqlite3`;
- `exports/tf-mvi-1-j1-witness.zip`.

The local private witness-signing key and gate-keyring state remain in the ignored local work directory with owner-only permissions. They are not included in the witness export or distributable package.

## Verify with the implementation verifier

```bash
PYTHONPATH=src python -m telic_j1 verify exports/tf-mvi-1-j1-witness.zip
```

## Verify independently

```bash
./scripts/verify_independent.sh
```

The standalone verifier does not import `telic_j1`.

## Run adversarial tests

```bash
PYTHONPATH=src python -m telic_j1 threats --workdir demo/threats
```

## Run the local interface

```bash
./scripts/serve_demo.sh
```

Open:

```text
http://127.0.0.1:8766
```

## Inspect the database

```bash
PYTHONPATH=src python -m telic_j1 inspect --workdir demo/run
```

## Expected final status

```text
step: retired
active policy version: 2
gate-k2: revoked
gate-k3: active
tool credential active: false
correction reachability: complete for scope
```

## Do not deploy

This is a research and reference package.

Do not connect it to production schedules, accounts, identities, payments, clinical systems, employment systems, or public decision systems.
