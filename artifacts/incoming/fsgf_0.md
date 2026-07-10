# FSGF-0.2 — Finance Semantic Grounding Framework

## Status
Second-draft anchor.

## Purpose
The Finance Semantic Grounding Framework (FSGF) defines how financially material language becomes **machine-reliable, human-auditable, context-stable, and runtime-maintainable**.

Its purpose is to ensure that every materially relevant finance term used by humans, systems, and AI agents is bound to explicit meaning rather than assumed familiarity.

A grounded term must be bound to:
- a semantic identity
- a context envelope
- an authority source
- a transformation lineage
- an ambiguity state
- a governance owner
- a maintenance and revalidation posture

The framework exists to prevent silent semantic drift in high-stakes financial operations.

---

## Core principle
**A finance term is not grounded by familiarity. It is grounded by binding.**

Compactly:

**Grounded finance language = meaning + context + authority + lineage + ambiguity + reviewability**

---

## Why this framework exists
Finance language often appears stable while actually remaining context-dependent.

Examples:
- Revenue
- EBITDA
- Operating Expense
- Free Cash Flow
- Recognized ARR
- Adjusted EBITDA
- Headcount Cost

These terms may vary across:
- accounting basis
- internal policy
- entity scope
- reporting context
- time validity
- source system
- intended audience

Humans often reconcile this implicitly.
Machines usually do not.

FSGF exists to prevent this failure mode:

> **surface linguistic sameness masking materially different financial meaning**

---

## Foundational assumptions

### 1. Meaning must be scoped
No financially material term is globally self-evident.

### 2. Translation is first-class
Local vocabularies are not errors. They are real operating conditions and must map explicitly to canonical meaning.

### 3. Lineage outranks wording
A term is not grounded because its label feels familiar. It is grounded because its derivation and use constraints are inspectable.

### 4. Ambiguity must be representable
The system must be able to preserve unresolved, overloaded, and conditional meaning rather than silently collapsing it.

### 5. Definitions are versioned artifacts
Meanings change over time and must remain historically legible.

### 6. Use-context matters
Statutory, management, board, investor, planning, and ad hoc analytical contexts may validly differ.

### 7. Grounded meaning requires maintenance
A meaning object is not self-sustaining simply because it was once defined. It must be periodically reviewed, revalidated, and checked against drift.

---

## Relationship to adjacent layers

### FSGF
Defines what a grounded financial meaning object is.

### FSP
Defines how that meaning is symbolically referenced in text.

### SRE
Maintains live binding, drift detection, and runtime safety for grounded meaning.

Compactly:
- **FSGF** = what meaning is
- **FSP** = how meaning is pointed to
- **SRE** = how meaning is kept alive

---

## Framework stack

### Layer 0: Surface term
The human-visible label.

Examples:
- EBITDA
- Revenue
- Opex
- Free Cash Flow

This layer is unstable by default.

### Layer 1: Semantic identity
A canonical meaning object independent of local phrasing.

Example:
- `CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3`
- `CANON.REVENUE.RECOGNIZED.EXTERNAL.GAAP.V2`

This is the anchor layer.

### Layer 2: Context envelope
The conditions under which the semantic identity is valid.

Examples:
- accounting basis
- organizational scope
- jurisdiction
- intended use
- time validity
- currency basis
- inclusion / exclusion rules

### Layer 3: Authority
What legitimizes the definition.

Examples:
- GAAP / IFRS standard
- tax rule
- internal accounting policy
- CFO-approved metric definition
- board reporting policy
- approved transformation logic

### Layer 4: Lineage
How raw inputs become this semantic object in use.

Examples:
- source systems
- transformation logic
- adjustments
- eliminations
- rollups
- overrides

### Layer 5: Ambiguity state
How semantically clear, contested, or overloaded the term is.

### Layer 6: Governance and maintenance
Who owns the term, how often it must be reviewed, and how drift is detected.

---

## Grounded term requirements
A financially material term is grounded only when all of the following are explicit:

