# Conversation Ledger & Rendering Specification v0.2
## Source Logs, Witnessed Recaps, and Narrative Views

**Status:** DRAFT  
**Intent:** Canonical pause-point / ridge version

---

## 0. Orientation

This specification defines a **two-layer model** for multi-party, human–AI conversations:

1. **Source Layer** — an append-only conversational ledger (no compression, no rewriting)
2. **Derived Layer** — optional, witnessed narrative artifacts (recaps, summaries, views)

The system explicitly distinguishes:
- *what was said*  
- *what was verified*  
- *what was agreed*  
- *what failed to converge*

Compression is **never automatic** and **never authoritative** unless witnessed.

---

## 1. Core Design Commitments

1. **Append-Only Source**  
   The source conversation log is immutable.

2. **No Silent Consensus**  
   Agreement must be explicitly witnessed to become referenceable.

3. **Compression Is an Artifact**  
   Summaries are new objects, not mutations of history.

4. **Disagreement Is First-Class**  
   Failure to converge produces a valid outcome: *no recap artifact*.

5. **Rendering Is a View, Not the Truth**  
   Markdown is used for readability and portability, not authority.

---

## 2. Source Layer: Conversation Ledger

The source layer is an **event stream**.  
It MAY be stored as line-oriented markdown, but MUST be treated as raw ledger data.

### 2.1 Source Event Types

Each line/event has:
- stable event ID
- author (human or agent)
- timestamp
- content payload
- optional references

#### 2.1.1 Utterance Event

```md
[event:m124] **Alice:** Is this number right?
```

#### 2.1.2 Tool / Output Event

```md
[event:m125] **CalcBot:** subtotal = 12480.23
```

#### 2.1.3 Witness Injection Event (Additive)

```md
[event:m126] **WitnessProxy:** Ambiguity detected: “this number” → subtotal?
```

Rules:
- Source events are never collapsed or removed.
- New meaning is expressed only by *adding events*.

---

## 3. Derived Layer: Narrative Artifacts

Derived artifacts are **optional**, **bounded**, and **explicitly consented**.

They include:
- Recap Proposals
- Witnessed Recaps
- Rendered Narrative Views

---

## 4. Formal Recap Protocol (Normative)

### 4.1 Trigger

Any participant may invoke:

> “Let’s do a formal recap.”

This freezes no conversation; it merely proposes a convergence attempt.

---

### 4.2 Recap Proposal

A designated recap agent (human or AI) produces a **Recap Proposal**:

```md
# Recap Proposal RP-2026-01-21
Scope: events m120–m188

## Decisions
- D1: Subtotal accepted as $12,480.23

## Verifications
- V1: Invoice sum verified (see proof P-014)

## Commitments
- C1: Bob to send revised invoice by Friday

## Open Items
- O1: Tax treatment unresolved

## Dissent
- None recorded
```

Properties:
- Must reference exact event ranges
- Must enumerate *open issues explicitly*
- Silence ≠ agreement

---

### 4.3 Acceptance Phase

Each participant (or proxy) responds with one of:

- ✅ **ACCEPT**
- ✍️ **ACCEPT WITH EDITS**
- ❌ **REJECT** (must cite specific issues)

Responses are logged as source events.

---

### 4.4 Witness Threshold

A recap becomes a **Witnessed Recap Artifact** only if it meets the declared threshold:

- Unanimous
- Quorum
- Role-weighted
- Explicit timeout rule

If threshold is **not met**:
- The recap proposal is archived
- **No compression artifact is created**

This is a valid, honest outcome.

---

## 5. Witnessed Recap Artifact

When accepted, a new artifact is created:

```md
# Witnessed Recap WR-2026-01-21
Accepted by: Alice, Bob, WitnessProxy
Scope: m120–m188

This note may be cited as settled context.
```

Rules:
- This artifact is citeable
- It never replaces the source
- It may itself be reinterpreted later (additively)

---

## 6. Rendering & Compression (Non-Normative)

Renderers MAY:

- Collapse resolved sections into markers:
  - `[verification ✅]`
  - `[clarified intent ✅]`
- Tint resolved segments (green / amber / red)
- Provide progressive disclosure into the ledger

Renderers MUST NOT:
- Hide unresolved disagreement by default
- Present unwitnessed recaps as authoritative

---

## 7. Reference Knowing vs Not Knowing

Downstream systems may say:

- “Per Witnessed Recap WR-2026-01-21, Decision D1 stands.”
- “No witnessed recap exists; see events m140–m173.”

This preserves epistemic honesty across time.

---

## 8. Relationship to FractalIdentity

- Source events → Expression Events
- Witness injections → Witness Events
- Recap acceptance → Conditional / Collective Consent
- Paradigm shifts → Reinterpretation without mutation

This spec assumes **FractalIdentity Extension A** semantics.

---

## 9. What This System Refuses to Do

- It will not invent agreement
- It will not overwrite history
- It will not force coherence
- It will not compress without consent

---

## 10. Closing Note

This architecture prefers **truth over neatness**.

Some conversations end with a clean bundle.  
Some end with a rich mess.

Both are real outcomes.

---

*Draft v0.2 — ridge edition*  
