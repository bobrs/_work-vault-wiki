# Consent-Scoped Communication Substrate
## Canonical Specification (v1)

---

### 0. Status and Intent

This document defines a **foundational communication substrate**.

It is not a product proposal, a roadmap, or a user interface description. It is a **protocol-level invariant** intended to remain stable across implementations, industries, and enforcement regimes.

The purpose of this document is to make explicit a layer that already exists implicitly across communication systems, and to do so in a way that simplifies implementation rather than adding complexity.

---

### 1. The Problem This Substrate Addresses

Modern communication systems conflate three distinct concerns:

1. **Scope** — who may see, participate in, or analyze an interaction
2. **Security** — how boundaries are enforced
3. **Trust** — how parties rely on one another

By entangling these concerns, systems fragment into incompatible tools: public forums, group chats, private messaging, and secure channels, each with its own mental model and assumptions.

This fragmentation becomes untenable in the presence of AI systems that can analyze, summarize, infer, and retain information at scale. Implicit boundaries are no longer safe once machines participate.

---

### 2. Core Insight

All communication already has an intended audience and set of constraints.

The failure of existing systems is not a lack of security or moderation, but that **scope is implicit**—encoded in channels, permissions, or social norms rather than declared.

This substrate makes scope **explicit and first-class**.

Everything else—privacy, moderation, security, compliance, encryption—is a matter of enforcing declared scope, not redefining it.

---

### 3. Fundamental Primitive

#### Scoped Utterance

Every communicative act consists of two elements:

- **Content**: the message payload
- **Scope**: an explicit declaration of intended visibility, participation, and reuse

Scope is not inferred from location, channel, or identity. It is declared at the level of the message.

---

### 4. Scope Semantics

A scope specifies:

- who may observe
- who may participate
- how the message may be reused or analyzed

Illustrative examples include:

- `public`
- `polite-public`
- `group:<identifier>`
- `private:<participants>`
- `secure:<domain>`

Scopes may be narrowed, nested, forked, or terminated. All transitions are explicit operations rather than implicit side effects.

---

### 5. The Handshake Ladder (Invariant)

The substrate defines a single ladder of scope refinement:

1. Broad, open scopes
2. Norm-constrained public scopes
3. Group-scoped contexts
4. Private contexts
5. High-assurance restricted contexts

The ladder itself never changes. Systems may start at different rungs or restrict movement, but the semantic structure is invariant.

---

### 6. Separation of Semantics and Enforcement

This substrate defines **scope semantics only**.

It does not mandate enforcement mechanisms. Enforcement may be social, procedural, policy-based, agent-mediated, or cryptographic.

Encryption and authentication enforce scope; they do not define it.

This separation allows simulation without cryptography, early iteration on interaction design, and later hardening without redesign.

---

### 7. Public Visibility and Analysis

In this model:

- Public-scoped information is fully observable and analyzable by anyone
- No actor has privileged analytic rights by default

Exclusivity—of participation, visibility, or analysis—exists only where scope has been explicitly narrowed by consent. This applies equally to humans, organizations, and AI systems.

---

### 8. Compatibility With Secure and Regulated Environments

Hyper-secure or regulated systems are configurations of the same substrate.

They differ only in default entry scope, authentication requirements, and enforcement strength. No alternate protocol is required, and the same message grammar and transition operators apply.

---

### 9. What This Substrate Does Not Define

This substrate does not:

- prescribe trust or reputation models
- define governance or moderation policy
- mandate cryptography
- specify user interfaces

These concerns belong to adjacent layers that build on top of the substrate.

---

### 10. Canonical Statement

> All communication contexts—public, group, private, and secure—are expressions of the same consent-scoped substrate. Differences in safety, privacy, and formality arise from enforcement configuration and entry scope, not from separate systems.

This statement is intended to remain valid indefinitely.