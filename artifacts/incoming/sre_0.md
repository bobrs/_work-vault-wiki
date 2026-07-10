# SRE-0.1 — Semantic Resolution Engine

## Status
First-draft anchor.

## Purpose
The Semantic Resolution Engine (SRE) is the runtime layer that keeps semantically grounded artifacts alive, current, and safe to use.

If FSP detects symbolic semantic references and FSGF defines grounded meaning, SRE performs the living work of resolution, re-resolution, drift detection, attention allocation, and execution gating.

The SRE is not a static lookup service. It is an attention system.

---

## Core function
The SRE receives parsed semantic references such as:

```text
{EBITDA}
{Revenue@GAAP}
{EBITDA@Board#V3}
```

and determines, at runtime:
- what semantic object they bind to
- whether that binding is still valid
- what context envelope applies
- whether drift or decay has occurred
- whether the requested use is permitted
- whether execution may proceed, must pause, or must escalate

---

## Foundational principle
**Meaning does not remain safe merely because it was once resolved.**

A resolved term is a maintained artifact, not a permanent fact.

---

## Primary invariant
**Resolution is a living act of attention, not a one-time lookup.**

---

## Position in the stack

surface text → FSP → typed semantic reference → SRE → grounded semantic object + runtime status → execution / AI reasoning / audit trail

Relationship to sibling layers:
- **FSGF** defines what grounded terms are
- **FSP** identifies semantic references in text
- **SRE** keeps those references valid in live operation

---

## Why SRE exists
Financial terms decay when they are treated as self-sustaining artifacts.

Examples of decay signals:
- a policy version changed
- a report context shifted
- a mapping was overridden
- an entity was reorganized
- a dashboard reused a term outside its original scope
- a once-valid interpretation now conflicts with current authority

The SRE exists to prevent silent semantic decay.

---

## Core responsibilities

### 1. Runtime resolution
Bind a parsed reference to a canonical semantic object.

### 2. Re-resolution
Re-evaluate existing bindings when context, policy, or system state changes.

### 3. Drift detection
Detect when a previously safe interpretation has become unstable or invalid.

### 4. Decay monitoring
Track semantic half-life, freshness, and coupling loss.

### 5. Permission and policy gating
Determine whether a bound semantic object may be explained, calculated, published, or acted upon.

### 6. Execution control
Return one of:
- proceed
- proceed with warning
- pause for review
- reject

### 7. Witness generation
Produce traceable records of how resolution occurred and why.

---

## Core concepts

### Semantic artifact
A grounded meaning object from FSGF that can be resolved and used.

### Attention
The runtime maintenance required to keep a semantic artifact current and trustworthy.

### Coupling
The degree of live connection between a term, its authority, its context, and its current use.

### Decay
The gradual loss of confidence that a semantic artifact remains valid in a given context.

### Drift
A detected mismatch between current usage and current semantic validity.

### Revalidation
An explicit act of refreshing confidence in a semantic artifact.

---

## Resolution contract

### Input
The SRE accepts parser output such as:

```json
{
  "notation": "{}",
  "status": "grounded",
  "surface_term": "EBITDA",
  "context": "Board",
  "specifier": "V3"
}
```

### Output
The SRE returns:

```json
{
  "resolution_status": "resolved",
  "canonical_id": "CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3",
  "canonical_label": "Adjusted EBITDA",
  "context_envelope": {
    "reporting_basis": "management",
    "organizational_scope": "consolidated",
    "intended_use": "board_review"
  },
  "authority_ref": "FIN-MET-014",
  "lineage_ref": "LINEAGE.METRIC.EBITDA.BOARD.V3",
  "attention_state": {
    "freshness": "current",
    "drift_risk": "low",
    "coupling_score": 0.96,
    "last_validated_at": "2026-04-09T00:00:00Z"
  },
  "policy_decision": "proceed",
  "confidence": 0.98
}
```

---

