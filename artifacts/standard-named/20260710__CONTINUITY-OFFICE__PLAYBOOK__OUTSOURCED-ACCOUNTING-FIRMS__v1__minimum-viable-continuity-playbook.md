# Minimum Viable Continuity Playbook
## Outsourced Accounting Firms (AI‑Capable Edition)

> **Continuity is the capability to preserve intent, consent, and legibility through change—without turning the firm into a bureaucracy.**

Outsourced accounting firms sit at the highest‑risk intersection of:
- multi‑tenant client data
- regulated financial workflows
- historical exceptions
- human + AI collaboration

This playbook defines the **minimum viable structures** required to safely operate AI across clients, providers, and time.

---

## 0. Firm Scope Boundary

**Declare what this playbook governs.**

Applies to:
- All client financial data
- All AI‑assisted analysis, summaries, classifications, or recommendations
- All external tools or providers touching client books

Explicitly excludes:
- Personal productivity tools with no client data
- One‑off experiments *until promoted*

> This prevents accidental cross‑client leakage and shadow‑AI production use.

---

## 1. Client‑Bound Intent Registry (CBIR)

**Purpose:** Make *why* work is performed legible per client.

Each client has **explicit intents**, not just services.

Minimum fields per intent:
- Client ID
- Intent ID
- Plain‑language purpose
- Authorized outputs
- Prohibited uses
- Regulatory sensitivity (tax, payroll, audit‑adjacent, advisory)

Example:
```
Client: ACME Co
INT‑FIN‑MONTHLY‑001
Purpose: Monthly management P&L summary
Authorized: Internal advisory conversations
Prohibited: Tax filing, lender reporting
Sensitivity: Medium
```

> Same data, different intent ≠ same permission.

---

## 2. Client Data Domain Map (CDDM)

**Purpose:** Prevent semantic bleed across clients and contexts.

Core accounting domains (minimum):
- General Ledger
- Revenue
- Expenses
- Payroll
- Taxes
- Forecasts / Projections

For each domain:
- System of record
- Client‑specific semantics
- Known ambiguities
- Allowed AI operations

Example:
```
Domain: Revenue
Client nuance: Deferred revenue tracked manually
Ambiguity: Cash vs accrual views diverge
```

> Declare disagreement early so AI doesn’t invent agreement.

---

## 3. AI Client Isolation Matrix (ACIM)

**Purpose:** Ensure AI never crosses client boundaries.

For each AI system or model:
- Client isolation method (hard / soft / none)
- Data domains accessible
- Allowed operations
- Retention policy
- Logging requirement

Example:
```
Model: GPT‑4.1
Client scope: Single‑client sessions only
Access: Read‑only financial summaries
Retention: Disabled
Logging: Required
```

> Multi‑client context windows are a **hard stop** unless explicitly engineered.

---

## 4. Provider & Tool Continuity Declaration

**Purpose:** Extend continuity beyond your firm.

Every tool or provider touching client data must declare:
- Data received
- Transformations performed
- AI usage (model + purpose)
- Artifacts returned
- Treatment of derived data

This includes:
- OCR / receipt tools
- Categorization software
- Forecasting platforms
- Offshore bookkeeping teams

> If they touch client books, they are inside your continuity boundary.

---

## 5. Advisory vs Bookkeeping Boundary Rule

**Purpose:** Prevent AI from silently crossing regulatory or liability lines.

Minimum rule:
- Bookkeeping AI: classify, summarize, reconcile
- Advisory AI: scenario analysis, explanations, options
- Tax / audit decisions: **human‑only unless explicitly approved**

Each AI output must be tagged:
- Informational
- Advisory
- Decision‑support

> This protects both licenses and trust.

---

## 6. Decision Trace Chain (Lightweight)

**Purpose:** Preserve explainability without audits.

Any AI‑assisted client‑impacting output must be traceable to:
- Client ID
- Intent ID
- Data domain(s)
- Model + version
- Human sponsor

No narrative required. Just a chain.

---

## 7. Experiment → Client‑Facing Promotion Gate

**Purpose:** Stop “we tested this once” from becoming firm infrastructure.

Promotion required when an AI tool becomes:
- recurring
- client‑visible
- relied upon for accuracy or speed

Promotion checklist:
- Assigned client intent(s)
- Data domain mapping
- AI isolation confirmation
- Sponsor named

> This is where most accounting firms silently fail today.

---

## 8. Continuity Steward (Fractional)

**Purpose:** Make continuity owned, not heroic.

Role:
- 2–4 hours/week
- Maintains registries
- Reviews promotions
- Resolves semantic disputes
- Has veto power on unsafe AI use

This is **stewardship**, not compliance.

---

## 9. The Client Safety Question

Every AI‑affected workflow must answer:

> **“Could this output accidentally affect the wrong client, filing, or financial decision?”**

If yes → continuity gap.

---

## What This Enables

- Safe AI‑augmented bookkeeping
- Scalable advisory services
- Defensible AI use
- Client trust at scale
- Future regulatory readiness without retrofitting

---

**Bottom line:**

> AI doesn’t reduce responsibility in outsourced accounting.
> It concentrates it.

Continuity is how you hold that responsibility without breaking the firm.

