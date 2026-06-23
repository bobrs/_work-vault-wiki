---
catalog: "Free Training Catalog"
training_id: "006"
title: "Decision Provenance"
subtitle: "The smallest unit of continuity"
track: "Core Practices"
estimated_time: "15–25 minutes"
audience:
  - Executives
  - Founders
  - Operators
  - IT / Security
  - Compliance
  - Product
  - AI teams
learning_outcomes:
  - Understand why decisions decay faster than systems
  - Learn how to capture decision provenance without bureaucracy
  - Apply decision records to human and AI-mediated decisions
prerequisites: "Training 001–005 recommended"
level: "Introductory"
license: "Free / Open Training"
version: "1.0"
last_updated: "2025-12-18"
---

# Decision Provenance
## The smallest unit of continuity

> **Training 006 · Core Practices**  
> **Time:** 15–25 minutes

---

## Core stance
Most continuity failures begin with a lost decision.

Systems don’t usually break first.  
**The understanding of why they exist does.**

Decision provenance is the practice of preserving *just enough* information about a decision so it remains intelligible, defensible, and revisitable over time.

---

## Why this lesson exists
Organizations often preserve:
- Code
- Policies
- Configurations
- Outputs

But they lose:
- Why a decision was made
- What alternatives were rejected
- What assumptions were true at the time
- What would justify changing course

When that happens:
- Reversal feels risky
- Change slows down
- AI trains on outcomes without intent
- Accountability becomes fuzzy

Decision provenance fixes this at the smallest possible scale.

---

## What decision provenance is (and is not)

### Decision provenance **is**
- Lightweight
- Context-preserving
- Attached to real work
- Designed for future readers
- Explicit about tradeoffs

### Decision provenance **is not**
- A meeting summary
- A justification memo
- A compliance artifact
- A post-hoc explanation
- A performance review

> Provenance exists to preserve *meaning*, not to defend egos.

---

## Why decisions decay faster than systems
Systems enforce decisions automatically.  
Humans remember decisions selectively.

Over time:
- Context disappears
- Assumptions change
- Constraints lift
- People leave

Without provenance, the system keeps enforcing yesterday’s intent—whether or not it still applies.

---

## The minimum viable decision record
A continuity-safe decision record answers **four questions**:

1. **What did we decide?**  
   (Be concrete.)

2. **Why did we decide it?**  
   (What problem were we solving?)

3. **What tradeoffs did we accept?**  
   (What did we knowingly give up?)

4. **What would trigger a revisit?**  
   (Conditions, not dates.)

That’s it.

If you capture only these four things, continuity improves immediately.

---

## Example (good)
> **Decision:** We will centralize customer audit logs in System X.  
> **Why:** Current logs are fragmented and fail audits.  
> **Tradeoffs:** Increased vendor dependency; slower access for engineering.  
> **Revisit if:** Audit scope changes or vendor pricing exceeds threshold Y.

Readable in 18 months. Reversible in principle.

---

## Example (bad)
> “We decided to move logs to X after the Q3 meeting.”

No why. No tradeoffs. No revisit logic.  
Continuity failure baked in.

---

## Where decision records should live
Decision provenance works best when **attached to the work**, not stored in a separate system.

Good locations:
- Architecture decision records (ADRs)
- Tickets or epics
- Policy sections
- Config repositories
- AI system manifests

Bad locations:
- Personal notes
- Slide decks
- Chat threads
- “Someone’s memory”

---

## Decision provenance and AI
AI systems:
- Act on historical decisions
- Generalize past intent
- Scale impact rapidly

Without decision provenance:
- AI amplifies outdated assumptions
- Consent boundaries blur
- Accountability dissolves

With provenance:
- AI mandates are explicit
- Review thresholds are clear
- Failures are explainable

Decision provenance becomes **AI governance without bureaucracy**.

---

## When to require decision provenance
Not every decision needs a record.

Require provenance when a decision is:
- High-impact
- Hard to reverse
- Automated
- Long-lived
- Compliance-relevant
- Delegated to a system or AI

Low-stakes, reversible decisions don’t need overhead.

---

## Common resistance (and how to address it)

**“This will slow us down.”**  
→ A 5–10 minute record prevents weeks of relearning later.

**“We’ll remember why.”**  
→ You won’t. And future you definitely won’t.

**“This is just more documentation.”**  
→ No. This is intent preservation, not instruction writing.

---

## Exercises

### Drill 1 — One Real Decision
Pick a decision from the last 30 days that will still matter in 6 months.

Write a four-line decision record using:
- What
- Why
- Tradeoffs
- Revisit triggers

Stop at four lines.

---

### Drill 2 — Find a Decision Without Provenance
Identify one system, policy, or automation where:
- The decision exists
- The rationale does not

Capture provenance retroactively—briefly and honestly.

---

### Drill 3 — Provenance Gate
Choose one workflow (e.g., production changes, AI deployment).

Define:
> “Decisions of type X require provenance.”

That single rule creates continuity at scale.

---

## FAQ

**Is this the same as ADRs?**  
ADRs are one implementation. Decision provenance is broader and applies beyond architecture.

**Who owns decision records?**  
The decision owner—not documentation teams.

**Can provenance be wrong?**  
Yes. That’s why revisit triggers matter more than certainty.

---

## Suggested next step
Pick **one decision-making area** (product, security, AI, compliance).  
Introduce a **four-question decision record**.

You’ve just installed the smallest, most powerful continuity primitive.

---

> **Preview:** Training 007 — *Survivable Workflows*  
> How to make processes reconstructable without over-documenting.
