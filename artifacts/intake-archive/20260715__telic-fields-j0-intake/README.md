# Telic Fields J.0 — Reference Implementation and Pilot Harness

This package is the first executable Stage J artifact.

It implements the bounded reference profile:

```text
TF-MVI-1 — Bounded Model-Assisted Scheduling

conformance target:
  TF-C4

bounded extension:
  TF-C5 retirement
```

The implementation is local-first and inspectable. It uses:

- Python 3.11 or newer;
- SQLite for the append-only event and object store;
- the six HI-S consolidated JSON Schema families;
- a deterministic model adapter;
- an external HMAC-backed action gate;
- a deterministic scheduling-tool simulator;
- participant correction and runtime-data refusal controls;
- consequence return;
- retirement and residual-state accounting;
- a checksummed provider-independent witness export;
- an independent verifier;
- an adversarial threat harness;
- a minimal local web interface.

## What the demonstration proves

```text
one invalid route blocked
one valid route executed
one consequence observed
one participant correction propagated
one retirement event revoked authority
one independent verifier reconstructed the chain
```

## Quick start

```bash
python3 -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt

./scripts/run_demo.sh
./scripts/run_tests.sh
```

Run the local web interface:

```bash
./scripts/serve_demo.sh
```

Then open:

```text
http://127.0.0.1:8765
```

## Command-line interface

```bash
PYTHONPATH=src python3 -m telic_j0.cli demo
PYTHONPATH=src python3 -m telic_j0.cli threats
PYTHONPATH=src python3 -m telic_j0.cli verify exports/tf-mvi-1-witness.zip
PYTHONPATH=src python3 -m telic_j0.cli serve
```

## Principal artifacts

- `src/telic_j0/` — implementation;
- `schemas/` — six consolidated schema families;
- `tests/` — unit, integration, web, event-chain, and adversarial tests;
- `demo/` — generated reference run and validation output;
- `exports/tf-mvi-1-witness.zip` — provider-independent witness;
- `ARCHITECTURE.md` — component and trust-boundary design;
- `SECURITY-AND-THREAT-MODEL.md` — threat controls;
- `CONFORMANCE-CLAIM.md` — bounded TF-C4 claim;
- `VALIDATION-REPORT.md` — executed validation evidence;
- `J0-GATE-REVIEW.md` — J.0 completion decision.

## Explicit non-claims

This package does not establish:

- production security;
- legal or regulatory compliance;
- clinical, financial, legal, employment, or public-adjudication suitability;
- general model safety;
- universal Telic Field conformance;
- certification status;
- repository ingestion or deployment.

The reference implementation uses no production personal data.
