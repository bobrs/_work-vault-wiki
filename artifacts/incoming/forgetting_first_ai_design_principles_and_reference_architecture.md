# Forgetting‑First AI

## Design Principles and Reference Architecture for Consent‑Aware Organizational AI

---

## Purpose

This document defines a **forgetting‑first design philosophy** for deploying AI in organizations where consent, boundaries, and agency must remain intact over time.

It complements the *Consent‑Aware AI in Organizations* taxonomy by translating theory into:

- Concrete **design principles**
- A modular **reference architecture**
- Explicit **forgetting levers** that are technical, not rhetorical

The core premise is simple:

> **Forgetting must be cheaper than remembering, and safer than compliance.**

---

## Part I — Design Principles

These principles are non‑optional if real forgetting is desired. Violating any one of them will reintroduce silent memory accumulation.

---

### Principle 1: Indirection Before Intelligence

**Never expose first‑order meaning to AI when second‑order structure is sufficient.**

- Replace identifiers with opaque tokens
- Abstract sensitive values into buckets, ranks, or classes
- Preserve relational structure without referents

**Forgetting lever:** destroy the indirection index

---

### Principle 2: Context Is a Boundary, Not a Prompt

Context must be **enforced structurally**, not requested linguistically.

- Context is scoped by role, purpose, and time
- Cross‑context access requires explicit re‑witnessing

**Forgetting lever:** expire or delete context shards

---

### Principle 3: Consent Is Loop‑Specific

Consent must be independently scoped for:

- Contribution
- Inference
- Learning
- Decision authority

Consent in one loop does not propagate to others.

**Forgetting lever:** revoke consent → automatic non‑propagation

---

### Principle 4: Memory Must Be Costed

Persistence is never free.

- Default state is non‑persistence
- Storage requires justification, witnessing, and scope

**Forgetting lever:** unattended memory decays automatically

---

### Principle 5: Time Is a First‑Class Constraint

All AI‑touched data must carry an expiration horizon.

- Different loops decay at different rates
- Renewal requires renewed consent

**Forgetting lever:** time‑based invalidation

---

### Principle 6: Witness Before Canon

No AI output becomes organizational memory, policy, or training input without a **human witness** taking epistemic ownership.

Witnessing is not approval; it is accountability.

**Forgetting lever:** unwitnessed outputs evaporate

---

### Principle 7: Learning Is Air‑Gapped

Inference systems and learning systems must be separated.

- Most interactions should never affect model behavior
- Learning occurs slowly, deliberately, and audibly

**Forgetting lever:** inference models are disposable

---

### Principle 8: Similarity Is Scoped

Embedding spaces encode memory implicitly.

- Separate embeddings by role, purpose, and consent domain
- Do not mix vectors across boundaries

**Forgetting lever:** delete embedding spaces, not just records

---

### Principle 9: Non‑Optimization Is a Feature

Some domains must remain intentionally under‑optimized.

- HR
- Governance
- Conflict resolution

What is never learned never needs to be erased.

---

## Part II — Reference Architecture

This architecture is conceptual, not vendor‑specific. It describes **control surfaces**, not implementation details.

---

## 1. Boundary Layer (Pre‑AI)

**Purpose:** enforce indirection and scope *before* AI contact

**Components:**
- Identity tokenizer
- Sensitive value abstraction
- Role + purpose scoping

**Outputs:**
- Opaque tokens
- Structured, non‑identifying representations

---

## 2. Context Shard Manager

**Purpose:** prevent context bleed

**Responsibilities:**
- Create per‑task, per‑role context shards
- Enforce shard isolation
- Track shard expiration

**Failure mode prevented:** cross‑role inference reuse

---

## 3. Inference Engine (Stateless)

**Purpose:** generate outputs without memory

**Characteristics:**
- No long‑term state
- No self‑learning
- Disposable instances

**Critical constraint:** outputs are non‑canonical by default

---

## 4. Inference Classification & Tagging

**Purpose:** limit propagation

Each output is tagged with:
- Inference class (descriptive, predictive, evaluative, speculative)
- Allowed downstream domains
- Expiration horizon

---

## 5. Witness Gate

**Purpose:** control transition from artifact → attractor

**Function:**
- Human explicitly witnesses output
- Confirms contextual validity
- Accepts accountability

**Absent witness:** output cannot persist

---

## 6. Memory Layer (Lossy by Design)

**Purpose:** store only what must persist

**Constraints:**
- No raw transcripts by default
- Summary‑only storage
- Template‑enforced compression

**Storage objects include:**
- Consent scope
- Expiry
- Witness ID

---

## 7. Learning Pipeline (Air‑Gapped)

**Purpose:** deliberate system improvement

**Inputs:**
- Curated, witnessed, consented summaries

**Controls:**
- Audit trails
- Slow update cadence
- Rollback capability

---

## 8. Expiry & Forgetting Engine

**Purpose:** make forgetting automatic

**Responsibilities:**
- Enforce time decay
- Destroy indices and embeddings
- Cascade deletion across layers

No human intervention required.

---

## Part III — Operational Posture

This architecture enforces forgetting not through trust, but through structure.

- Violations fail closed
- Memory requires energy
- Forgetting is the resting state

The organization retains judgment, consent remains reversible, and AI stays bounded.

---

## Closing Note

Most AI systems fail ethically because they are designed to **remember by default**.

A forgetting‑first system reverses the asymmetry:

> *What is remembered is precious. What is forgotten is normal.*

That inversion is the whole game.

