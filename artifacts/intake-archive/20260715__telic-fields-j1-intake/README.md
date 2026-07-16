# Telic Fields J.1 — Independent Verification, Selective Disclosure, and Pilot Hardening

Status: executable reference implementation  
Version: 0.1  
Conformance claim: `TF-C4` with bounded `TF-C5` retirement behavior  
Production claim: none

J.1 hardens the J.0 scheduling pilot without widening its domain claim.

The package demonstrates:

```text
source
→ projection
→ standing
→ versioned policy and authority
→ current context
→ non-sovereign model route
→ external signed gate token
→ transactional tool attempt
→ compensation or action
→ consequence
→ participant correction
→ selective witness export
→ independent verification
→ retirement
```

## Principal changes from J.0

- Ed25519-signed witness manifest;
- standalone verifier that imports no `telic_j1` code;
- versioned immutable authorization policy;
- HMAC action-key rotation and revocation;
- stale-context rejection by canonical context fingerprint;
- serialized concurrent event appends;
- optimistic object-revision checks;
- correction-descendant reachability reporting;
- public, participant, operator, and verifier witness views;
- record commitments for omitted data;
- runtime privacy enforcement;
- partial tool-failure compensation;
- accessible no-JavaScript web interface;
- sixteen-case adversarial harness.

## Quick start

```bash
python -m venv .venv
. .venv/bin/activate
pip install -r requirements.txt
./scripts/run_tests.sh
./scripts/run_demo.sh
./scripts/verify_independent.sh
```

Run the local interface:

```bash
./scripts/serve_demo.sh
```

Open `http://127.0.0.1:8766`.

## Independent witness

The package includes:

- `exports/tf-mvi-1-j1-witness.zip`

Verify it without importing the implementation package:

```bash
PYTHONPATH= python verifier/verify_witness.py exports/tf-mvi-1-j1-witness.zip
```

The verifier checks:

- ZIP path safety;
- SHA-256 checksums;
- Ed25519 manifest signature;
- twelve JSON Schemas;
- object commitments;
- hash-chained events;
- four selective-disclosure views;
- ten required runtime proofs.

## Demonstrated result

```text
stale pre-correction route: DENIED
morning inaccessible route: DENIED
partial scheduling attempt: COMPENSATED
old gate key after revocation: REJECTED
fresh evening route: COMMITTED
participant consequence: RETURNED
correction descendants: COMPLETE FOR SCOPE
retirement: TOOL AUTHORITY REVOKED
public witness: PRIVATE SOURCE OMITTED WITH COMMITMENTS
independent signature verification: PASS
```

## Important boundary

The implementation contains only synthetic demonstration records.

It is not approved for clinical, legal, financial, employment, benefits, credit, insurance, election, or other high-stakes adjudication.

## Next transition

Proceed to:

- **J.2 — External Review, Multi-Party Trial, and Release Candidate**
