# Stable Loop Language 🝳 — First Five Signature Rules (Snort-style)

> Goal: quick, cathartic “Snort rules for language” that can later be translated into real lint rules (Vale, custom AST, etc.).
>
> Design stance: **detect first**, then offer **stable rewrites** or a **clarifying question**. We’re not trying to be complete—just high-leverage.

---

## Conventions

- **Doc classes** (context tags): `spec`, `policy`, `instructions`, `marketing`, `chat`.
- **Severity**: `INFO < WARN < ERROR`.
- **Scores** (optional): `loop 🝳`, `boundary 🝚`, `breach 🜬` on a 0–1 scale.
- **Action**:
  - `ALERT` → highlight + suggest rewrites.
  - `ASK` → ask a one-line disambiguation question.
  - `FAIL` → block merge / publication in strict contexts.

Rule format (pseudo):
```
RULE <id>
WHEN <pattern>
AND <context>
THEN <action, severity>
BECAUSE <why>
SUGGEST <rewrite options>
OR ASK <clarifying question>
```

---

## Rule 1 — MAY_NOT_AMBIGUITY

```
RULE SLL-001 MAY_NOT_AMBIGUITY
WHEN token == "may not"
AND doc_class IN {spec, policy}
THEN FAIL severity=ERROR  scores(loop 🝳=0.2, boundary 🝚=0.8, breach 🜬=0.7)
BECAUSE "may not" conflates prohibition (deontic) with uncertainty (epistemic)
SUGGEST
  A) If prohibition: "must not" / "is not permitted to" / "is prohibited from"
  B) If uncertainty: "might not" / "may fail to" / "it is possible that ... not"
OR ASK "Do you mean forbidden (must not) or uncertain (might not)?"
```

**Examples**
- Unstable: “Users may not export data.”
- Stable (forbidden): “Users **must not** export data.”
- Stable (uncertain): “Exports **might fail** under these conditions.”

---

## Rule 2 — MAY_DEONTIC_UNMARKED

```
RULE SLL-002 MAY_DEONTIC_UNMARKED
WHEN pattern matches /(you|users|client|caller|requester)\s+may\s+<VERB>/
AND doc_class IN {spec, policy, instructions}
THEN ALERT severity=ERROR  scores(loop 🝳=0.35, boundary 🝚=0.6, breach 🜬=0.45)
BECAUSE "may" is underspecified: permission vs capability vs intent
SUGGEST
  A) Permission: "is permitted to"
  B) Authorization: "is authorized to" (if access/control is implied)
  C) Capability: "can" (only if purely physical/technical ability)
  D) Optionality: "is not required to" / "may optionally" (only in RFC-style specs)
OR ASK "Is this permission, authorization, capability, or optional behavior?"
```

**Examples**
- Unstable: “The client may retry the request.”
- Stable (optionality): “The client **may retry** the request (optional).” *(RFC-style only)*
- Stable (recommendation): “The client **should** retry the request.” *(if recommended)*
- Stable (permission): “The client **is permitted to** retry the request.”

---

## Rule 3 — SHOULD_REASONLESS

```
RULE SLL-003 SHOULD_REASONLESS
WHEN token == "should"
AND doc_class IN {policy, instructions, spec}
AND no rationale within N=2 sentences
THEN ALERT severity=WARN  scores(loop 🝳=0.55, boundary 🝚=0.35, breach 🜬=0.2)
BECAUSE "should" without rationale hides authority and weakens compliance/consent clarity
SUGGEST
  A) If required: "must"
  B) If recommendation: "should" + add rationale: "because ..."
  C) If preference: "we recommend ..." / "ideally ..."
OR ASK "Is this a requirement (must) or a recommendation (should + because)?"
```

**Examples**
- Unstable: “Users should rotate keys.”
- Stable (requirement): “Users **must** rotate keys every 90 days.”
- Stable (recommendation): “Users **should** rotate keys every 90 days **to reduce exposure**.”

---

## Rule 4 — PASSIVE_AGENT_HIDING

```
RULE SLL-004 PASSIVE_AGENT_HIDING
WHEN pattern matches /(is|are|was|were|be|been)\s+(allowed|permitted|required|prohibited|recommended)/
AND doc_class IN {policy, spec, instructions}
AND no explicit agent/authority present nearby
THEN ALERT severity=WARN  scores(loop 🝳=0.5, boundary 🝚=0.5, breach 🜬=0.35)
BECAUSE passive voice can hide who grants permission / enforces boundary 🝚
SUGGEST
  A) Add authority: "The system permits..." / "Admins must..." / "Policy X prohibits..."
  B) If mutual consent: "Both parties agree that ..."
OR ASK "Who is the authority/agent that permits or requires this?"
```

**Examples**
- Unstable: “Access is allowed after verification.”
- Stable: “**The system permits** access after verification.”
- Stable: “**Admins may grant** access after verification.”

---

## Rule 5 — VAGUE_EVALUATIVE_TERMS

```
RULE SLL-005 VAGUE_EVALUATIVE_TERMS
WHEN token IN {"reasonable", "appropriate", "as needed", "where applicable", "best effort"}
AND doc_class IN {policy, spec, instructions}
THEN ALERT severity=WARN  scores(loop 🝳=0.6, boundary 🝚=0.45, breach 🜬=0.25)
BECAUSE vague evaluatives outsource meaning to an implicit judge; destabilizes expectations
SUGGEST
  A) Replace with measurable criteria (thresholds, time windows, roles)
  B) If truly contextual: add a decision rule (who decides + what factors)
OR ASK "What criteria determine ‘reasonable/appropriate’ here, and who decides?"
```

**Examples**
- Unstable: “Take reasonable steps to secure data.”
- Stable: “Encrypt data at rest and in transit; restrict access to approved roles; log access for 90 days.”

---

## Optional: Minimal Severity Policy

- `spec`, `policy`: treat SLL-001 and SLL-002 as **ERROR** by default.
- `instructions`: treat them as **WARN** unless safety/security relevant.
- `marketing`, `chat`: treat all as **INFO/WARN** only (no FAIL).

---

## Notes for Translation into Real Lint

- These signatures can map to:
  - **Vale** regex rules + message
  - AST-based parsing for subject/modality detection
  - LLM-only fallback for *classification* when deterministic rules match

Key principle: **deterministic trigger → probabilistic disambiguation → human choice**.

