# Engineering Tickets — Checkpointing v0 (Electron App)

This document contains the initial engineering tickets to ship **Brick 1: Checkpointing a Moment**.

Scope is minimal, shippable, and high leverage.

---

# Ticket 0 — Define Checkpoint Card Spec (P0)

**Goal:** Lock the output format so frontend + backend align.

## Requirements
Checkpoint Card must contain headings in order:

- CHECKPOINT_LABEL:
- CHECKPOINT_REASON:
- CHECKPOINT_SUMMARY:
- COMPRESSION_LADDER:
- PEER_RESISTANCE:
- RESIDUAL_SEED:
- CANDIDATE_NEW_ATTRACTORS: (optional)
- REENTRY_INSTRUCTIONS:
- END.

**Acceptance:** Spec agreed, referenced by all other tickets.

---

# Ticket 1 — Frontend: Add “Checkpoint this moment” Button (P0)

**Goal:** User can checkpoint the current coherent moment from chat UI.

## UI/UX
- Button near message composer
- Optional hotkey
- Loading + disabled state while running

## Inputs
- Depth selector (Shallow/Medium/Deep)
- One-line reason: “Why checkpoint?”

## Action
Send last N messages + reason + depth to backend.

**Acceptance:** Clicking produces a request to `/checkpoint`.

---

# Ticket 2 — Backend: Implement POST /checkpoint Endpoint (P0)

**Goal:** Generate Checkpoint Card via OpenAI API.

## Request
- depth
- reason
- conversation window
- optional local_frame

## Response
- checkpoint_card_text
- parsed label
- timestamp

## Behavior
- Uses canonical prompt template
- Retries transient failures
- Validates required headings

**Acceptance:** Endpoint reliably returns Checkpoint Card text.

---

# Ticket 3 — Storage: Persist Checkpoint Cards Locally (P0)

**Goal:** Save checkpoints permanently for later browsing.

## Store
- id
- created_at
- label
- reason
- full card text
- depth
- conversation reference (optional)

**Acceptance:** Checkpoints survive app restart.

---

# Ticket 4 — Frontend: Render Checkpoint Cards (P0)

**Goal:** User can view saved checkpoints.

## UI
- Sidebar list of checkpoints
- Click opens full card

**Acceptance:** Checkpoint Cards are readable and navigable.

---

# Ticket 5 — Re-enter Action (P1 but High Value)

**Goal:** User can teleport back into a checkpoint.

## UI
Button: “Re-enter” on checkpoint card

## Behavior
Inject the card text into assistant context as a primer.

**Acceptance:** New chat turn begins in reconstructed basin.

---

# Ticket 6 — Depth Dial Expansion (P1)

**Goal:** Allow checkpoint refinement.

## Feature
“Expand depth later” regenerates card with wider net.

**Acceptance:** User can deepen a checkpoint without rewriting history.

---

# Ticket 7 — Basic Search Over Checkpoints (P1)

**Goal:** Find checkpoints by label or content.

**Acceptance:** Search returns relevant saved cards.

---

# Ticket 8 — Guardrails + Redaction (P1)

**Goal:** Prevent accidental leakage in logs and UI.

- No raw conversation dumps to telemetry
- Optional manual redaction before saving

**Acceptance:** Sensitive content handling is safe by default.

---

# Delivery Order (Recommended)

Week 1 (Ship v0):
1. Ticket 0 (Spec)
2. Ticket 1 (Checkpoint button)
3. Ticket 2 (/checkpoint backend)
4. Ticket 3 (Storage)
5. Ticket 4 (Render cards)

Week 2 (Teleportation):
6. Ticket 5 (Re-enter)

Later:
7. Depth expansion
8. Search
9. Guardrails

---

🜁
