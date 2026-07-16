# HI-0 Validation Report

Status: completed  
Validation date: 2026-07-15

## JSON Schema checks

The eight candidate JSON Schemas were parsed and checked as Draft 2020-12 schemas:

- `core-envelope.schema.json`
- `center-reference.schema.json`
- `telic-projection.schema.json`
- `semantic-trail-event.schema.json`
- `route-and-gate.schema.json`
- `model-role-authority.schema.json`
- `decision-witness.schema.json`
- `contest-correction-event.schema.json`

Result:

```text
8 valid schemas
0 schema-validation errors
```

## Worked-instance checks

The following example components were validated:

### Example A

- three CenterReference instances;
- three TelicProjection instances;
- selected Route and GovernanceGate bundle.

### Example B

- three CenterReference instances;
- ContestCorrectionEvent.

### Example C

- three CenterReference instances;
- ModelRoleAuthorityEnvelope;
- selected Route and GovernanceGate bundle.

Result:

```text
all selected instances valid
0 instance-validation errors
```

## Scope of validation

This report confirms structural validation only.

It does not establish:

- legal validity;
- moral legitimacy;
- complete provenance;
- domain safety;
- production security;
- interoperability with a deployed W3C PROV system;
- correctness of every human-readable example;
- scientific validity of the Telic Field framework.

## Remaining technical validation

Before I.1:

- add explicit `$defs` for reusable authority and consent types;
- test schema resolution across packaged and remote environments;
- create negative test cases for prohibited collapses;
- test bitemporal correction sequences;
- test protected omission and selective disclosure;
- test event-to-graph materialization;
- evaluate whether the common envelope is too large for P0/P1 use.
