# Telic Field Papers — HI-3 Context Capacity and Legitimate Stop

This package completes I.3 and H.3 as the fourth controlled H/I pass.

## Technical artifacts

- `I3-CONTEXT-CAPACITY-STOP-AND-ESCALATION-SPECIFICATION.md`
- `CONTEXT-CAPACITY-AND-AUTHORITY-DEGRADATION-MATRIX.md`
- `STOP-ESCALATION-AND-RECOVERY-MATRIX.md`
- `MINIMUM-CONTEXT-BY-ACTION-MATRIX.md`
- ten candidate schemas under `schemas/`
- eight positive demonstrations under `examples/`
- twelve negative conformance fixtures under `tests/`
- independent context-capacity export.

## Public artifact

- `H3-WHEN-THE-SYSTEM-SHOULD-STOP.md`

H.3 develops:

- context capacity versus storage capacity;
- missing standing versus missing data;
- contradiction and uncertainty;
- privacy as capacity;
- participant load;
- authority degradation;
- stop and delay cost;
- competent escalation;
- capacity debt;
- recovery.

## Demonstration result

```text
large context with missing standing: PAUSE
small context for reversible draft: CONTINUE WITH CONDITIONS
protected omission: CAPACITY IMPROVED
overload: EXECUTE → RECOMMEND
missing correction: STOP
participant overload: STAGE
competent outer loop: ESCALATE
context recovery: RECOMMENDATION AUTHORITY RESTORED
```

## Validation result

```text
10 schemas checked
0 schema errors
8 positive demonstrations passed
12 prohibited patterns detected
context-capacity export checksums: PASS
technical/public contradictions found: 0
```

## Gate result

```text
PASS WITH CONDITIONS
```

The principal remaining limitations are:

- domain-specific materiality;
- authenticated capacity evidence;
- tool-level authority enforcement;
- privacy-preserving escalation;
- delay harm;
- strategic overload;
- participant-load privacy;
- independent public-reader testing.

## Next transition

Proceed to HI-4:

- I.4 — Temporal Standing, Commitment, and Succession Specification;
- H.4 — The Present Is Not the Whole Timeline.
