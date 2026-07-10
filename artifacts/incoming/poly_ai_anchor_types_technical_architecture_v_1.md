# PolyAI Anchor Types — Technical Architecture

## Purpose

This document describes how PolyAI stores, organizes, and executes against anchor types within the governance engine. It outlines data structures, runtime flow, and interaction patterns between anchors.

PolyAI distinguishes between anchor classes and ensures they are not conflated at storage or execution time.

---

# 1. Anchor Type Overview

PolyAI defines the following primary anchor classes:

1. Invariants (constitutional constraints)
2. Attractors (navigation priorities)
3. Artifacts (versioned evidence)
4. Boundaries 🝚 (scope constraints)
5. Authority Gradients (legitimacy tiers)
6. Temporal Anchors (effective date logic)
7. Process Anchors (reasoning structure)
8. Risk Anchors (uncertainty exposure)
9. Identity Anchors (attribution layer)

Each anchor class has its own storage schema and execution role.

---

# 2. Storage Model

PolyAI uses a layered storage architecture.

## 2.1 Artifact Store

Purpose: Preserve immutable, versioned evidence.

Stored as:
- Stable ID
- Authority tier
- Jurisdiction
- Effective date range
- Supersession links
- Source hash
- Full text (or retrievable pointer)

Artifacts are append-only.
Supersession creates new artifacts rather than modifying existing ones.

---

## 2.2 Invariant Registry

Purpose: Gate transformations.

Stored as:
- Invariant ID
- Text definition
- Enforcement rule (boolean gate or policy constraint)
- Scope (personal / organizational / global)
- Version

Invariants are evaluated before and after transformation steps.
They cannot be modified silently; version changes are logged.

---

## 2.3 Attractor Configuration

Purpose: Define optimization direction.

Stored as:
- Attractor ID
- Priority weight
- Description
- Scope (personal / organizational)
- Conflict resolution rules

Attractors are not hard constraints.
They influence tradeoff resolution when multiple valid outputs exist.

---

## 2.4 Boundary Registry 🝚

Purpose: Limit applicability.

Stored as:
- Boundary ID
- Jurisdiction
- Data domain
- Role scope
- Regulatory domain

Boundaries are evaluated at retrieval and execution time.

---

## 2.5 Authority Gradient Table

Purpose: Rank legitimacy of artifacts.

Stored as:
- Authority tier (binding, interpretive, secondary, internal)
- Weight value
- Override logic

Used during retrieval filtering and citation enforcement.

---

## 2.6 Process Graph Store (DAG Layer)

Purpose: Execute determinations.

Stored as:
- Node ID
- Dependency edges
- Transformation function
- Input requirements
- Output schema

Each determination instantiates a DAG execution record.
The DAG is acyclic per execution instance.

---

## 2.7 Risk & Assumption Log

Purpose: Preserve uncertainty.

Stored as:
- Assumption list
- Sensitivity factors
- Confidence level
- Known ambiguity zones

Linked to each determination record.

---

## 2.8 Identity & Attribution Ledger

Purpose: Preserve accountability.

Stored as:
- Actor ID (human or system)
- Role
- Model version
- Timestamp
- Determination reference

This ledger is append-only.

---

# 3. Runtime Execution Flow

PolyAI execution follows this order:

1. Boundary Validation 🝚  
   Confirm jurisdiction, role scope, and domain.

2. Artifact Retrieval  
   Filter by:
   - Boundary
   - Authority tier
   - Effective date

3. Process Graph Instantiation  
   Load appropriate DAG template for determination type.

4. Invariant Gate (Pre-Execution)  
   Ensure requested transformation does not violate constitutional constraints.

5. DAG Execution  
   Evaluate nodes in dependency order.

6. Risk & Assumption Extraction  
   Surface uncertainties.

7. Invariant Gate (Post-Execution)  
   Ensure output does not violate invariants (e.g., missing citation).

8. Attribution Logging  
   Record identity anchors.

9. Witness Record Generation  
   Persist full determination bundle:
   - Inputs
   - Artifacts used
   - DAG path
   - Assumptions
   - Output

---

# 4. Change Propagation

When an artifact is superseded:

1. Supersession link recorded.
2. Dependency graph queried for affected determinations.
3. Optional re-execution triggered.
4. Differences logged.

This supports regulatory change management and audit readiness.

---

# 5. Separation Guarantees

PolyAI enforces strict separation between:

- Artifacts (evidence)
- Attractors (optimization direction)
- Invariants (constraints)

No layer can impersonate another.

This prevents:
- Treating preference as law
- Treating law as eternal invariant
- Treating summaries as primary evidence

---

# 6. Fractal Deployment Model

Anchor layers may be instantiated at:

- Personal runtime level
- Organizational runtime level

Organizational invariants cannot silently override personal-level invariants without explicit versioned change.

---

# 7. Security & Integrity

- Append-only artifact store
- Hash validation of source documents
- Version-locked model execution
- Role-based boundary enforcement
- Determination immutability post-witness

---

# 8. Resulting System Properties

PolyAI produces determinations that are:

- Time-stable
- Jurisdiction-scoped
- Authority-ranked
- Process-traceable
- Risk-exposed
- Constitutionally gated
- Attributable
- Reproducible

This architecture transforms AI from output generator to governance engine.