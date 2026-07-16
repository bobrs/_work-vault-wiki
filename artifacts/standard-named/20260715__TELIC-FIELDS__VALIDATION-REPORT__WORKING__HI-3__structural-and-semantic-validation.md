# HI-3 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

Ten candidate Draft 2020-12 schemas were checked:

- `context-demand-profile.schema.json`
- `context-capacity-profile.schema.json`
- `standing-coverage-assessment.schema.json`
- `participant-load-record.schema.json`
- `overload-event.schema.json`
- `capacity-debt-record.schema.json`
- `authority-degradation-record.schema.json`
- `stop-escalation-decision.schema.json`
- `escalation-record.schema.json`
- `context-reconstitution-record.schema.json`

Result:

```text
schemas checked: 10
schema errors: 0
```

## Positive demonstrations

All eight required demonstrations passed:

1. token-rich context remained standing-poor;
2. small context supported a narrow reversible action;
3. protected omission improved privacy and participant-load capacity;
4. overload degraded authority from execute to recommend;
5. missing correction caused stop;
6. participant overload caused staged disclosure;
7. escalation reached a competent outer loop;
8. context reconstitution restored recommendation authority while preserving remaining debt.

Result:

```text
positive demonstrations passed: 8
positive failures: 0
```

## Negative conformance cases

All twelve prohibited patterns were detected:

1. token-count sufficiency;
2. fluent authority persistence;
3. privacy treated as deficit;
4. participant-burden blindness;
5. missing correction ignored;
6. composite-score concealment;
7. hierarchy-only escalation;
8. no-decision without a cost bearer;
9. capacity-debt erasure;
10. authority restoration without reconstitution;
11. small-context rejection;
12. overload without tool-level degradation.

Result:

```text
negative cases detected: 12
undetected negative cases: 0
```

## Independent context-capacity export

The demonstration export contains:

- demand and capacity profiles;
- standing and privacy demonstrations;
- authority degradation;
- stop decision;
- competent escalation;
- recovery and capacity debt;
- event stream;
- schemas;
- manifest;
- checksums.

Result:

```text
checksum files verified: 18
checksum failures: 0
independent_of_capacity_model: true
```

## Public-page consistency review

H.3 was checked against I.3 for the following claims:

- context capacity is not storage or token capacity;
- missing standing differs from missing data;
- contradiction may remain unresolved;
- privacy can increase capacity;
- participant load is a system property;
- authority should degrade as context fails;
- stop and pause have cost bearers;
- escalation must be competence-matched;
- capacity debt survives successful output;
- recovery restores only supported authority.

Result:

```text
technical/public contradictions found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- clinical assessment of human capacity;
- universal materiality thresholds;
- legal authority for escalation;
- completeness of standing discovery;
- production security;
- cryptographic enforcement;
- public-reader comprehension;
- scientific validity of a universal context-capacity model.

## Conditions before production use

- define domain-specific materiality thresholds;
- authenticate standing and correction records;
- enforce authority degradation at the credential and tool layers;
- test participant-load estimates with real users;
- test privacy-preserving escalation;
- implement escalation return and closure events;
- test capacity-debt aging and succession;
- conduct independent reader testing of H.1 through H.3.
