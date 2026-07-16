# Telic Field Papers — HI-1 Provenance and Public Primer

This package completes I.1 and H.1 as the second controlled H/I pass.

## Technical artifacts

- `I1-PROVENANCE-EVENT-AND-CORRECTION-SPECIFICATION.md`
- `I1-TELIC-FIELD-PROV-PROFILE.md`
- `CORRECTION-AND-PROPAGATION-MATRIX.md`
- eight candidate schemas under `schemas/`
- five positive demonstrations under `examples/`
- ten negative conformance fixtures under `tests/`
- `tests/run_hi1_validation.py`
- `tests/validation-results.json`

## Public artifact

- `H1-WHAT-MATTERS-BEFORE-THE-SYSTEM-ACTS.md`

H.1 is the first public primer.

It introduces the framework through six questions:

```text
What matters?
What was shared?
What was inferred?
Who may act?
Who bears the consequence?
How can it be corrected or ended?
```

## Independent export

The package includes:

- `exports/participant-export-demo/`

The export contains records, events, a witness, a selective-disclosure view, schemas, a manifest, and checksums. It excludes the protected source content while preserving proof that omission occurred.

## Validation result

```text
8 schemas checked
0 schema errors
5 positive demonstrations passed
10 negative cases detected
participant export manifest: PASS
participant export checksums: PASS
```

## Gate result

```text
PASS WITH CONDITIONS
```

The principal remaining limitations are:

- descendant discovery completeness;
- authenticated correction authority;
- cryptographically stronger protected omission;
- external-system correction enforcement;
- portable namespace governance;
- independent public-reader testing.

## Next transition

Proceed to HI-2:

- I.2 — Navigation, Gate, and Decision-Witness Specification;
- H.2 — The Projection Is Not the Person.
