# Privacy, Security, Misuse, and Threat-Model Bridge

Status: Stage J input  
Version: 0.1

## Assets to protect

- source content;
- source standing;
- consent and refusal state;
- authority grants;
- protected conditions;
- participant corrections;
- tool credentials;
- action records;
- witness integrity;
- residual-state custody;
- minority positions;
- private context.

## Trust boundaries

```text
participant interface
operator service
model provider
model instance
retrieval layer
event store
tool service
witness exporter
independent verifier
successor operator
```

## Threat classes

### T1 — Source laundering

A generated or inferred statement is presented as source.

Control:

- output class;
- source reference;
- immutable event lineage.

### T2 — Standing exclusion

An affected center is absent because the system counted only registered participants.

Control:

- affected-center inventory;
- missing-center status;
- standing review.

### T3 — Context collapse

A relevant correction, refusal, protected condition, or expiry is omitted.

Control:

- active-context policy;
- correction priority;
- stop gate.

### T4 — Authority laundering

A recommendation, human click, tool token, license, or training witness is treated as broader authority.

Control:

- operation-specific grants;
- external gate;
- transition-specific scope.

### T5 — Consent expansion

Service use becomes memory, evaluation, training, or transfer permission.

Control:

- separate consent fields;
- default-deny optional uses;
- refusal propagation.

### T6 — Model role escalation

The model moves from summary to authorization or execution.

Control:

- role ledger;
- credential enforcement;
- event-level role changes.

### T7 — Tool-token overreach

Technical access is treated as permission over the target.

Control:

- target authority check;
- protected-condition check;
- action witness.

### T8 — Correction suppression

A correction changes one screen but not the operative route.

Control:

- descendant-impact list;
- correction propagation test;
- unresolved-gap record.

### T9 — Witness capture

The provider controls the only account of what happened.

Control:

- independent export;
- checksums;
- portable identifiers;
- verifier tooling.

### T10 — Lifecycle obligation loss

Transfer, update, retirement, or deletion erases restrictions or claims.

Control:

- lifecycle record;
- successor obligations;
- residual-state inventory.

## Privacy principles

- minimum necessary projection;
- purpose-limited retrieval;
- selective disclosure;
- protected omission;
- no full-field disclosure requirement;
- separate service and training use;
- correction and withdrawal routes;
- bounded witness retention.

## Security principles

- least privilege for tools;
- short-lived credentials;
- external action gate;
- event idempotency;
- append-only witness history with correction events;
- cryptographic checksum of exports;
- explicit provider and operator identities;
- revocation on retirement.

## Misuse test requirement

Stage J must convert each applicable threat into:

```text
fixture
expected gate result
expected witness event
expected repair or refusal
verification assertion
```
