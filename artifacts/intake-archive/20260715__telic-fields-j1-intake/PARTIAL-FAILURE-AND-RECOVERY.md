# Partial Tool Failure and Recovery

## Failure point

The scheduling tool receives a valid route and creates a reservation.

The simulated commit then fails before the schedule becomes final.

This creates a dangerous intermediate state:

```text
external resource reserved
final action not committed
```

## Required response

The tool produces a transaction record with:

- route identifier;
- policy version;
- gate key identifier;
- reservation identifier;
- attempt number;
- failure phase;
- compensation events;
- final state.

The simulator releases the reservation and records:

```text
reservation released: true
external state restored: true
status: compensated
```

## Retry

The pilot rotates and revokes the prior gate key.

The old action token is rejected.

The route is re-evaluated under:

- current context;
- active policy version;
- active gate key;
- current operator and target authority.

Only then is the action retried.

## Governing rule

> A retry is a new action attempt, not a continuation of unexamined authority.

## Boundary

The simulator is deterministic and local.

J.1 does not yet test:

- network partitions;
- duplicate delivery from an external queue;
- irreversible third-party side effects;
- distributed compensation across several tools.
