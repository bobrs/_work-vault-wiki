---
catalog: "Free Training Catalog"
training_id: "007"
title: "Survivable Workflows"
subtitle: "How to make processes reconstructable without over-documenting"
track: "Core Practices"
estimated_time: "20–30 minutes"
audience:
  - Operators
  - Product
  - IT / Security
  - Compliance
  - AI teams
learning_outcomes:
  - Identify workflows that are fragile vs survivable
  - Learn how to make processes reconstructable without bureaucracy
  - Reduce key-person dependency in operations
prerequisites: "Training 001–006 recommended"
level: "Introductory"
license: "Free / Open Training"
version: "1.0"
last_updated: "2025-12-18"
---

# Survivable Workflows
## How to make processes reconstructable without over-documenting

> **Training 007 · Core Practices**  
> **Time:** 20–30 minutes

---

## Core stance
A workflow is survivable if someone else can run it correctly **without asking the original operator**.

Most workflows don’t fail because they are undocumented.  
They fail because **they are not reconstructable**.

---

## Why this lesson exists
Organizations often rely on workflows that:
- Live in people’s heads
- Depend on timing, intuition, or “knowing who to ask”
- Break during vacations, turnover, or stress
- Are re-learned repeatedly

Traditional documentation attempts to fix this by writing *everything*.  
That usually fails.

This lesson focuses on **minimum-viable survivability**, not exhaustive process capture.

---

## What makes a workflow fragile
A workflow is fragile when:
- One person knows the sequence
- Exceptions aren’t explained
- Recovery steps are tribal knowledge
- Outputs are checked implicitly, not explicitly

Early warning signs:
- “It’s faster if I just do it”
- “I’ll explain it when something breaks”
- “There’s a trick to this part”

---

## What makes a workflow survivable
A workflow is survivable when:
- Its purpose is clear
- The critical steps are visible
- Failure modes are named
- Hand-off points are explicit

Survivability is about **orientation**, not precision.

---

## The survivable workflow pattern
A survivable workflow can often be captured on **one page**.

It answers five questions:

1. **What is this workflow for?**  
   (Purpose / outcome)

2. **When does it start and end?**  
   (Boundaries)

3. **What are the critical steps?**  
   (Not every step—only the ones that matter)

4. **What commonly goes wrong?**  
   (Known failure modes)

5. **How do we know it worked?**  
   (Verification signal)

That’s enough for continuity.

---

## What not to do
Avoid:
- Step-by-step micromanuals
- Screenshots of every click
- Edge cases without prioritization
- “Just follow these 47 steps”

Those age poorly and aren’t trusted under pressure.

---

## Survivable workflows and AI
When workflows are implicit:
- AI automates the wrong parts
- Exceptions get flattened
- Human judgment is lost

When workflows are survivable:
- AI can be safely inserted
- Boundaries are clear
- Escalation paths exist

Survivability is a prerequisite for safe automation.

---

## Exercises

### Drill 1 — Workflow Survivability Test
Pick one recurring workflow.

Ask:
- Could someone else run this tomorrow?
- Could they recover if it failed?
- Could they explain why each step exists?

Any “no” indicates fragility.

---

### Drill 2 — One-Page Workflow Card
Create a one-page workflow artifact answering the five questions above.

Stop after one page.

---

### Drill 3 — Replace a Person Dependency
Identify one workflow step that depends on a specific person.

Replace it with:
- A checkpoint
- A decision rule
- A documented exception

---

## FAQ

**Isn’t this just SOP documentation?**  
No. SOPs optimize consistency. Survivable workflows optimize reconstructability under change.

**Won’t this slow things down?**  
No. It reduces interruption and emergency explanation.

**Who owns workflows?**  
Operators own execution. Continuity ensures survivability.

---

## Suggested next step
Pick **one fragile workflow**.  
Make it survivable—not perfect.

That’s how continuity enters operations.

---

> **Next:** Training 008 — *Drift Detection*  
> How policies, workflows, and systems quietly rot—and how to notice early.
