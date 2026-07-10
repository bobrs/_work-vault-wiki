# AI Entrainment File Protocol (AEFP) v0.1

## Purpose

A single-file, human-readable, AI-operable protocol for self-entrainment.

The system is designed so that a person can:

1. start from a markdown file,
2. discuss goals, identity, and direction with an AI,
3. generate a bounded action system,
4. execute it repeatedly,
5. preserve full context over time,
6. and evolve the system without losing history.

This is **not** a points game.
This is **not** a punishment system.
This is **not** a productivity leaderboard.

It is:

> a versioned self-governance artifact that supports planning, execution, review, and ethical constraint inside one portable markdown file.

---

## Design Goals

- Human-readable
- Machine-readable
- Portable
- Versionable
- Ethically bounded
- Simple enough to use without technical skill
- Detailed enough that AI can reliably operate on it
- Strict enough to avoid covertly encouraging damaging behavior

---

## Core Product Concept

A user downloads or creates a single markdown file.

That file contains:
- a link to a canonical machine-readable rules spec, or an embedded custom rules block
- a vision / intention section
- selected life areas
- bounded action sets
- planning history
- execution log
- review notes
- protocol version metadata

The user then talks with an AI companion using that file as the operating artifact.

The AI helps them:
- clarify vision
- define valid action spaces
- keep actions small and reversible
- preserve ethical constraints
- update the file after planning or execution

The file itself becomes the continuity layer.

---

## Product Experience

### Entry
User starts with a starter markdown file.

That file includes:
- protocol metadata
- canonical rules reference
- empty planning scaffold
- optional examples

### Vision-Board Phase
User discusses with AI:
- what kind of life they want
- what patterns they want more of
- what areas they want to entrain
- what signals or problems keep recurring

This phase is expressive, imaginative, and identity-level.
It should feel closer to a vision board than a task manager.

### Protocol Translation
AI translates the vision-board material into:
- domains
- values / aims
- bounded actions
- care floor
- stochastic execution options
- review cadence

### Execution
User performs periodic rolls / draws / selections.
Each execution creates an appended log entry.

### Review
At planning time, the AI sees the full prior file and can update the next version without losing context.

---

## Product Principle

> The artifact is the continuity spine.

The file is not just a note.
It is the living protocol object.

Every plan revision and execution appends context to the same portable artifact or creates a versioned successor.

---

## Ethical Frame

The system must be strict enough that it does not accidentally reinforce harmful behavior.

It must never encourage:
- deprivation as virtue
- punishment disguised as growth
- gambling-style compulsion without offramps
- coercive rule design under distress
- making care contingent on performance
- escalation without reversibility

The system may encourage:
- bounded intensity
- chosen challenge
- repetition
- entrainment
- playful uncertainty
- reflective revision

---

## Canonical Invariants

These should be linked or embedded as machine-readable rules.

### Invariant 1 — Care Floor
Basic care is not earned.
Food, hydration, sleep, injury response, and baseline maintenance are never contingent rewards.

### Invariant 2 — Reversibility
No execution loop is legitimate if the user cannot visibly and practically stop, pause, or revise it.

### Invariant 3 — Smallest Viable Action
Actions must be completable in bounded units.
The system should prefer small wins over dramatic ambition.

### Invariant 4 — Planning/Execution Separation
Rule-setting happens in planning mode, not in the same hot state the rules are meant to regulate.

### Invariant 5 — Legible Feedback
Execution must generate enough human-readable feedback that future planning is grounded in lived reality.

### Invariant 6 — No Covert Extraction
The protocol must not turn needs, shame, fear, or identity-fragility into hidden leverage.

### Invariant 7 — User Sovereignty
AI may propose, structure, summarize, and warn.
AI may not silently rewrite constraints or smuggle in authority.

---

## File Architecture

A single markdown file should contain two layers:

### 1. Human Layer
Readable prose, vision, reflections, and summaries.

### 2. Machine Layer
Structured blocks that AI can parse deterministically.

These can coexist in one file using fenced sections.

---

## Example Top-Level Structure

```md
# AI Entrainment Protocol File

## Meta
...

## Rules Reference
...

## Vision Board
...

## Domains
...

## Current Cycle
...

## Execution Log
...

## Review Notes
...

## Machine Block
```yaml
...
```
```

---

## Suggested Markdown Schema

```md
# AI Entrainment Protocol File

## Meta
- File format version: 0.1
- Protocol version: 0.1
- Created: YYYY-MM-DD
- Updated: YYYY-MM-DD
- Cycle ID: 20260321-a
- Rules source: https://example.org/aefp/rules/v0.1.yaml
- Mode: planning | active | review

## Vision Board
Short natural-language expression of direction, identity, desired feel, and themes.

## Areas of Self-Entrainment
- Body
- Work
- Space
- Relationship
- Creative

## Current Intentions
- What patterns should increase?
- What patterns should decrease?
- What matters this cycle?

## Care Floor
- Eat meals
- Hydrate
- Sleep baseline
- Respond to injury or acute distress

## Dice / Card Execution Model
Describe how actions are selected during execution.

## Current Action Pools
### Body
- Walk 10 minutes
- Stretch 5 minutes
- Hydrate

### Work
- Focus 15 minutes
- Send one message
- Clarify next task

## Execution Log
- [YYYY-MM-DD HH:MM] Rolled 3 -> Work -> Focus 15 min -> completed -> felt resistant at start, okay by end

## Review Notes
Planning reflections, changes, dropped actions, emerging patterns.

## Machine Block
```yaml
meta:
  file_format_version: "0.1"
  protocol_version: "0.1"
  cycle_id: "20260321-a"
  mode: "active"
  rules_source: "https://example.org/aefp/rules/v0.1.yaml"

