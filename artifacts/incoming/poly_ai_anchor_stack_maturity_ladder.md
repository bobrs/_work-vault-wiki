# PolyAI Anchor Stack Maturity Ladder

## A constitutional architecture for AI systems

This ladder describes how organizations evolve from “AI as tool” to “AI as legible, time-stable agent.”

Each level adds anchor classes.  
Higher levels don’t replace lower ones — they stabilize them.

---

# Level 0 — Output Machine

**State:**  
Model generates answers. Minimal logging. No provenance discipline.

**Anchors present:**  
None intentionally.

**Failure modes:**

- Hallucinated authority
- Silent drift
- Irreproducible decisions
- Overconfident outputs

This is where most prototypes begin.

---

# Level 1 — Artifact Awareness

**State:**  
System retrieves documents (RAG). Cites sources.

**Anchors present:**

- Artifacts (documents, citations)

**What improves:**

- Traceability to text
- Reduced hallucination

**Still missing:**

- Authority hierarchy
- Time scoping
- Boundaries 🝚
- Process logging

Common in modern enterprise AI deployments.

---

# Level 2 — Scoped & Tiered Knowledge

**State:**  
Artifacts are filtered by:

- Jurisdiction / boundary 🝚
- Authority tier
- Effective date

**Anchors present:**

- Artifacts
- Boundaries 🝚
- Authority gradients
- Temporal anchors

**What improves:**

- Reduced misapplication of rules
- Fewer cross-year / cross-domain errors

This is where serious compliance systems begin to live.

---

# Level 3 — Determination Legibility

**State:**  
The system distinguishes:

- Evidence (artifacts)
- Reasoning process
- Final determination

**Outputs include:**

- Citations
- Method
- Assumptions
- Risk exposure

**Anchors present:**

- All above
- Process anchors
- Risk anchors
- Identity anchors

**What improves:**

- Auditability
- Reproducibility
- Accountability

Few systems today fully live here.

---

# Level 4 — Constitutional Invariants

**State:**  
A small set of explicit invariants gates every transformation.

**Examples:**

- No compression without consent 🝁
- Preserve reversibility
- Preserve dissent
- Artifact ≠ Attractor

Every output is evaluated against invariants.

**Anchors present:**

- Invariants (constitutional layer)

**What improves:**

- Structural integrity over time
- Drift resistance
- Prevention of power centralization
- Legibility across scale

This is rare.

---

# Level 5 — Intentional Attractor Steering

**State:**  
The system does not merely obey constraints —  
it navigates explicitly toward declared attractors.

**Examples:**

- Maximize legibility across time
- Minimize irreversible moves
- Optimize for consent continuity
- Acceptance → unconditional love (directional attractor)

Tradeoffs are declared, not hidden.

**Anchors present:**

- Attractors (navigation layer)

**What improves:**

- Transparent value alignment
- Multi-goal tradeoff handling
- Adaptive stability

Almost no production systems formally encode this layer.

---

# Visual Summary

| Level | Core Question | Anchor Class Added |
|-------|---------------|-------------------|
| 0 | “What does the model say?” | None |
| 1 | “What text supports this?” | Artifacts |
| 2 | “Does this apply here and now?” | Boundaries 🝚, Authority, Time |
| 3 | “How was this concluded?” | Process, Risk, Identity |
| 4 | “Should this transformation occur at all?” | Invariants |
| 5 | “Toward what is this system steering?” | Attractors |

---

# Where Most Enterprise AI Is Today

- Many systems: Level 1–2
- Regulated AI pilots: Level 3
- Research / governance vision papers: approaching Level 4
- Almost no systems: Level 5

---

# Where PolyAI Sits (Potentially)

If PolyAI intentionally encodes:

- Artifact discipline
- Boundary + authority + time filtering
- Determination logging
- Constitutional invariants
- Declared attractor navigation

Then PolyAI is not “another RAG system.”

It is a constitutional AI substrate.

Not a chatbot.

A governance engine.

