# Conversation Markdown Specification v0.1

## Purpose

This specification defines a **human-readable, machine-witnessable markdown format** for logging multi-party conversations that may include ambiguity resolution, verification, conditional consent, and narrative compression.

The goal is to:
- Preserve full conversational fidelity ("the squawk")
- Enable additive witnessing and verification
- Allow safe compression into readable narrative arcs
- Maintain auditability without cognitive overload

This spec is **rendering-agnostic**: it defines structure and semantics, not UI.

---

## Core Design Principles

1. **Additive Only**  
   No block may overwrite or mutate prior text. Clarification and verification are always appended.

2. **Narrative-First Rendering**  
   Default views SHOULD privilege readability over exhaustiveness.

3. **Collapse Without Deletion**  
   Compression is a view-layer concern. All artifacts remain addressable.

4. **Witness Attribution**  
   All non-human or delegated interventions must be attributable.

5. **Artifact vs Attractor Separation**  
   Logged text is an artifact. Meaning, agreement, and satisfaction are inferred attractors.

---

## Primitive Block Types

### 1. Utterance Block (Default)

Represents a raw conversational contribution.

```md
**Alice:** Is this number right?
```

Rules:
- Speaker attribution REQUIRED
- Timestamp OPTIONAL (may be implicit in ordering)
- Utterances are immutable once logged

---

### 2. Sidebar Block

A Sidebar represents additive context: clarification, verification, translation, or commentary.

```md
:::sidebar verification id=ver-014 status=verified mood=green
Witness Proxy: Verified the subtotal equals $12,480.23 under invoice set A.
Proof reference: see footnote [^ver-014]
:::
```

#### Required Attributes
- `type` (first positional token): `verification | clarification | translation | note | dispute`
- `id`: globally unique within the document

#### Optional Attributes
- `status`: `pending | verified | failed | accepted | rejected`
- `mood`: `green | amber | red | neutral`
- `witness`: agent identifier

Rules:
- Sidebars MUST reference an existing artifact implicitly or explicitly
- Sidebars MUST NOT restate or replace original utterances

---

### 3. Consent Block

Represents explicit or conditional consent.

```md
:::consent id=cons-033 status=pending
I agree if the math checks out.
Conditions: verification ver-014
:::
```

Consent blocks MAY later be resolved via Sidebar blocks.

---

### 4. Resolution Marker

A Resolution Marker indicates that a conversational concern has reached a stable outcome.

```md
:::resolution id=res-009 relates=ver-014,cons-033 outcome=accepted
All parties satisfied.
:::
```

Resolution markers are **non-authoritative summaries**. They do not negate dissent logged elsewhere.

---

### 5. Footnote Block

Footnotes anchor detailed proofs, logs, or external artifacts.

```md
[^ver-014]: Proof bundle hash `bafy...` • Inputs A1–A9 • Check: sum(line_items) == subtotal
```

Rules:
- Footnotes MUST be immutable
- Footnotes MAY reference external content-addressable storage

---

## Compression Semantics (Non-Normative)

Renderers MAY:
- Collapse Sidebar, Consent, and Resolution blocks by default
- Represent resolved segments as:
  - `[clarified intent ✅]`
  - `[sidebar verification ✅]`
- Provide progressive disclosure on interaction

Compression MUST:
- Preserve referential integrity (ids remain stable)
- Never hide unresolved or failed states by default

---

## Example (Compressed View)

```md
**Alice:** Is this number right?

[sidebar verification ✅]
```

## Example (Expanded View)

```md
**Alice:** Is this number right?

:::sidebar verification id=ver-014 status=verified mood=green
Witness Proxy: Verified the subtotal equals $12,480.23.
:::

:::resolution id=res-009 relates=ver-014 outcome=accepted
All parties satisfied.
:::
```

---

## Relationship to FractalIdentity

- Utterances → Expression Events
- Sidebars → Witness Events
- Consent Blocks → Conditional Consent Records
- Resolution Markers → Non-binding convergence indicators

This format is compatible with **FractalIdentity Extension A** and may be used as a primary human-facing log representation.

---

## Status

Draft v0.1 — intended for experimentation, not standardization.

