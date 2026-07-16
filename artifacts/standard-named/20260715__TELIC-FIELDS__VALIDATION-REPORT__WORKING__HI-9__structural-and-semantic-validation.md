# HI-9 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

Twelve candidate Draft 2020-12 schemas were checked:

- `source-dataset-standing-record.schema.json`
- `collection-authorization-record.schema.json`
- `license-authority-consent-profile.schema.json`
- `training-transformation-lineage.schema.json`
- `annotation-preference-data-record.schema.json`
- `model-constitution-lineage.schema.json`
- `preference-optimization-record.schema.json`
- `synthetic-data-ancestry-record.schema.json`
- `withdrawal-unlearning-record.schema.json`
- `derivative-correction-propagation.schema.json`
- `benefit-contributor-recognition-record.schema.json`
- `consentful-training-witness.schema.json`

Result:

```text
schemas checked: 12
schema errors: 0
```

## Positive demonstrations

All eight required demonstrations passed:

1. a publicly accessible source remained blocked without training authority;
2. research-training permission did not become commercial-deployment permission;
3. preference data retained task, labor, disagreement, and downstream provenance;
4. provider principles and community-adopted rules remained distinct;
5. synthetic data retained model and ancestor-source lineage;
6. withdrawal stopped future use and performed bounded unlearning without claiming perfect removal;
7. correction and restriction propagated into known derivative models and runtime policy;
8. a community benefit claim remained concrete, governed, and connected to contribution.

Result:

```text
positive demonstrations passed: 8
positive failures: 0
```

## Negative conformance cases

All twelve prohibited patterns were detected:

1. public availability represented as consent;
2. license represented as consent;
3. one collection grant represented as authority for every transition;
4. an individual represented as able to authorize community-held knowledge;
5. a bounded annotation task represented as universal human preference;
6. provider principles represented as a legitimate public constitution without adoption lineage;
7. synthetic data represented as source-free;
8. source deletion represented as proof of model forgetting;
9. approximate unlearning represented as complete removal;
10. derivative models losing known source obligations;
11. contributor payment represented as unlimited future consent;
12. consentful runtime use represented as retroactive purification of training.

Result:

```text
negative cases detected: 12
undetected negative cases: 0
```

## ConsentfulTrainingWitness

The event-generated witness preserves:

- source and dataset standing;
- collection authority;
- transition-specific authority, consent, and license scope;
- transformation lineage;
- annotation and preference provenance;
- constitution authority;
- preference optimization;
- synthetic ancestry;
- withdrawal and unlearning residuals;
- derivative correction propagation;
- concrete benefit mechanisms;
- known unknowns and unreachable descendants.

Result:

```text
consentful-training witness: PASS
generated_from_events: true
lineage classification: MIXED AUTHORITY
binary purity claim: false
```

## Independent training-lineage export

The export contains:

- source-standing records;
- collection authorizations;
- transition-authority profile;
- transformation lineage;
- annotation and preference record;
- model constitution;
- optimization record;
- synthetic ancestry;
- withdrawal and unlearning record;
- derivative propagation;
- benefit record;
- eight demonstrations;
- event stream;
- ConsentfulTrainingWitness;
- schemas;
- manifest;
- checksums.

Result:

```text
checksum files verified: 33
checksum failures: 0
independent of training provider: true
```

## Public-page consistency review

H.9 was checked against I.9 for the following claims:

- training is a recruitment relation;
- public availability is not consent;
- access, permission, consent, ownership, and legitimacy remain distinct;
- authority is transition-specific;
- source standing may be collective;
- transformation does not erase lineage;
- annotation and preference data remain conditional;
- constitution explicitness does not create authority;
- synthetic data retains ancestry;
- withdrawal and unlearning remain distinct;
- derivative models inherit obligations;
- benefit sharing requires a concrete mechanism;
- consentful training is a qualified lineage profile rather than a purity badge;
- training and deployment legitimacy remain separate.

Result:

```text
technical/public contradictions found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- legal conclusions about any actual training corpus;
- complete provenance;
- universal individual-consent requirements;
- exact machine unlearning;
- discovery of every derivative model;
- one universal community authority;
- sufficient compensation or benefit in every domain;
- production security;
- public-reader comprehension;
- scientific proof of the broader framework.

## Conditions before production use

- authenticate source-standing and authority records;
- implement transition-specific restriction enforcement;
- test dataset-mixing and provenance retention;
- preserve annotator disagreement in real preference pipelines;
- audit constitution authority and revisions;
- verify synthetic ancestry to a declared depth;
- test withdrawal and unlearning claims against declared evidence;
- audit known derivatives and successor obligations;
- review community benefit mechanisms independently;
- conduct independent reader testing of H.1 through H.9.
