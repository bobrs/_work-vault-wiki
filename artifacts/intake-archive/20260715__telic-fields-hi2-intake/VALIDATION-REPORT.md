# HI-2 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

The following ten candidate Draft 2020-12 schemas were checked:

- `field-classification.schema.json`
- `route.schema.json`
- `route-portfolio.schema.json`
- `cost-bearer-record.schema.json`
- `protected-condition-review.schema.json`
- `decision-rule-declaration.schema.json`
- `governance-gate.schema.json`
- `model-recommendation.schema.json`
- `decision-witness.schema.json`
- `consequence-review.schema.json`

Result:

```text
schemas checked: 10
schema errors: 0
```

## Positive demonstrations

All seven required demonstrations passed:

1. two Pareto-efficient routes remained unresolved;
2. a protected condition blocked an otherwise efficient route;
3. missing standing caused pause;
4. a route portfolio preserved legitimate plurality;
5. a DecisionWitness was generated from an event stream;
6. observed consequence caused route revision;
7. model recommendation remained recommendation only.

Result:

```text
positive demonstrations passed: 7
positive failures: 0
```

## Negative conformance cases

All twelve prohibited patterns were detected:

1. hidden scalar sovereignty;
2. protected-condition compensation;
3. missing standing represented as zero;
4. Pareto efficiency represented as legitimacy;
5. model recommendation treated as authorization;
6. route consideration treated as consent;
7. eventless witness;
8. consequence overwrite;
9. no-decision erasure;
10. route-portfolio collapse;
11. undeclared decision rule;
12. omitted cost bearer.

Result:

```text
negative cases detected: 12
undetected negative cases: 0
```

## Event-generated witness

The witness generator read:

- the decision event stream;
- structured witness context;
- referenced route, gate, recommendation, and classification records.

The generated witness validated against `decision-witness.schema.json`.

Result:

```text
generated_from_events: true
event order preserved: true
selected route derived from route_selected event: true
model recommendation retained separately: true
```

## Independent witness export

The decision-witness demonstration export contains:

- event stream;
- generated witness;
- route comparison;
- protected-condition gate;
- missing-standing gate;
- route portfolio;
- model recommendation;
- schemas;
- manifest;
- checksums.

Result:

```text
checksum files verified: 17
checksum failures: 0
independent_of_recommendation_model: true
```

## Public-page consistency review

H.2 was checked against I.2 for the following distinctions:

- field, projection, and receiver mirror remain distinct;
- private access does not create disclosure authority;
- consent is scoped to artifact, recipient, purpose, duration, and downstream use;
- source correction can stop inference laundering before disclosure;
- witness does not require merger or total surveillance;
- model mediation does not create adjudication authority;
- inadequate context may require ask, narrow, pause, escalate, fork, or stop.

Result:

```text
technical/public contradictions found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- fairness of the example decision;
- completeness of cost-bearer discovery;
- legitimacy of protected-condition authority in every domain;
- production security;
- legal compliance;
- model neutrality;
- public-reader comprehension;
- scientific validity of the broader Telic Field framework.

## Conditions before production use

- authenticate standing and protected-condition authority;
- test cost-bearer discovery against real institutional workflows;
- implement decision-rule sensitivity analysis;
- test event-generated witness creation against a production event store;
- implement independent route and gate review;
- conduct privacy and strategic-manipulation threat modeling;
- conduct independent reader testing of H.1 and H.2.
