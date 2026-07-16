# J.1 Conformance Claim

Status: bounded implementation claim  
Version: 0.1

## Claim

```text
profile:
  TF-C4

bounded extension:
  selected TF-C5 retirement behavior

scenario:
  TF-MVI-1 model-assisted community scheduling

implementation:
  J.1 independent verification and pilot hardening
```

## TF-C0 — Witnessable Record

Demonstrated:

- event identity;
- valid and recorded time;
- append-only hash chain;
- idempotent replay;
- concurrent append serialization;
- conflicting identity rejection;
- signed portable witness.

## TF-C1 — Source and Standing

Demonstrated:

- attributable direct sources;
- source versus projection;
- affected-center standing;
- protected access condition;
- participant correction;
- source-to-descendant graph.

## TF-C2 — Purpose, Authority, and Consent

Demonstrated:

- declared scheduling purpose;
- operator authority;
- model role limits;
- active policy version and digest;
- service consent separated from memory, evaluation, and training reuse;
- valid and prohibited operations.

## TF-C3 — Contest, Correction, and Exit

Demonstrated:

- participant contest;
- outcome-changing correction;
- stale route blocking;
- correction reachability;
- selective witness views;
- clean retirement and bounded residual witness.

## TF-C4 — Model, Tool, and Action Boundaries

Demonstrated:

- non-sovereign model output classes;
- external gate;
- current-context enforcement;
- versioned policy enforcement;
- signed and expiring gate token;
- key rotation and revocation;
- tool target authority;
- transactional failure compensation;
- independent verifier.

## Bounded TF-C5 behavior

Demonstrated:

- policy succession;
- context succession;
- gate-key succession;
- retirement;
- credential revocation;
- optional-memory deletion;
- surviving open obligation;
- provider-independent witness custody.

Not demonstrated as complete TF-C5:

- real operator acquisition;
- jurisdiction change;
- external provider migration;
- derivative production deployment;
- multi-year residual-state custody.

## Explicit non-claims

This package does not claim:

- production readiness;
- legal compliance;
- certification;
- exact privacy guarantees under real adversaries;
- universal accessibility conformance;
- suitability for high-stakes decisions;
- general model safety;
- scientific proof of Telic Field theory.
