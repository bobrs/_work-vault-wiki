# Stable Loop Language 🝳 — First Five Rules (Vale Style)

> This document rewrites the first five Snort-style signature rules as **Vale-compatible prose lint rules**.
>
> Assumptions:
> - Rules live under a custom style, e.g. `StableLoop/`.
> - Document context is provided via frontmatter or directory mapping (e.g. `spec`, `policy`, `instructions`).
> - Severity can be tuned per doc class via Vale config.

---

## 0. Shared Conventions

Each rule follows standard Vale YAML structure:

```yaml
extends: existence | substitution | conditional
message: "..."
level: error | warning | suggestion
scope: sentence | paragraph | text
```

Where possible:
- **Regex is conservative** (trigger early, explain clearly).
- **Human disambiguation is preferred** over auto-correction.

---

## Rule 1 — MAY_NOT_AMBIGUITY

**File:** `StableLoop/MAY_NOT_AMBIGUITY.yml`

```yaml
extends: existence
message: "‘may not’ is ambiguous (prohibition vs uncertainty). Use ‘must not’ for prohibition or ‘might not’ for uncertainty."
level: error
scope: sentence
ignorecase: true
tokens:
  - "may not"
```

**Intent**
- Hard error in `spec` and `policy` docs.
- Downgrade to `warning` in `instructions` if desired.

---

## Rule 2 — MAY_DEONTIC_UNMARKED

**File:** `StableLoop/MAY_DEONTIC_UNMARKED.yml`

```yaml
extends: existence
message: "Unmarked ‘may’ with an agent is ambiguous (permission, authorization, capability, or intent). Replace with an explicit modality."
level: error
scope: sentence
ignorecase: true
tokens:
  - "\\b(you|users?|clients?|callers?|requesters?)\\s+may\\b"
```

**Notes**
- This rule intentionally fires broadly.
- Use suggestions or documentation to guide rewrites:
  - permission → “is permitted to”
  - authorization → “is authorized to”
  - capability → “can”
  - intent → “is considering”

---

## Rule 3 — SHOULD_REASONLESS

**File:** `StableLoop/SHOULD_REASONLESS.yml`

```yaml
extends: existence
message: "‘should’ without rationale hides authority. Add a reason (‘because …’) or replace with ‘must’ if required."
level: warning
scope: sentence
ignorecase: true
tokens:
  - "\\bshould\\b"
```

**Tuning Guidance**
- Pair with a *positive* rule that allows “should … because …”.
- Escalate to `error` in safety- or compliance-critical policies.

---

## Rule 4 — PASSIVE_AGENT_HIDING

**File:** `StableLoop/PASSIVE_AGENT_HIDING.yml`

```yaml
extends: existence
message: "Passive permission/prohibition hides the authority. Specify who permits, requires, or prohibits this action."
level: warning
scope: sentence
ignorecase: true
tokens:
  - "\\b(is|are|was|were|be|been)\\s+(allowed|permitted|required|prohibited|recommended)\\b"
```

**Examples Flagged**
- “Access is allowed after verification.”

**Preferred Rewrite**
- “The system permits access after verification.”

---

## Rule 5 — VAGUE_EVALUATIVE_TERMS

**File:** `StableLoop/VAGUE_EVALUATIVE_TERMS.yml`

```yaml
extends: existence
message: "Vague evaluative term detected. Replace with measurable criteria or specify who decides and how."
level: warning
scope: sentence
ignorecase: true
tokens:
  - "\\breasonable\\b"
  - "\\bappropriate\\b"
  - "\\bas needed\\b"
  - "\\bwhere applicable\\b"
  - "\\bbest effort\\b"
```

---

## Optional: Severity Mapping by Doc Class

Example `.vale.ini` snippet:

```ini
[*.md]
BasedOnStyles = StableLoop

[spec/*.md]
StableLoop.MAY_NOT_AMBIGUITY = error
StableLoop.MAY_DEONTIC_UNMARKED = error

[instructions/*.md]
StableLoop.MAY_NOT_AMBIGUITY = warning
```

---

## Design Principle (Canonical)

> **Deterministic detection first. Semantic clarification second. Human choice always available.**

These rules are meant to surface *loop instability*, not to enforce stylistic purity.

---

## Next Logical Extensions

- `CAN_CAPABILITY_VS_PERMISSION.yml`
- `WILL_PROMISE_VS_PREDICTION.yml`
- `UNDEFINED_PRONOUN.yml`
- `SCOPE_LEAK.yml` ("including but not limited to", "etc.")
- `BEST_EFFORT_NONCOMMITMENT.yml`

