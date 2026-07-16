# J.0 Runbook

## Requirements

- Python 3.11 or newer
- `jsonschema`

Install:

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run the deterministic demonstration

```bash
./scripts/run_demo.sh
```

Outputs:

```text
demo/run/pilot.sqlite3
exports/tf-mvi-1-witness.zip
```

## Verify the witness independently

```bash
PYTHONPATH=src python3 -m telic_j0.cli verify exports/tf-mvi-1-witness.zip
```

Expected result:

```text
valid: true
failed_gate: true
valid_action: true
consequence_return: true
correction_propagation: true
retirement_revocation: true
```

## Run all tests

```bash
./scripts/run_tests.sh
```

This executes:

- event identity and hash-chain tests;
- reference-scenario integration tests;
- participant-correction propagation tests;
- external-gate tests;
- local web-interface smoke tests;
- ten cross-branch threat cases;
- independent witness verification.

## Run the local web interface

```bash
./scripts/serve_demo.sh
```

Open `http://127.0.0.1:8765`.

The page exposes stepwise controls for:

- field seeding;
- model summary;
- participant correction;
- route generation and gating;
- authorized execution;
- consequence observation;
- retirement.

Read-only JSON endpoints:

```text
/api/status
/api/events
/api/objects
/api/witness
```

## Reset a demonstration

Remove the selected work directory:

```bash
rm -rf demo/run
```

Then rerun the demo.

## Inspect the local state

```bash
PYTHONPATH=src python3 -m telic_j0.cli inspect --workdir demo/run
```

## Safety boundary

Do not connect this reference package to production calendars, clinical systems, employment scheduling, benefits systems, financial accounts, or public decision infrastructure.
