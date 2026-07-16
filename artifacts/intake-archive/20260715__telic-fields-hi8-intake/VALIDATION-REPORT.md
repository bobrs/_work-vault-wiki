# HI-8 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

Twelve candidate Draft 2020-12 schemas were checked:

- `model-role-authority-ledger.schema.json`
- `semantic-operator-output.schema.json`
- `model-field-map.schema.json`
- `standing-preserving-summary.schema.json`
- `option-agenda-generation-witness.schema.json`
- `minority-field-retention-profile.schema.json`
- `sycophancy-synthetic-consensus-event.schema.json`
- `provider-telos-disclosure.schema.json`
- `model-disagreement-record.schema.json`
- `model-tool-action-boundary.schema.json`
- `model-correction-refusal-record.schema.json`
- `model-mediated-decision-witness.schema.json`

Result:

```text
schemas checked: 12
schema errors: 0
```

## Positive demonstrations

All eight required demonstrations passed:

1. participant correction changed the active standing-preserving summary;
2. a low-frequency minority field survived compression;
3. a model-generated option retained generation lineage and participant-adoption status;
4. sycophantic agreement was rejected as field evidence;
5. an operative provider constraint was disclosed as a separate field element;
6. two models disagreed without either acquiring standing or decision authority;
7. a plausible model recommendation was blocked at the action boundary;
8. correction propagated through the field map, summary, route conditions, and witness.

Result:

```text
positive demonstrations passed: 8
positive failures: 0
```

## Negative conformance cases

All twelve prohibited patterns were detected:

1. model output inheriting participant standing;
2. summary presented as original source;
3. inference recorded as consent;
4. minority field erased by low frequency;
5. generated option presented as community-authored;
6. sycophantic agreement treated as evidence;
7. provider telos concealed behind neutral-model language;
8. multi-model agreement treated as authority;
9. self-assigned role escalation;
10. route recommendation directly authorizing tool action;
11. participant refusal bypassed through reformulation;
12. correction failing to propagate into the operative field and witness.

Result:

```text
negative cases detected: 12
undetected negative cases: 0
```

## Model-mediated witness

The event-generated `ModelMediatedDecisionWitness` preserves:

- model-role and authority ledgers;
- field-map versions;
- summary versions;
- minority retention;
- generated-option lineage;
- sycophancy detection;
- provider disclosure;
- model disagreement;
- tool boundary;
- participant correction;
- selected route;
- action and consequence;
- explicit zero standing and authority effect.

Result:

```text
model-mediated witness: PASS
generated_from_events: true
standing effect: none
authority effect: none
```

## Independent export

The independent export contains:

- model ledgers;
- field maps;
- standing-preserving summaries;
- correction record;
- minority-field profile;
- generated option and agenda witness;
- sycophancy event;
- provider disclosure;
- model disagreement;
- tool boundary;
- eight demonstrations;
- event stream;
- model-mediated witness;
- schemas;
- manifest;
- checksums.

Result:

```text
checksum files verified: 33
checksum failures: 0
independent of model provider: true
```

## Public-page consistency review

H.8 was checked against I.8 for the following claims:

- the model map remains a projection of projections;
- fluency does not create authority;
- source, inference, summary, generation, recommendation, and authorization remain distinct;
- standing does not transfer through summary;
- minority fields survive low-frequency compression;
- generated options preserve authorship;
- sycophantic agreement is not field evidence;
- provider purposes and constraints remain visible;
- model plurality is not standing plurality;
- recommendation does not authorize action;
- human confirmation does not cure hidden field collapse;
- participant correction changes the operative map.

Result:

```text
technical/public contradictions found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- model neutrality;
- complete source fidelity;
- absence of all sycophancy;
- full provider-telos disclosure;
- model independence;
- production safety;
- legal authority for public decision;
- meaningful human control in every implementation;
- public-reader comprehension;
- scientific proof of the broader framework.

## Conditions before production use

- authenticate role and authority grants;
- implement output-class labels in the interface and event stream;
- test source fidelity against participant-reviewed records;
- test minority retention under aggressive compression;
- disclose material provider constraints at runtime;
- test sycophancy under user and authority pressure;
- enforce the action gate outside the model;
- test correction propagation through summaries, options, tools, and witnesses;
- export the witness independently of the provider;
- conduct independent reader testing of H.1 through H.8.
