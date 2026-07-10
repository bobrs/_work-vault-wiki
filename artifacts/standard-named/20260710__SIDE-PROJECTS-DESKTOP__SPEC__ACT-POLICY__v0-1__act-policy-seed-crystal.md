# ACT–POLICY Seed Crystal v0.1

**Minimal Substrate for Consent‑Bound Meaning Systems**

---

## 0. Purpose

This document defines the **irreducible substrate** for systems in which meaning is shared, transformed, witnessed, logged, negotiated, or allowed to decay under consent.

It intentionally does **not** define:
- dialogue UX
- fairness or optimization models
- legal or institutional procedure
- trust scoring or reputation logic
- metaphysical assumptions about identity

Those elements exist as *views layered above* this substrate.

This specification defines only:
1. What can happen (`ACT`)
2. How it is allowed (`POLICY`)
3. Who may verify it (`WITNESS`)
4. How shared meaning evolves (`STATE`)

Everything else in the ecosystem compiles into this layer.

---

## 1. Core Ontology

The system rests on **four and only four primitives**.

### 1.1 ACT — Attempted Transformation

An **ACT** is an attempt by an actor to transform shared semantic state.

```
ACT {
  act_id
  actor
  scope
  operator
  payload
  authority_proof
  policy_proof
  timestamp
}
```

An ACT is **not** a message.

It is a *request to change meaning*.

ACTs are evaluated, not merely received.

---

### 1.2 OPERATOR — Type of Transformation

An operator defines **how meaning is being touched**.

This is the complete canonical operator set:

| Operator | Description |
|--------|------------|
| ASSERT | Introduce a claim into scope |
| INQUIRE | Request information |
| MIRROR | Reflect an existing claim verbatim |
| INTERPRET | Propose an inference, model, or meaning |
| PROPOSE | Offer an action, term, or outcome |
| COMMIT | Bind acceptance or agreement |
| RETRACT | Withdraw a prior claim or commitment |
| LOG | Write to durable record |
| ASSIGN | Change roles or delegation |
| BOUND | Set or update policy |
| CLOSE | End scope or overlay |

**Design rule:**
> If an interaction cannot be expressed as one of these operators, it is not primitive.

All higher‑level speech acts compile into this set.

---

### 1.3 POLICY — Executable Consent

A **POLICY** is a function that decides whether an ACT is allowed.

```
POLICY(scope) : (ACT) → {ALLOW | DENY | REQUIRE_CONFIRMATION}
```

POLICY evaluates:
- operator
- actor role
- payload class
- time
- prior state
- delegation bounds

**Consent is not a concept.**  
**Consent is the policy function.**

A *consent vector* is simply a serialized POLICY.

---

### 1.4 STATE — Agreed Semantic Situation

```
STATE(scope) {
  claims
  commitments
  roles
  active_policy
  witnesses
  metadata
}
```

STATE changes **only** via accepted ACTs.

---

## 2. Authority & Delegation

### 2.1 Authority Proof

Every ACT carries an `authority_proof` establishing:
- identity
- role
- delegation chain
- scope validity

Authority answers the question:
> *Why is this actor allowed to attempt this operator?*

---

### 2.2 Delegation Bound Rule

An actor may perform an ACT only if:

```
effective_policy = min(
  policy(scope),
  delegation_policy(principal),
  role_capabilities(actor)
)
```

Delegation can **never** increase authority beyond what the principal consented to.

---

## 3. Payload Classes

Payloads are classified so POLICY can reason over them.

| Class | Description |
|-----|------------|
| C0 | Explicit text / stated claims |
| C1 | Preferences or intent |
| C2 | Interpretations or inferences |
| C3 | Sensitive domains (health, finance, legal, sexuality, etc.) |
| C4 | Identifiers (names, accounts, addresses, unique IDs) |

POLICY may allow some operators on some classes and deny others.

Example:
- INTERPRET allowed on C0, denied on C3
- LOG allowed on C0, denied on C2–C4

---

## 4. Witness

### 4.1 Witness Definition

A **WITNESS** is an actor permitted to verify and record ACT evaluation.

Witness capabilities are **strictly limited by policy**.

A witness may:
- verify POLICY(scope)
- verify ACT validity
- LOG accepted ACTs (if permitted)
- READBACK logged state

A witness may **not**:
- INTERPRET meaning
- PROPOSE outcomes
- alter STATE except via LOG or BOUND when allowed

> **The witness is intentionally weak.**  
> Strength lives in policy, not in the witness.

---

### 4.2 Witness as Overlay

Witnessing is optional.

A scope may have:
- no witness
- one witness
- multiple witnesses

Witness roles are assigned via `ASSIGN` ACTs.

Triads, rotation, and witness networks emerge from POLICY rules over ASSIGN and LOG.

---

## 5. ACT Evaluation Lifecycle

For every ACT:

1. Validate Authority
2. Evaluate POLICY(scope)
3. If DENY → reject
4. If REQUIRE_CONFIRMATION → await matching ACT(s)
5. If ALLOW → apply to STATE
6. If LOG permitted → record

No other state transitions occur.

---

## 6. Logging & Memory

LOG is an operator, not a side effect.

- If POLICY denies LOG, no durable trace exists.
- Memory decay, archival, and resurrection are POLICY‑governed lifecycle processes over logs.

This layer integrates directly with semantic lifecycle and garbage‑collection systems.

---

## 7. Temporal Semantics

POLICY may depend on:
- time
- activity
- consent epoch
- drift thresholds

Re‑consent is expressed as:

```
ACT(operator=BOUND, payload=new_policy)
```

---

## 8. Closure

CLOSE is an ACT.

It:
- ends a scope
- freezes STATE
- triggers lifecycle rules (archive, decay, erase)

---

## 9. Explicit Non‑Goals

This seed crystal deliberately avoids assumptions about:
- humans vs non‑humans
- language vs non‑linguistic signaling
- dialogue structure
- negotiation strategy
- legal enforceability
- trust metrics

Those concerns belong to higher layers.

---

## 10. Derivation Principle

> **Everything is an ACT.**  
> **Everything is gated by POLICY.**  
> **Witnessing is optional and minimal.**  
> **Consent is executable.**  
> **Meaning never mutates without authorization.**

If a system element can be expressed as an ACT evaluated by POLICY and optionally logged by a WITNESS, it belongs in the substrate.

If not, it is a view.

---

## 11. Mapping (Informative)

- Dialog Turns / Threads → serialization and grouping of ACTs
- Consent Semantics → human‑readable POLICY expressions
- Trust Interoperability → archetypal POLICY and LOG patterns
- Transport protocols → ACT envelopes
- Dialogica → high‑level POLICY sets and neutral INTERPRET/PROPOSE roles
- Witness Nets → distributed verification and logging policies
- Loop decay systems → POLICY over log lifecycles

---

## Closing Note

This document is intentionally small.

It is meant to be stable under extension, portable across domains, and resistant to semantic drift.

Everything else grows from here.

