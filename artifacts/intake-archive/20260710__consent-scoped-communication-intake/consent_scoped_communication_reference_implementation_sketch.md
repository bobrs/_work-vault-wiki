# Consent-Scoped Communication
## Reference Implementation Sketch

---

### Purpose

This document describes a **minimal, concrete reference implementation** of the consent-scoped communication substrate.

It is not a production system and not a product roadmap. Its purpose is to demonstrate that the substrate:

- can run as a real system
- collapses complexity rather than adding it
- supports public, group, private, and secure interaction using the same primitives

This sketch is intentionally small and implementation-agnostic.

---

### Design Constraints

The reference implementation must:

- use a single message grammar
- treat scope as explicit metadata
- separate semantics from enforcement
- work without cryptography initially
- allow cryptographic enforcement to be added later without redesign

---

### Core Data Model

#### Message

Every message has the following structure:

```
Message {
  id: MessageID
  content: Payload
  scope: ScopeDescriptor
  timestamp: Time
  author: AgentID
}
```

Only `content` and `scope` are semantically required. Other fields support ordering and attribution.

---

### Scope Descriptor

```
ScopeDescriptor {
  type: public | polite-public | group | private | secure
  participants: optional [AgentID]
  domain: optional Identifier
  permissions: optional Constraints
}
```

Notes:
- `type` defines the semantic class of scope
- `participants` restricts visibility and participation
- `domain` allows grouping (e.g. organization, project)
- `permissions` expresses reuse or analysis constraints

This structure is extensible without changing semantics.

---

### Scope Operations

The reference system supports the following operations:

- **Declare**: create a message with an explicit scope
- **Refine**: narrow scope (e.g. public → group)
- **Fork**: create a new scoped thread from an existing one
- **Terminate**: end a scoped interaction

All operations are explicit and visible.

---

### Enforcement Layer (Pluggable)

The reference implementation separates scope semantics from enforcement.

Initial enforcement modes:

- UI-level filtering
- agent compliance (human or AI)
- logging and visibility

Later enforcement modes:

- access control
- encryption
- cryptographic capability checks

Enforcement consumes `ScopeDescriptor` but does not redefine it.

---

### AI Interaction Model

AI agents operate under the same rules as humans.

- AI may freely analyze messages with `public` scope
- AI must check scope before summarizing, remembering, or reusing content
- Cross-scope leakage is treated as a detectable violation

This allows AI safety to be evaluated operationally.

---

### Minimal Scenario Walkthrough

**Scenario: Public to Private Transition**

1. A discussion begins in `public` scope
2. A participant refines scope to `polite-public`
3. Two participants fork to `group:design`
4. A sensitive detail triggers a fork to `private:[A,B]`
5. An AI assistant summarizes only within allowed scopes

No platform switch occurs. Only scope changes.

---

### Cryptographic Hardening (Optional)

Cryptographic enforcement can be added by:

- mapping `ScopeDescriptor` to encryption domains
- issuing keys or capabilities per scope
- enforcing access at message delivery time

No changes to message grammar or user behavior are required.

---

### Evaluation Hooks

The reference implementation exposes hooks for:

- detecting scope violations
- auditing AI behavior
- testing boundary clarity
- simulating adversarial conditions

These hooks support later preregistered evaluation without constraining design.

---

### Outcome

This reference implementation demonstrates that:

- one protocol supports all communication contexts
- scope is sufficient as the primary abstraction
- security and privacy emerge from enforcement configuration

It establishes a concrete foundation for further development and evaluation.