# Telic Fields J.2 — External-Review Readiness, Multi-Party Trial, and Release Candidate

Status: executable release candidate  
Version: 0.1.0-rc1  
Conformance claim: `TF-C4` with selected `TF-C5` retirement behavior  
Production claim: none  
External human review claim: not complete

J.2 advances the J.1 hardened scheduling pilot into a reproducible, threshold-approved release candidate and a synthetic authenticated multi-party trial.

The package demonstrates:

```text
authenticated participant projections
→ two independent participant corrections
→ current-context reconstruction
→ failed policy migration
→ policy rollback
→ corrected policy activation
→ external action gating
→ durable queue fault injection
→ exactly-once scheduling effect
→ consequence return
→ selective witness export
→ threshold release approval
→ deterministic release build
→ retirement with open review obligations
```

## What changed from J.1

- Ed25519-authenticated participant, operator, reviewer, and verifier roles;
- replay-resistant role assertions scoped to one session and operation;
- three-party scheduling field with two outcome-changing corrections;
- policy migration testing with explicit rollback;
- durable SQLite delivery queue with duplicate, reordering, and timeout-after-apply faults;
- exactly-once external effect under retry and duplicate delivery;
- two-of-three independent release-custodian approval;
- deterministic ZIP release construction;
- standalone release verifier that imports no implementation package;
- privacy and accessibility review records that accurately preserve the absence of external human sign-off;
- release-candidate manifest that explicitly excludes production and external-review claims.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./scripts/run_tests.sh
./scripts/run_trial.sh
./scripts/verify_independent.sh
./scripts/build_release.py
./scripts/verify_release.sh
```

Run the local interface:

```bash
./scripts/serve_demo.sh
```

Open `http://127.0.0.1:8767`.

## Principal exports

- `exports/tf-mvi-1-j2-witness.zip`
- `exports/telic-fields-j2-rc1.zip`

The witness is independently verifiable. The release candidate requires two valid signatures from three separate release custodians over one exact manifest digest.

## Important boundary

J.2 performs a separate-process verification dry run, not an external organizational review. No independent human security, privacy, accessibility, or governance sign-off is claimed.

The package uses synthetic demonstration records only. It is not approved for clinical, legal, financial, employment, benefits, credit, insurance, election, or other high-stakes adjudication.

## Next transition

Proceed to:

- **J.3 — Observed External Exercise, Governance Handoff, and Pilot Admission**