## Runtime states
Each semantic reference should carry a runtime state.

### Resolution states
- resolved
- unresolved
- ambiguous
- deprecated
- conflict
- stale
- decayed

### Policy states
- allowed
- allowed_with_warning
- review_required
- prohibited

### Attention states
- current
- aging
- stale
- unstable
- decayed

---

## Semantic decay model
The SRE should explicitly model semantic decay.

### Decay signals
- authority changed
- steward review overdue
- policy superseded
- context mismatch detected
- lineage broken or incomplete
- source system remapped
- alias conflict introduced
- frequent human override patterns

### Decay indicators
- time since last validation
- divergence between expected and actual usage
- increase in ambiguity frequency
- repeated fallback to local mappings
- conflicting references across artifacts

### Suggested decay outputs
- freshness score
- drift risk score
- coupling score
- revalidation urgency

---

## Attention mechanics
The SRE should be designed as an attention allocation engine.

### Attention tasks
- maintaining active bindings
- revalidating stale bindings
- monitoring high-risk terms
- checking use-context alignment
- detecting semantic leakage across adjacent reports or systems

### Attention is finite
The SRE should support prioritization.

Priority inputs may include:
- financial materiality
- regulatory sensitivity
- frequency of use
- ambiguity rate
- policy churn
- scope of downstream impact

This allows the system to spend the most attention where semantic failure would be most costly.

---

## Revalidation triggers
Revalidation should occur when any of the following happen:

### Time-based triggers
- validation half-life exceeded
- steward review cadence reached

### Context-based triggers
- document type changed
- entity scope changed
- reporting basis changed
- user role changed
- intended use changed

### Authority-based triggers
- policy updated
- standard interpretation revised
- canonical object deprecated

### Lineage-based triggers
- transformation logic modified
- source system changed
- manual override inserted

### Pattern-based triggers
- unusual ambiguity cluster
- repeated human disagreement
- conflict across related artifacts

---

## Coupling model
Coupling measures how strongly a live usage remains aligned with grounded meaning.

### Example contributors to coupling
- authority freshness
- context alignment
- lineage completeness
- alias certainty
- policy consistency
- human validation recency

### Suggested coupling interpretation
- 0.90–1.00 = strongly coupled
- 0.70–0.89 = usable but aging
- 0.50–0.69 = unstable
- below 0.50 = decayed / unsafe

Coupling should affect whether execution proceeds.

---

## Drift detection
The SRE should detect multiple classes of drift.

### Definition drift
The surface term now points to a different semantic identity.

### Context drift
The same definition is being used in an invalid or broadened scope.

### Authority drift
The governing policy changed but the old meaning persists locally.

### Lineage drift
The derivation path changed while the label remained constant.

### Narrative drift
Human shorthand begins to masquerade as grounded terminology.

---

## Policy and consent gating
The SRE should integrate with a policy engine that governs allowed actions.

### Example policy decisions
- AI may explain `{Revenue@GAAP}`
- AI may calculate `{Revenue@GAAP}` only using approved lineage
- AI may not publish `{Revenue@GAAP}` without human sign-off
- AI may not bind `<Adjusted Earnings>` as authoritative in production output

### Policy dimensions
- action type
- user role
- system role
- materiality tier
- confidence threshold
- audit requirement

---

## Execution decisions
For each resolved or partially resolved reference, the SRE returns an execution posture.

### Proceed
Safe for the requested use.

### Proceed with warning
Usable, but drift, aging, or ambiguity should be surfaced.

### Pause for review
Human confirmation required before use.

### Reject
Execution not permitted or semantic state unsafe.

---

## Witness and audit record
Every resolution event should generate a witness record.

### Witness record fields
- raw reference text
- parsed reference object
- canonical resolution result
- context envelope applied
- policy checks performed
- decay / drift indicators
- execution decision
- timestamp
- actor or system identity

The witness record exists to support replay, audit, and post-hoc review.

---