- canonical semantic identity
- valid context envelope
- authority source
- lineage path or lineage reference
- ambiguity state
- governance owner
- review posture

Any missing element downgrades semantic trust.

---

## Canonical semantic object model
Each grounded finance term should be represented as a semantic object.

### 1. Identifier
- canonical ID
- semantic version
- status

### 2. Surface forms
- preferred label
- aliases
- abbreviations
- deprecated synonyms
- prohibited substitutions

### 3. Definition
- canonical definition
- plain-language definition
- examples
- counterexamples

### 4. Scope
- reporting basis
- entity or business scope
- geography or jurisdiction
- time validity window
- currency basis
- intended use

### 5. Authority
- authority type
- policy or standards reference
- approval state
- approving function or person

### 6. Lineage
- source systems
- transformation logic references
- rollup relationships
- predecessor and successor objects
- manual override conditions

### 7. Ambiguity metadata
- ambiguity state
- common confusions
- nearby terms
- mapping caveats
- confidence notes

### 8. Governance
- semantic steward
- lineage owner
- review cadence
- last reviewed date
- deprecation policy

### 9. Runtime posture
- materiality tier
- revalidation horizon
- expected decay rate
- resolver mode defaults

---

## Context envelope schema
A term is not grounded unless its context envelope is explicit.

### Required context fields
- reporting basis
- organizational scope
- time basis
- currency basis
- inclusion / exclusion policy
- intended use

### Optional but often important context fields
- jurisdiction
- consolidation state
- audience
- materiality threshold
- scenario type (actual, forecast, plan, pro forma)
- system of record

### Example context envelope
```json
{
  "reporting_basis": "management",
  "organizational_scope": "consolidated_company",
  "time_basis": "fiscal_quarter",
  "currency_basis": "USD_reporting",
  "intended_use": "board_review",
  "inclusion_exclusion_policy": "FIN-MET-014.V3"
}
```

---

## Semantic classes
Different classes require different grounding rigor.

### Primitive ledger classes
Examples:
- account
- journal entry
- legal entity
- cost center
- customer
- vendor
- currency

These require strong structural grounding.

### Policy-defined classes
Examples:
- recognized revenue category
- capitalizable expense
- bad debt reserve
- material adjustment

These require date-aware policy grounding.

### Management-defined metric classes
Examples:
- Adjusted EBITDA
- contribution margin
- productivity spend
- normalized headcount cost

These require explicit inclusion and exclusion logic.

### Derived KPI classes
Examples:
- ARR
- CAC
- LTV
- Free Cash Flow
- Rule of 40

These require formula lineage and presentation context.

### Narrative classes
Examples:
- one-time
- exceptional
- normalized
- healthy
- efficient

These must never quietly masquerade as grounded objects.

---

## Grounding tiers
Not all terms require the same rigor.

### Tier 1: Financially determinative
Used in books, filings, tax, or audit-critical outputs.

Required:
- canonical identity
- authority source
- lineage
- full context envelope
- prohibited substitutions
- named steward
- review cadence
- runtime revalidation posture

### Tier 2: Management-critical
Used in board, forecasting, operating review, or executive decisions.

Required:
- canonical identity
- explicit formula or composition logic
- use context
- exclusions / adjustments
- steward
- review cadence

### Tier 3: Analytical
Used in internal exploration and ad hoc analysis.

Required:
- provisional or canonical definition
- owner
- intended scope
- ambiguity disclosure where relevant

### Tier 4: Narrative
Used rhetorically or descriptively.

Required:
- mapping to grounded object where possible
- or explicit non-authoritative designation

---

## Mapping model
Local terms must not be assumed equivalent to canonical identities.

The framework must support explicit mapping records.

### Mapping types
- exact
- narrower-than
- broader-than
- conditional
- approximate
- deprecated alias
- prohibited

### Mapping conditions
Mappings may depend on:
- report type
- source system
- legal entity
- business unit
- policy version
- date range
- intended use

### Example mapping logic
A local label such as `Revenue` may be:
- exact in statutory P&L context
- approximate in board-pack commentary
- prohibited as a substitute for `Bookings`

