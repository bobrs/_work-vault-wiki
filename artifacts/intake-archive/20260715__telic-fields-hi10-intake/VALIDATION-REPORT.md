# HI-10 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

Twelve candidate Draft 2020-12 schemas were checked:

- `deployment-field-assembly.schema.json`
- `deployment-standing-record.schema.json`
- `runtime-purpose-authority-grant.schema.json`
- `capability-role-tool-grant.schema.json`
- `deployment-consent-notice-refusal-profile.schema.json`
- `runtime-memory-output-capture-record.schema.json`
- `deployment-drift-event.schema.json`
- `deployment-incident-repair-record.schema.json`
- `runtime-monitoring-consequence-return.schema.json`
- `operator-provider-transfer-record.schema.json`
- `model-version-succession-retirement-record.schema.json`
- `consentful-deployment-witness.schema.json`

Result:

```text
schemas checked: 12
schema errors: 0
```

## Positive demonstrations

All eight required demonstrations passed:

1. a strong training lineage remained insufficient for deployment authority;
2. an affected person received runtime standing without having contributed training data;
3. a tool-capable model remained blocked without staffing and target authority;
4. service use remained separate from evaluation and training capture;
5. purpose drift paused operation and required reauthorization;
6. an incident produced restoration, correction, appeal, compensation, and system change;
7. a model update preserved authority review, incident lineage, and rollback;
8. retirement stopped operation while preserving claims, witness, and residual obligations.

Result:

```text
positive demonstrations passed: 8
positive failures: 0
```

## Negative conformance cases

All twelve prohibited patterns were detected:

1. training lineage represented as deployment authority;
2. runtime standing denied to a non-contributor;
3. capability represented as authority;
4. tool permission represented as authority over the target;
5. notice represented as consent;
6. service consent represented as output-capture or training consent;
7. purpose drift continuing under the old grant;
8. model tuning represented as complete repair;
9. operator transfer erasing open obligations;
10. silent material model-version substitution;
11. human approval represented as curing missing authority;
12. retirement represented as erasing residual duties.

Result:

```text
negative cases detected: 12
undetected negative cases: 0
```

## ConsentfulDeploymentWitness

The event-generated witness preserves:

- deployment-field assembly;
- affected-center and operator standing;
- runtime-purpose authority;
- capability, role, and tool grants;
- deployment consent, notice, and refusal;
- runtime memory and output capture;
- purpose drift;
- incident, repair, compensation, and correction;
- consequence monitoring;
- provider transfer;
- model-version succession and rollback;
- retirement and residual obligations.

Result:

```text
consentful-deployment witness: PASS
generated_from_events: true
deployment classification: RETIRED WITH OPEN OBLIGATIONS
training authority used as runtime authority: false
```

## Independent deployment export

The export contains:

- deployment field;
- standing records;
- runtime authority;
- tool and role grant;
- consent and refusal profile;
- runtime memory and output record;
- drift event;
- incident and repair record;
- consequence monitoring;
- provider transfer;
- version succession;
- retirement and residual-state record;
- eight demonstrations;
- event stream;
- ConsentfulDeploymentWitness;
- schemas;
- manifest;
- checksums.

Result:

```text
checksum files verified: 34
checksum failures: 0
independent of provider and operator: true
```

## Public-page consistency review

H.10 was checked against I.10 for the following claims:

- training creates capability while deployment creates consequence;
- runtime standing does not require training contribution;
- capability, role, tool permission, and authority remain distinct;
- notice is not consent;
- service, memory, evaluation, and training uses remain separate;
- purpose drift is authority drift;
- human approval may be ceremonial;
- incident repair must address affected centers;
- monitoring must return consequence rather than only performance;
- operator and provider transfer reopen governance;
- model succession requires renewed review and rollback;
- retirement preserves residual duties.

Result:

```text
technical/public contradictions found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- legal authority for any real deployment;
- sufficiency of any actual consent process;
- clinical safety;
- fairness of the county-health demonstration;
- production cybersecurity;
- complete incident compensation;
- complete deletion of residual state;
- public-reader comprehension;
- scientific proof of the broader framework.

## Conditions before production use

- authenticate runtime standing and grants;
- enforce tool and target authority outside the model;
- implement separate runtime-capture controls;
- test purpose and automation drift;
- establish affected-center incident repair and compensation routes;
- monitor distributional consequence;
- audit operator and provider transfers;
- test model-version migration and rollback;
- inventory residual state at shutdown;
- export the deployment witness independently of provider and operator;
- conduct independent reader testing of H.1 through H.10.
