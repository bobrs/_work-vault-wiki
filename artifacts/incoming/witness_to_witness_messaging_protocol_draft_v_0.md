# Witness-to-Witness Messaging Protocol (Draft v0.1)

## Purpose

The Witness-to-Witness (W2W) Messaging Protocol defines a way for meaning to move between people **without being owned, optimized, or reinterpreted by intermediaries**.

It treats communication not as content, but as an **act of witnessing** — bounded by intent, sensitivity, and distribution, and enforced by machines acting on behalf of human consent.

This protocol is substrate-level. It can underlie AI assistants, social media, creative collaboration, governance, and private communication.

---

## Core Premise

> Meaning should travel with its boundaries.

In W2W systems:
- Humans **declare** consent.
- AI **enforces** consent.
- Platforms provide **transport only**.

No system may infer new rights beyond what is explicitly declared.

---

## Definitions

**Witness**  
A participant who receives meaning with the responsibility to honor its declared context and constraints.

**Message**  
Any unit of meaning (text, image, audio, summary, reference, or derived artifact).

**Consent Header**  
A human-readable, machine-parseable declaration that travels with a message and governs its use.

**AI Steward**  
A non-authoritative agent that enforces declared consent, refuses violations, and provides auditability.

---

## The Three Cascades

### 1. Intent Cascade (Forward)
**Question:** *Why am I sharing this, and what may be done with it?*

Intent authorizes downstream actions.
Examples:
- Share for awareness only
- Request feedback
- Invite collaboration
- Bear witness without response

Intent flows **downward** into permitted actions.

---

### 2. Sensitivity Cascade (Reverse)
**Question:** *What is this, and what must never be done with it?*

Sensitivity constrains inference, storage, and reuse.
Examples:
- Unfinished thought
- Personal data
- Creative IP
- Therapeutic or vulnerable material

Sensitivity flows **upward**, overriding convenience or optimization.

---

### 3. Distribution Cascade (Lateral)
**Question:** *Who is this for, and where may it travel?*

Distribution governs audience, transport, and propagation.
Examples:
- Only this witness
- Friends group
- Role-based group
- Public, with attribution

Distribution flows **sideways** across networks.

---

## The Witness Header (Minimal Fields)

Every W2W message may include a header with the following fields:

- **Author**: pseudonymous or attributed
- **Audience**: me | specific witness(es) | group | public
- **Intent**: view | reflect | respond | collaborate | witness-only
- **Sensitivity**: public | personal | sensitive | protected | sacred
- **Rights**: view | comment | quote | remix | act-on
- **Derivatives**: allowed | summaries-only | quotes ≤ N | none
- **Distribution**: forwardable | same-audience-only | no-forward
- **TTL**: duration or expiry condition
- **Attribution**: required | optional | forbidden
- **Training**: allowed | never

Headers must be readable by humans without tooling.

---

## Enforcement Rules

1. **Declared consent is the sole source of authority.**
2. **Restrictions override permissions** in case of conflict.
3. **AI may refuse action** but may not invent consent.
4. **Silence is a valid action** when consent is unclear.
5. **All actions and refusals must be auditable.**

---

## Audit Requirements

Every message must be able to answer:
- What consent authorized this action?
- What restriction limited or blocked action?
- What data was explicitly not used?
- Why did this occur now?

Audits must be available to the author and relevant witnesses.

---

## Identity Model

W2W does not require global identity.

- Identity may be ephemeral, contextual, or relationship-bound.
- Trust is situational, not reputational.
- Audience sets may be cryptographic, list-based, or role-based.

Witness status arises from **consent**, not profile permanence.

---

## Role of Platforms

Platforms are transports.

They may:
- carry messages
- cache encrypted payloads
- render headers

They may not:
- reinterpret intent
- expand distribution
- infer rights
- optimize meaning

---

## Role of AI

AI acts as a **steward**, not an author.

AI may:
- parse consent headers
- enforce constraints
- refuse violations
- explain enforcement decisions

AI may not:
- reinterpret intent
- derive new permissions
- train on restricted material

---

## Outcomes

Witness-to-Witness systems enable:
- AI assistants that are trustworthy by construction
- Social media with real audience boundaries
- Portable creator rights
- Therapy- and creativity-safe AI
- Audit-ready governance

---

## Closing Principle

> Consent is no longer a setting or a click.
> It is a declarative layer that travels with meaning.
>
> Witness-to-witness messaging is how humans remain sovereign in the AI age.

---

*Draft v0.1 — intended to evolve through use, not decree.*