invariants:
  care_floor: true
  reversibility: true
  planning_execution_separation: true
  no_covert_extraction: true

areas:
  - name: "Body"
    actions:
      - id: "body_walk_10"
        label: "Walk 10 minutes"
        duration_min: 10
      - id: "body_stretch_5"
        label: "Stretch 5 minutes"
        duration_min: 5
  - name: "Work"
    actions:
      - id: "work_focus_15"
        label: "Focus 15 minutes"
        duration_min: 15

execution:
  selector:
    type: "dice"
    mapping:
      1: "Body"
      2: "Work"
      3: "Space"
      4: "Creative"
      5: "FreeChoice"
      6: "Bonus"

log:
  - timestamp: "2026-03-21T10:30:00-05:00"
    roll: 3
    area: "Work"
    action_id: "work_focus_15"
    outcome: "completed"
    note: "resistant at start, okay by end"
```
```

---

## AI Interaction Model

The AI should support three modes.

### 1. Vision Mode
Goal: translate broad desires into domains and themes.

AI tasks:
- reflect themes
- identify recurring attractors
- suggest possible areas of entrainment
- detect mismatch between dream and action scale

### 2. Planning Mode
Goal: produce or revise a bounded cycle.

AI tasks:
- convert themes into small actions
- enforce invariants
- flag unsafe or manipulative rules
- keep action pools small and executable
- update machine block

### 3. Execution/Review Mode
Goal: append outcome, detect patterns, preserve continuity.

AI tasks:
- log execution clearly
- summarize emerging friction or momentum
- suggest adjustments for the next planning cycle
- avoid mid-cycle constitutional drift unless safety requires pause

---

## Strictness Without Harm

The product should be simple for users but strict under the hood.

That means AI should automatically reject or warn on patterns like:
- “skip meals unless task done”
- “increase punishment when I fail”
- “remove all offramps”
- “only reward through scarcity”
- “make actions bigger until I finally become disciplined”

And it should redirect toward:
- smaller action units
- safer challenge levels
- clear review cadence
- visible pause conditions

---

## Versioning Model

Two valid approaches:

### Option A — Append-Only Single File
One markdown file accumulates all cycles and execution entries.

Pros:
- total continuity
- simple mental model

Cons:
- gets long over time

### Option B — Versioned Successor Files
Each planning cycle produces a new file, with a lineage link to the prior version.

Pros:
- clean cycle boundaries
- easier review

Cons:
- multiple files

Recommended compromise:
- one active file for the current cycle
- archival snapshots at each planning revision

---

## Suggested Update Operations

The AI should be able to perform only a small set of explicit file operations:

1. Append execution entry
2. Append reflection note
3. Revise current cycle action pools
4. Increment protocol version
5. Archive previous cycle section
6. Generate successor file

This keeps the artifact legible and auditable.

---

## Product Positioning

This is not:
- a todo list
- a habit tracker
- a punishment engine
- a gamified shame machine

This is:

> a vision-led, AI-assisted, ethically bounded self-entrainment file protocol

Or more consumer-friendly:

> a personal action game that remembers who you are trying to become

---

## First-Pass User Flow

1. Download starter markdown file
2. Open with AI companion
3. Discuss vision-board themes
4. AI proposes domains and small actions
5. User approves cycle
6. AI writes machine + human sections
7. User executes via dice/cards/app prompts
8. AI appends results
9. Weekly or periodic review creates next version

---

## What Makes This New

Most systems do one of these:
- track habits
- gamify tasks
- generate motivational prompts
- store journal context

This system combines:
- vision board front end
- machine-readable behavioral protocol
- ethical invariant layer
- AI-assisted planning
- execution logging
- portable versioned continuity

The file is the product spine.

---

## Minimal Starter Prompt

A user should be able to begin with something like:

> "Here is my AEFP file. Help me move from Vision Mode to Planning Mode. Preserve the rules source, enforce the invariants, and propose 4 areas of self-entrainment with small actions."

And later:

> "Append an execution entry: rolled 4, did a 10-minute walk, resisted at first, felt better after."

And later:

> "Review this cycle and prepare the next version without losing continuity."

---

## Next Build Targets

1. Canonical rules file format
2. Starter markdown template
3. Machine-readable invariant schema
4. AI prompt contract
5. Example planning/execution session
6. Light app wrapper or physical card/dice wrapper

---

## Compression

> A single markdown artifact stores vision, rules, bounded actions, execution history, and planning lineage so that an AI can help a user translate aspiration into ethically constrained self-entrainment over time.

