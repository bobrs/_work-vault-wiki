# HI-1 Validation Report

Status: completed  
Validation date: 2026-07-15

## Schema validation

The following eight candidate Draft 2020-12 schemas were checked:

- `portable-identifier.schema.json`
- `correction-record.schema.json`
- `correction-propagation-record.schema.json`
- `authority-record.schema.json`
- `protected-omission-proof.schema.json`
- `selective-witness-view.schema.json`
- `participant-export-manifest.schema.json`
- `derived-assertion.schema.json`

Result:

```text
schemas checked: 8
schema errors: 0
```

## Positive demonstrations

All five required demonstrations passed:

1. full correction propagation;
2. partial propagation with explicit external gap;
3. expired authority rejected for a new action;
4. protected omission without source disclosure;
5. inference status preserved through repeated reuse.

Result:

```text
positive demonstrations passed: 5
positive failures: 0
```

## Negative conformance cases

All ten prohibited patterns were detected:

1. inference laundering;
2. expired-authority reuse;
3. silent history rewrite;
4. false propagation completeness;
5. protected-omission collapse;
6. omission represented as absence;
7. provenance represented as truth;
8. model-only witness custody;
9. contest without responsible authority;
10. correction without descendant review.

Result:

```text
negative cases detected: 10
undetected negative cases: 0
```

## Independent export

The demonstration participant export passed schema validation.

Its checksums were independently recalculated.

Result:

```text
manifest validation: PASS
checksum files verified: 13
checksum failures: 0
independent_of_originating_model: true
protected source content included: false
protected omission marked: true
```

## Public-primer consistency review

H.1 was checked against I.1 for the following claims:

- correction does not silently rewrite history;
- protected omission is represented rather than treated as absence;
- provenance is not truth or legitimacy;
- source and inference remain separate;
- expired authority remains visible and ineligible;
- correction may remain incomplete in external systems;
- model role does not create action authority;
- witness does not require total surveillance.

Result:

```text
technical/public contradiction found: 0
```

## Scope of validation

This report establishes structural and internal semantic validation only.

It does not establish:

- production security;
- cryptographic proof;
- legal compliance;
- clinical safety;
- scientific validity;
- completeness of descendant discovery;
- interoperability with an external PROV implementation;
- public-reader comprehension outside the project team.

## Conditions before production use

- replace provisional identifier and namespace choices;
- define authenticated correction authority;
- implement secure selective disclosure;
- test descendant discovery against real graph stores;
- test external correction notification;
- conduct privacy threat modeling;
- conduct independent reader testing of H.1;
- perform legal and domain review where consequential actions are involved.