## Resolver modes

### Strict mode
Used for filings, close processes, audit support, or regulated reporting.
- unresolved grounded references are errors
- ambiguity blocks execution
- stale bindings require revalidation

### Advisory mode
Used for analysis, drafting, and exploration.
- ambiguity surfaces warnings
- candidate bindings may be suggested
- outputs remain non-authoritative

### Discovery mode
Used during rollout and ontology maturation.
- aggressive suggestion behavior
- all outputs remain provisional
- no autonomous authority granted

---

## Resolution precedence
Suggested resolution order:

### For `{TERM@CONTEXT#SPECIFIER}`
1. exact canonical ID or policy tag if specifier is explicit
2. exact alias match within context
3. exact canonical label in context
4. version-aware default mapping
5. otherwise ambiguous

### For `{TERM@CONTEXT}`
1. exact alias in context
2. canonical label in context
3. context-specific default
4. otherwise ambiguous

### For `{TERM}`
1. active document context
2. active team or system context
3. permitted global default
4. otherwise ambiguous

The SRE must prefer explicit ambiguity over overconfident resolution.

---

## Example resolution cases

### Case A: stable binding
Input:
```text
{EBITDA@Board}
```
If the board metric registry is current, policy unchanged, and lineage intact, return resolved + proceed.

### Case B: stale binding
Input:
```text
{Revenue@GAAP}
```
If policy changed last week and steward review is incomplete, return stale + pause for review.

### Case C: decayed alias
Input:
```text
{Operating Margin}
```
If the term maps to multiple current objects across related entities, return ambiguous or decayed.

### Case D: narrative masquerade
Input:
```text
(core profitability)
```
Tag as narrative only; prohibit authoritative use without explicit mapping.

---

## Minimal runtime schema
```json
{
  "reference_id": "ref_001",
  "raw_text": "{EBITDA@Board#V3}",
  "parsed": {
    "notation": "{}",
    "surface_term": "EBITDA",
    "context": "Board",
    "specifier": "V3"
  },
  "resolution": {
    "canonical_id": "CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3",
    "resolution_status": "resolved"
  },
  "attention_state": {
    "freshness": "current",
    "coupling_score": 0.96,
    "drift_risk": "low",
    "revalidation_urgency": "low"
  },
  "policy_state": {
    "decision": "proceed",
    "mode": "strict"
  },
  "witness": {
    "timestamp": "2026-04-09T00:00:00Z",
    "actor": "system"
  }
}
```

---

## AI integration
When an LLM encounters a semantic reference, the orchestration layer should:
1. parse it with FSP
2. send it to SRE
3. resolve and validate the reference
4. inject grounded meaning, lineage, and policy posture into the model context
5. constrain generation according to runtime state
6. attach witness metadata to downstream outputs

This ensures AI reasons over live bindings, not guessed meanings.

---

## Minimum viable implementation

### Phase 1
- support runtime resolution of top 50–100 critical finance terms
- basic ambiguity detection
- manual revalidation workflow

### Phase 2
- add coupling scores and freshness tracking
- integrate policy gates
- generate witness records automatically

### Phase 3
- drift monitoring across reports and dashboards
- automatic revalidation triggers
- entity and policy-aware routing

### Phase 4
- execution gating for AI-assisted workflows
- rollback and reversibility support
- organizational attention budgeting

---

## Failure modes
- treating SRE as a static dictionary lookup
- caching meaning beyond its validation horizon
- overtrusting global defaults
- suppressing ambiguity to preserve workflow speed
- failing to emit witness records
- ignoring decay because numbers still look plausible

---

## Compact definition
The Semantic Resolution Engine is the runtime attention system that keeps grounded financial meaning live, current, permitted, and auditable.

---

## Anchor note
This document is intended as the first stable anchor for SRE. It should evolve alongside FSP and FSGF, and should remain aligned with the principle that semantic safety requires continued attention, not one-time declaration.

