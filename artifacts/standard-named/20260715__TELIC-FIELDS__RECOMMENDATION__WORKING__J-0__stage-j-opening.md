# Stage J Opening Recommendation

Status: approved candidate transition  
Version: 0.1

# J.0 — Reference Implementation and Pilot Harness

## Objective

Build the smallest inspectable system that demonstrates the Telic Field constitutional chain end to end.

## Required components

### 1. Event store

Must support:

- portable event identifiers;
- valid and recorded time;
- append-only history;
- correction and supersession;
- idempotent replay;
- export.

### 2. Six common schema families

- Center and Standing
- Source, Projection, and Context
- Purpose, Authority, Consent, and Role
- Route, Gate, Action, and Consequence
- Event, Witness, Contest, and Repair
- Lifecycle, Transfer, and Residual State

### 3. Participant interface

Must support:

- scoped projection;
- consent and refusal choices;
- correction;
- review of model summary;
- witness export.

### 4. Model adapter

Must preserve:

- assigned role;
- output class;
- source references;
- uncertainty;
- generated-option authorship;
- zero standing and authority effect.

### 5. External action gate

Must enforce:

- operation scope;
- authority;
- consent or other basis;
- protected conditions;
- tool permission;
- target authority;
- context adequacy.

The gate must not rely on the language model's self-report.

### 6. Scheduling tool simulator

Must support:

- read availability;
- prepare candidate;
- reject unauthorized commit;
- execute authorized commit;
- return witnessed result;
- revoke credentials.

### 7. Consequence and correction harness

Must demonstrate:

- observed burden or access result;
- participant correction;
- propagation into active context and next route;
- repair or route revision.

### 8. Retirement harness

Must demonstrate:

- runtime grant expiry;
- credential revocation;
- optional-memory deletion;
- bounded archival witness;
- open-obligation accounting.

### 9. Independent verifier

Must validate:

- checksums;
- schema conformance;
- event chain;
- gate result;
- correction propagation;
- retirement state.

### 10. Adversarial suite

Must include all TF-MVI-1 negative tests and relevant threat fixtures.

## Recommended implementation boundary

```text
local-first
single bounded scenario
simulated scheduling tool
one model provider adapter
provider-independent event and witness store
no production personal data
```

## Stage J success criterion

J.0 succeeds when an independent verifier can prove:

```text
the source remained attributable
the affected centers retained standing
the authority was scoped
the model remained non-sovereign
the tool gate blocked one invalid action
one valid action occurred
the consequence returned
the correction changed the operative system
retirement ended authority
the witness remained portable
```

## Explicitly deferred

- production deployment;
- formal standards submission;
- certification program;
- legal or clinical claims;
- automated public adjudication;
- broad plugin ecosystem;
- universal telic ontology.

## Recommended next package

```text
J0-REFERENCE-IMPLEMENTATION-AND-PILOT-HARNESS__v0-1
```
