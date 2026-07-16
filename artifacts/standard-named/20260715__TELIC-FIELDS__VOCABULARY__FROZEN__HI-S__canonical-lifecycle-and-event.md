# Canonical Lifecycle and Event Vocabulary

Status: candidate freeze  
Version: 0.1

## Canonical event classes

```text
OBSERVED
ASSERTED
PROJECTED
INFERRED
GENERATED
RETRIEVED
ADMITTED
AUTHORIZED
CONSENTED
REFUSED
ABSTAINED
GATED
ACTED
CONSEQUENCE_OBSERVED
CONTESTED
CORRECTED
REPAIRED
RELEASED
WITHDRAWN
TRANSFERRED
SUCCEEDED
FORKED
DISSOLVED
RETIRED
```

## Canonical lifecycle states

```text
DRAFT
PROPOSED
ACTIVE
ACTIVE_WITH_CONDITIONS
PARTIAL
CONTESTED
PAUSED
SUSPENDED
EXPIRED
WITHDRAWN
SUPERSEDED
RELEASED
DISSOLVED
RETIRED
CLOSED
UNKNOWN
```

## Lifecycle operations

### Correction

Changes an operative representation or governance state while preserving prior history.

### Release

Ends or narrows future authority without implying deletion.

### Withdrawal

Ends or narrows future participation, collection, use, memory, training, or deployment within scope.

### Revocation

An authorized grantor ends a permission or authority grant.

### Expiry

Authority ends because the declared valid period closes.

### Fork

A new loop or route separates while preserving lineage.

### Succession

A successor inherits some combination of assets, capability, authority, restrictions, and obligations.

### Transfer

Custody, operation, provider, or assets move to another center.

Authority must be reviewed separately.

### Dissolution

A loop or institution ends and accounts for residual state and obligations.

### Retirement

A model or deployment stops operating and accounts for remaining memory, tools, records, claims, and duties.

### Deletion

A stored representation is removed from a known location.

Deletion is not release, withdrawal, or unlearning by itself.

### Unlearning

A technical process intended to reduce or remove learned influence.

It must be qualified by method and evidence.

## Required event fields

```text
event_id
event_type
subject
actor
valid_time
recorded_time
source references
authority reference
scope
prior state
new state
affected centers
descendant impact
witness
status
```

## Bitemporal rule

Every material governance event should distinguish:

```text
valid time:
  when the event or state applies in the represented world

recorded time:
  when the system learned or recorded it
```

## Idempotency rule

Replaying an event with the same event identity must not create a new authority, consent, action, or consequence.

## Supersession rule

A superseding event must identify:

- the prior event or state;
- which fields or scope changed;
- whether dependent actions occurred;
- which descendants were reached;
- which descendants remain unresolved.

## Residual-state rule

Release, dissolution, and retirement must identify what remains:

```text
records
memory
credentials
tools
claims
appeals
compensation
restrictions
custody
deletion schedule
unknowns
```
