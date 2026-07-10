# Finance Semantic System — Starter Guide (v0.1)

## Status
Introductory guide for practitioners.

---

# 1. Why this exists

Finance already *looks* structured:
- ledgers
- reports
- reconciliations

But the **language inside finance is not machine-reliable**.

Example:
> EBITDA increased by 12%

Questions a machine cannot safely answer:
- Which EBITDA?
- What exclusions?
- Which policy version?
- Which entity?

Humans resolve this implicitly.
Machines guess.

That gap is why AI adoption in finance lags.

---

# 2. Why machine-readable meaning matters

Most AI systems today operate on:
> patterns in language

But finance requires:
> **binding between language and reality**

Without machine-readable meaning:
- AI hallucinations look plausible
- auditability breaks
- numbers lose trust

With machine-readable meaning:
- AI becomes deterministic
- outputs are explainable
- audits become traceable
- systems interoperate cleanly

---

# 3. The core problem

Finance terms are often:
- reused
- overloaded
- context-dependent

Example:

"Revenue" may differ by:
- GAAP vs management
- entity vs consolidated
- time recognition

This creates a hidden failure mode:

> **same word, different reality**

---

# 4. The solution: explicit semantic grounding

Instead of assuming meaning, we **bind meaning explicitly**.

Example:

```text
{Revenue@GAAP}
```

This means:
- this is not just a word
- it is a reference to a defined object

---

# 5. The three-layer system

The system has three core components:

## FSGF — Grounding Framework
Defines what a term *means*

## FSP — Parser
Detects and structures semantic references

## SRE — Resolution Engine
Keeps meaning valid at runtime

---

# 6. Mental model

- FSGF = dictionary + rules
- FSP = reader
- SRE = interpreter + safety system

---

# 7. Notation (how you write it)

### Grounded term
```text
{EBITDA}
```
Means: resolve this term

### With context
```text
{Revenue@GAAP}
```

### With version or policy
```text
{EBITDA@Board#V3}
```

---

### Ambiguous term
```text
[EBITDA]
```
Meaning unclear or intentionally unbound

### Proposed term
```text
<Adjusted EBITDA>
```
Draft definition

### Narrative term
```text
(core profitability)
```
Not authoritative

---

# 8. What happens under the hood

## Step 1 — Parsing

Input:
```text
{EBITDA@Board}
```

FSP converts it into:
- term = EBITDA
- context = Board
- status = grounded

---

## Step 2 — Resolution

SRE:
- finds canonical definition
- checks policy
- checks freshness
- checks lineage

---

## Step 3 — Decision

SRE returns:
- proceed
- warn
- pause
- reject

---

## Step 4 — Execution / AI use

AI receives:
- definition
- exclusions
- allowed actions

So it does not guess meaning.

---

# 9. Example: without system

```text
EBITDA increased 12%
```

Problems:
- ambiguous
- not auditable
- not reproducible

---

# 10. Example: with system

```text
{EBITDA@Board#V3} increased 12%
```

Now:
- definition is known
- exclusions are known
- lineage is traceable
- AI can reason safely

---

# 11. Real-world usage examples

## Board report

```text
{Revenue@GAAP} grew 8% while {EBITDA@Board} declined due to restructuring costs.
```

## Analysis

```text
Compare {FreeCashFlow@Mgmt} to [Free Cash Flow] reported last quarter.
```

## Drafting

```text
<Normalized EBITDA> may exclude one-time litigation costs.
```

## Narrative explanation

```text
(core profitability) improved despite lower revenue growth.
```

---

# 12. Why this changes AI adoption

Without grounding:
- AI guesses meaning
- finance rejects it

With grounding:
- AI operates on defined objects
- outputs are auditable
- trust increases

Result:
> AI becomes safer than manual interpretation

---

# 13. Why this feels “expensive”

Because the system must:
- track context
- detect drift
- maintain meaning
- revalidate continuously

But this cost replaces:
- audit failures
- misinterpretation
- semantic drift

---

# 14. What you actually get

- consistent terminology
- cross-system alignment
- AI-safe workflows
- audit-ready reasoning
- reduced ambiguity

---

# 15. Minimal adoption path

Start small:

1. Define 20–50 key terms
2. Use `{}` in one report (e.g. board deck)
3. Map those terms to definitions
4. Let AI reference them

---

# 16. Key rules

- Do not assume meaning
- Use `{}` for anything important
- Use `[]` when unsure
- Never upgrade ambiguity silently

---

# 17. Final takeaway

This system does one thing:

> It turns financial language into something machines can understand without guessing.

And that is the missing step that allows AI to safely operate in finance.

---

## Anchor note
This guide is intentionally simple. It introduces the system without requiring full technical depth. It should evolve alongside FSGF, FSP, and SRE as the system matures.

