# Telic Field Papers — HI-2 Navigation, Gates, and the Projection Boundary

This package completes I.2 and H.2 as the third controlled H/I pass.

## Technical artifacts

- `I2-NAVIGATION-GATE-AND-DECISION-WITNESS-SPECIFICATION.md`
- `NAVIGATION-GATE-AND-AUTHORITY-MATRIX.md`
- `DECISION-METHOD-ADAPTER-MATRIX.md`
- ten candidate schemas under `schemas/`
- seven positive demonstrations under `examples/`
- twelve negative conformance fixtures under `tests/`
- event-based witness generator;
- independent decision-witness export.

## Public artifact

- `H2-THE-PROJECTION-IS-NOT-THE-PERSON.md`

H.2 develops:

- field, projection, and receiver mirror;
- private and shared channels;
- minimum necessary projection;
- bounded consent;
- inference laundering;
- correction before disclosure;
- witness without merger or total surveillance.

## Demonstration result

```text
2 nondominated routes preserved
1 protected condition blocked an efficient route
1 missing-standing condition caused pause
1 route portfolio preserved parallel paths
1 DecisionWitness generated from events
1 consequence review revised a route
1 model recommendation remained non-authoritative
```

## Validation result

```text
10 schemas checked
0 schema errors
7 positive demonstrations passed
12 prohibited patterns detected
decision-witness export checksums: PASS
```

## Gate result

```text
PASS WITH CONDITIONS
```

The principal remaining limitations are:

- protected-condition authentication;
- standing materiality;
- route-generation framing;
- delay burden;
- model influence without formal authority;
- independent public-reader testing.

## Next transition

Proceed to HI-3:

- I.3 — Context Capacity, Stop, and Escalation Specification;
- H.3 — When the System Should Stop.
