# ACT–POLICY Seed Crystal v0.1 — Worked Examples

This document provides **concrete examples** of the ACT–POLICY substrate in use.

The goal is not completeness, but *demonstrability*: each example shows how ordinary interaction, mediation, and witnessing reduce cleanly to ACTs evaluated by POLICY.

---

## Example 1 — Simple Information Request (No Witness)

**Scenario:** Participant A asks Participant B for a standard sourdough recipe. No witness is involved.

### Initial STATE(scope="recipe")
- claims: ∅
- commitments: ∅
- roles: A=SPEAKER, B=SPEAKER
- active_policy: allows ASSERT, INQUIRE, INTERPRET, PROPOSE
- witnesses: ∅

### ACT 1 — A asks
```
ACT {
  actor: A
  scope: "recipe"
  operator: INQUIRE
  payload: "Can you give me a standard sourdough recipe?"
}
```

POLICY("recipe") → ALLOW

STATE unchanged (question introduced).

### ACT 2 — B responds
```
ACT {
  actor: B
  scope: "recipe"
  operator: ASSERT
  payload: "A basic sourdough uses starter, flour, water, and salt..."
}
```

POLICY("recipe") → ALLOW

STATE updated with claim.

*No logging occurs because LOG was never attempted.*

---

## Example 2 — Witness Overlay Mid-Conversation

**Scenario:** A and C are discussing a sensitive topic. A asks B to witness.

### ACT 1 — Invite witness
```
ACT {
  actor: A
  scope: "A-C-discussion"
  operator: ASSIGN
  payload: "Invite B as witness"
}
```

### ACT 2 — B accepts
```
ACT {
  actor: B
  scope: "A-C-discussion"
  operator: ASSIGN
  payload: "Accept witness role"
}
```

STATE updated: witness=B

---

## Example 3 — Consent Policy Set by Primaries

**Scenario:** A and C set consent rules for the witnessed scope.

### ACT 3 — A proposes policy
```
ACT {
  actor: A
  scope: "A-C-discussion"
  operator: BOUND
  payload: {
    allow: [ASSERT, INQUIRE],
    deny: [INTERPRET, PROPOSE],
    log: {C0:1, C1:0, C2:0, C3:0, C4:0}
  }
}
```

POLICY → REQUIRE_CONFIRMATION

### ACT 4 — C confirms
```
ACT {
  actor: C
  scope: "A-C-discussion"
  operator: COMMIT
  payload: "Accept policy"
}
```

POLICY becomes active.

---

## Example 4 — Witness-Enforced Violation

**Scenario:** A attempts interpretation when it is disallowed.

### ACT 5 — Violation attempt
```
ACT {
  actor: A
  scope: "A-C-discussion"
  operator: INTERPRET
  payload: "I think you feel this way because..."
}
```

POLICY("A-C-discussion") → DENY

### Witness action
- Witness verifies denial
- Witness interrupts (no STATE change, no LOG)

---

## Example 5 — Consented Logging and Readback

**Scenario:** A and C allow logging of explicit statements.

### ACT 6 — Log a statement
```
ACT {
  actor: C
  scope: "A-C-discussion"
  operator: LOG
  payload: {
    class: C0,
    text: "C wants to pause the project for two weeks."
  }
}
```

POLICY → ALLOW

Witness logs item.

### ACT 7 — Readback
```
ACT {
  actor: A
  scope: "A-C-discussion"
  operator: INQUIRE
  payload: "Witness, read back the current context."
}
```

Witness outputs logged snapshot verbatim.

---

## Example 6 — Round-Robin Triad Witnessing

**Scenario:** Participants A, B, C ensure mutual accountability by rotating witness roles.

### Phase 1
- Witness=B
- Primaries=A,C

### Phase 2
```
ACT {
  actor: A
  scope: "triad"
  operator: ASSIGN
  payload: "Rotate witness to C"
}
```

C accepts; witness=C
Primaries=A,B

### Phase 3
Witness rotates again to A.

Each phase produces its own consented log, none of which requires trust in a single witness.

---

## Example 7 — Consent Decay and Re-Bound

**Scenario:** Time passes; consent expires.

POLICY includes: `expiry = 7 days`

### After expiry
Any ACT → REQUIRE_CONFIRMATION

### ACT — Re-consent
```
ACT {
  actor: A
  scope: "A-C-discussion"
  operator: BOUND
  payload: "Renew prior policy"
}
```

C commits; policy resumes.

---

## Example 8 — Mapping to Dialogica (Informative)

A Dialogica mediation session is simply:
- a scope with a specialized POLICY
- neutral actors allowed INTERPRET and PROPOSE
- mandatory LOG for decisions
- CLOSE only after COMMIT

No new primitives are required.

---

## Closing Observation

In every case:
- nothing happens without an ACT
- nothing proceeds without POLICY
- nothing persists without LOG permission
- witnessing is optional, minimal, and structural

These examples demonstrate that the seed crystal is sufficient to generate the entire higher-level ecosystem.

