# J.2 Runbook

## Environment

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
```

## Run tests

```bash
./scripts/run_tests.sh
```

## Run the multi-party trial

```bash
./scripts/run_trial.sh
```

## Verify the witness independently

```bash
./scripts/verify_independent.sh
```

## Build the release candidate twice

```bash
python scripts/build_release.py
```

## Verify the release independently

```bash
./scripts/verify_release.sh
```

## Inspect trial state

```bash
PYTHONPATH=src python -m telic_j2 inspect
```

## Serve the local interface

```bash
./scripts/serve_demo.sh
```

## Reset

Remove `demo/release-candidate-trial/` and rerun the trial. Do not distribute the private run directory. It contains local demonstration keys.
