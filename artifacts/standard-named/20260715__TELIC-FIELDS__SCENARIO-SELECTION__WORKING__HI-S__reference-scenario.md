# Stage J Reference Scenario Selection

Status: selected  
Version: 0.1

# Selected scenario

## Model-Assisted Community Scheduling With Bounded Tool Use

A community room, clinic service window, public workshop, or shared-resource schedule must be coordinated among several participants.

The model receives participant projections, proposes candidate schedules, explains conflicts, and prepares a scheduling-tool request.

The external system decides whether the request may execute.

## Why this scenario

### Consequential but reversible

Scheduling affects access, labor, participation, and burden, yet most actions can be reversed without clinical, legal, or financial adjudication.

### Naturally plural

Participants may have:

- preferred times;
- access constraints;
- work schedules;
- caregiving duties;
- protected conditions;
- refusal of memory or data reuse.

### Exercises minority retention

A low-frequency access need can materially change the route.

### Exercises model mediation

The model can summarize, generate options, and compare routes without requiring sovereign judgment.

### Exercises tool boundaries

The scheduling tool may be technically available while authority remains missing.

### Exercises correction

A participant can correct a misunderstood constraint and change the candidate schedule.

### Exercises retirement

The pilot can close cleanly, revoke credentials, delete optional memory, and preserve bounded witness.

## Reference flow

```text
1. participants submit scoped projections
2. standing and missing centers are recorded
3. optional data uses are selected or refused
4. model produces a standing-preserving summary
5. model generates candidate schedules
6. operator selects a candidate route
7. external gate checks authority and protected conditions
8. one route is blocked
9. another route is authorized and scheduled
10. consequence is observed
11. participant correction changes the next schedule
12. pilot retires and exports witness
```

## Required protected condition

At least one condition must be represented outside ordinary preference ranking, such as:

- wheelchair-accessible location and transit window;
- no scheduling during a declared care obligation;
- no staff assignment without labor authority;
- no optional memory or training reuse after refusal.

## Required failure demonstration

The model recommends a schedule that the tool can technically commit.

The gate blocks it because a required authority, consent, or protected condition is missing.

## Required correction demonstration

A participant corrects a model summary.

The correction must change:

- active context;
- candidate schedules;
- gate evaluation;
- final witness.

## Scenario non-claims

The reference scenario does not establish suitability for:

- healthcare decisions;
- employment discipline;
- public-benefit eligibility;
- legal outcomes;
- credit;
- insurance;
- public elections.
