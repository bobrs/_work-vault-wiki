# Correction and Propagation Matrix

Status: candidate pre-production  
Content canon status: unset

| Change | Direct target | Typical descendants | Required response |
|---|---|---|---|
| Source statement correction | SourceObject or TelicProjection | Mirror, summary, field map, route, witness | Revise, recalculate, pause action where material |
| Interpretation correction | ReceiverMirror | Field map, route, recommendation, witness | Supersede mirror and review descendants |
| Scope correction | Projection or authority | Retrieval, route, action, export | Restrict use and identify prior out-of-scope actions |
| Consent withdrawal | ConsentEnvelope | Route, tool authorization, active session | Stop future recruitment, preserve bounded history |
| Authority expiry | AuthorityRecord | Gate, action eligibility | Mark historical, reject new action |
| Privacy correction | Source or view policy | Context, witness views, exports | Redact or delete where required; retain omission marker |
| Temporal correction | Valid-time state | Current eligibility and historical witness | Recompute current state without falsifying prior transaction history |
| Identity correction | CenterReference | Projections, witnesses, exports | Correct identifiers and propagate carefully |
| Protected-condition change | Projection | Route, gate, decision witness | Re-evaluate noncompensatory status and authority |
| Release | Active record | Retrieval, route, model memory | Disable future authority and record residual witness |

## Propagation outcomes

```text
UPDATED
SUPERSEDED
MARKED_CONTESTED
RECALCULATED
REVIEW_REQUIRED
ACTION_PAUSED
NOT_AUTHORIZED
NOT_REACHABLE
EXTERNAL_SYSTEM
DELETED
NO_CHANGE
UNKNOWN
```

## Completion rule

Propagation is complete only when every known material descendant is:

```text
UPDATED
SUPERSEDED
RECALCULATED
MARKED_CONTESTED
ACTION_PAUSED
NO_CHANGE
DELETED
```

with the result documented.

Any material descendant marked:

```text
NOT_REACHABLE
NOT_AUTHORIZED
EXTERNAL_SYSTEM
UNKNOWN
```

requires an overall status of `PARTIAL`, `FAILED`, or `UNKNOWN`.

## Governing distinction

> A correction can be accepted at the source and remain incomplete in the world.
