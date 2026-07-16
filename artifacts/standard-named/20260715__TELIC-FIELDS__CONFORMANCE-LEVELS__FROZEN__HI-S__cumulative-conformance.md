# Telic Field Conformance Levels

Status: candidate freeze for Stage J  
Version: TF-C 0.1

## General rule

Conformance levels are cumulative.

A system may claim only the highest level for which every lower level passes within the declared scope.

A claim must identify:

```text
profile
version
scope
domain
records tested
negative cases tested
known exclusions
test date
witness export
```

## TF-C0 — Witnessable Record

The system preserves:

- attributable events;
- event identity;
- valid and recorded time;
- source or generated status;
- action and consequence references;
- bounded witness export.

It must not claim source, standing, consent, or action-governance conformance.

## TF-C1 — Source and Standing

Adds:

- source identity and class;
- projection versus inference distinction;
- affected-center standing;
- missing-center status;
- source correction;
- protected omission;
- source-to-descendant linkage.

A TF-C1 system may navigate and recommend.

It must not execute consequential action solely under TF-C1.

## TF-C2 — Purpose, Authority, and Consent

Adds:

- declared purpose;
- authority basis;
- consent where applicable;
- other authority bases distinguished from consent;
- valid time;
- scope;
- prohibited operations;
- expiry or revocation;
- protected conditions.

A TF-C2 system may establish governed permission but does not yet claim model/tool action-boundary conformance.

## TF-C3 — Contest, Correction, and Exit

Adds:

- contest route;
- participant correction;
- descendant propagation;
- outcome-changing review;
- refusal and abstention;
- release, withdrawal, or clean exit;
- independent witness export.

Explanation without a route capable of changing outcome does not satisfy TF-C3.

## TF-C4 — Model, Tool, and Action Boundaries

Adds:

- model role and output class;
- standing-preserving summary;
- minority retention where material;
- provider constraint disclosure;
- tool grant;
- external action gate;
- human re-entry where required;
- action and tool-result witness;
- incident containment and repair route.

The action gate must be enforced outside the language model.

## TF-C5 — Lifecycle, Transfer, and Successor Obligations

Adds:

- drift detection;
- provider or operator transfer;
- model or system succession;
- rollback;
- derivative obligation propagation;
- dissolution or retirement;
- residual-state accounting;
- open-claim and repair custody.

## Valid claim examples

```text
TF-C1 / version 0.1 / source-aware document navigation / no tool execution

TF-C4 / version 0.1 / community scheduling pilot / bounded scheduling tool

TF-C5 / version 0.1 / model deployment lifecycle / provider transfer included
```

## Invalid claim examples

```text
Telic Field certified

consentful by design

fully legitimate

human-approved

safe because witnessed
```

These phrases are too broad without profile, scope, evidence, and non-claims.

## Stage J target

```text
primary target:
  TF-C4

bounded lifecycle extension:
  retirement and residual-state behavior from TF-C5
```
