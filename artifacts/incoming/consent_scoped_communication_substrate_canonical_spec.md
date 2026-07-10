# Consent-Scoped Communication Substrate

## Canonical, Durable Specification

### Purpose
This document defines a **single, unified communication substrate** capable of operating across all security, privacy, and social contexts—from hostile public environments to hyper-secure, closed systems—without changing protocol semantics, mental models, or message structure.

It is intended to be **stable, minimal, and future-proof**.

---

## Core Claim (Invariant)

> All communication contexts can be implemented using the same protocol primitives. Differences in security, privacy, or formality arise solely from **enforcement configuration and starting scope**, not from different systems.

This is a reformulation of the substrate itself.

---

## Fundamental Primitive

### Scoped Utterance

Every message consists of:

- **Content**: the message payload
- **Scope**: an explicit declaration of intended visibility, participation, and boundary conditions

The scope is a first-class field, not an implicit property of the channel.

---

## Scope Semantics

Scopes define *who may see, respond to, or propagate* an utterance.

Examples (non-exhaustive):

- `public`
- `polite-public`
- `group:<identifier>`
- `private:<participants>`
- `secure:<domain>`

Scopes may be:
- nested
- narrowed
- forked
- terminated

Scope transitions are explicit operations.

---

## The Handshake Ladder

The protocol defines a **single ladder of scope refinement**:

1. Broad / open scopes
2. Norm-constrained scopes
3. Group-scoped contexts
4. Private or restricted scopes
5. High-assurance / cryptographically enforced scopes

**The ladder itself never changes.**

Different systems may start at different rungs.

---

## Entry Point Variability (Not Mode Switching)

A system may begin operation at any point on the ladder:

- Open public discourse → broad scope, minimal enforcement
- Organizational collaboration → group scope, policy enforcement
- Regulated or classified environments → restricted scope, cryptographic enforcement

In all cases:
- message structure is identical
- scope semantics are identical
- transition operators are identical

---

## Enforcement Separation

Scope semantics are defined independently of enforcement.

### Enforcement may be:
- Social / normative
- Agent-respected (AI or human)
- Policy-based
- Cryptographic

Encryption and access control **enforce scopes**; they do not define them.

This separation allows:
- simulation without cryptography
- early iteration on social dynamics
- later hardening without redesign

---

## Simulation-First Validity

The protocol is valid when scopes are implemented as:
- plain-text tags
- socially respected annotations

Simulation is not a shortcut; it is the correct developmental phase.

Cryptographic enforcement may be introduced later with no change to:
- message grammar
- user behavior
- protocol semantics

---

## Hyper-Secure Compatibility

Hyper-secure systems are a configuration of this same substrate:

- restricted default scopes
- mandatory authentication
- cryptographic enforcement from the first message

No alternate protocol is required.

---

## Benefits of This Reformulation

- One protocol for all contexts
- One mental model for users
- One message schema for developers
- Explicit, auditable boundary transitions
- Reduced moderation and policy ambiguity
- AI-safe scope visibility and enforcement

---

## Final Statement (Canonical)

> This protocol defines a consent-scoped communication substrate in which all social, private, and secure interactions are expressions of the same underlying primitives. Security, privacy, and formality are properties of enforcement configuration and entry scope—not of separate systems.

This document is intended to remain valid indefinitely.