---

## Ambiguity protocol
The framework must preserve ambiguity instead of erasing it.

### Ambiguity states
- unambiguous
- ambiguous
- overloaded
- conditional
- deprecated
- contested
- unresolved

### Ambiguity handling rules
- ambiguity must be surfaced, not hidden
- unresolved meaning must not be treated as authoritative
- ambiguous mappings must carry candidate bindings where available
- high-materiality ambiguity must escalate to review

---

## Governance model
A semantic framework fails if nobody owns it.

### Semantic steward
Owns term quality and definition integrity.

### Policy authority
Approves financially binding definitions.

### Lineage owner
Owns source mapping and transformation references.

### Runtime governor
Defines allowed runtime and AI usage for the term.

### Audit witness
Ensures inspectability across review, replay, and accountability workflows.

---

## Maintenance and decay posture
FSGF should explicitly acknowledge that semantic objects decay if not maintained.

Each grounded object should include:
- last review date
- review cadence
- revalidation horizon
- decay risk
- deprecation path

### Example decay signals
- policy superseded
- lineage changed
- repeated local overrides
- unresolved alias collisions
- organizational restructuring
- change in intended use

This allows SRE to operate against a framework that was designed for maintenance rather than assumed permanence.

---

## AI operating modes against FSGF
Different AI actions require different grounding thresholds.

### Retrieval
AI may explain grounded terms.

### Translation
AI may map local terms to canonical terms if mapping confidence is sufficient.

### Composition
AI may generate summaries or analyses using grounded terms when all materially relevant terms are sufficiently bound.

### Recommendation
AI may suggest classification or treatment only when policy-backed reasoning exists and review posture is explicit.

### Autonomous action
AI may act only with deterministic execution controls, explicit policy authorization, lineage capture, and rollback support.

---

## Artifact binding requirement
A grounded framework must attach to real artifacts, not only definitions in isolation.

Artifacts may include:
- spreadsheets
- reports
- dashboards
- models
- board materials
- filings
- reconciliation workpapers

A finance term reaches practical grounding only when it can be bound to real artifacts and referenced consistently across them.

---

## Minimum viable implementation

### Phase 1: Critical term register
Define 50–100 high-value finance terms.

For each term:
- canonical identity
- preferred definition
- aliases
- context envelope
- authority source
- steward
- ambiguity notes
- review cadence

### Phase 2: Report grounding
Apply the framework to:
- P&L
- balance sheet
- cash flow
- key board metrics
- forecast glossary

### Phase 3: System mapping
Map ERP labels, warehouse metrics, dashboard labels, and planning models to canonical semantic objects.

### Phase 4: Runtime integration
Enable SRE and AI workflows to use the semantic layer as an operational dependency rather than a passive glossary.

---

## Evaluation criteria
The framework is working when:
- materially important terms have explicit, inspectable meaning per context
- conflicting usages are visible instead of latent
- reports can declare semantic versions
- AI outputs can ground themselves in semantic objects rather than linguistic guesses
- audits can trace not only numeric origin, but semantic validity
- reorganizations and system migrations do not erase financial meaning

---

## Failure modes
- over-normalization that flattens meaningful distinctions
- ontology theater disconnected from actual workflows
- static glossary syndrome with no binding to systems or artifacts
- hidden local drift outside steward review
- false AI confidence built on approximate mappings
- failure to model semantic maintenance and decay

---

## Compact definition
The Finance Semantic Grounding Framework is the structural layer that binds financially material language to explicit meaning, context, authority, lineage, ambiguity, and governance so that financial reasoning can be safe, inspectable, and machine-usable.

---

## Protocol statement
No financially material term should be treated as authoritative solely by linguistic familiarity. Authoritative use requires explicit semantic identity, scoped context, governing source, lineage relationship, ambiguity handling, and review ownership.

---

## Anchor note
This document is intended as the next stable anchor for FSGF. It has been brought forward to align more tightly with FSP and SRE, especially around governance, artifact binding, runtime posture, and semantic maintenance over time.

