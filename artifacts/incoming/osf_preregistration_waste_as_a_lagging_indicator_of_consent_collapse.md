# OSF Preregistration

## Title

**Waste as a Lagging Indicator of Unnoticed Consent Collapse**

---

## 1. Research Question

Does the accumulation of waste in complex systems function as a *lagging indicator* of prior, unnoticed collapse in consent mechanisms?

More specifically:
- Do measurable failures in micro-consent (local, time-bound, context-sensitive gating of interaction) *precede* increases in measurable waste?
- Can consent collapse be detected early enough to predict and reduce future waste?

---

## 2. Theoretical Background and Rationale

Across biological, social, and technical systems, intelligence and sustainability depend on regulated interaction. Consent is operationalized here as the mechanism by which systems permit, modulate, or refuse interaction.

When consent mechanisms fail silently—through coercion, bypass, overload, ambiguity, latency, or capture—systems continue interacting past optimal boundaries. This misaligned continuation is hypothesized to produce downstream waste, including material waste, energetic inefficiency, coordination overhead, informational overload, and relational breakdown.

This study reframes waste not primarily as inefficiency or excess, but as the delayed manifestation of suppressed or unacknowledged refusal (“no”).

---

## 3. Hypotheses

**H1 (Temporal precedence):** Indicators of consent collapse will statistically precede indicators of waste, with a measurable lag.

**H2 (Magnitude relationship):** The degree of consent collapse will positively predict the magnitude of subsequent waste.

**H3 (Incremental prediction):** Consent-collapse indicators will improve prediction of waste beyond baseline models using only volume, demand, or growth metrics.

**H4 (Intervention sensitivity, exploratory):** Systems with stronger micro-consent affordances will exhibit lower waste for comparable levels of interaction.

---

## 4. Operational Definitions

### 4.1 Consent

Consent is defined as a system’s capacity to represent, communicate, and enact refusal or modulation of interaction locally and reversibly.

### 4.2 Consent Collapse

Consent collapse refers to failure modes in which refusal signals are suppressed, delayed, or rendered ineffective. These include:
- Bypass
- Coercion
- Overwhelm
- Ambiguity
- Latency
- Capture

A **Consent Collapse Index (CCI)** will be constructed as a composite of leading indicators (see Measures).

### 4.3 Waste

Waste is defined as downstream cost incurred due to misaligned or unwanted continuation of interaction. Categories include:
- Material waste
- Energetic waste (rework, inefficiency)
- Informational waste
- Coordination waste
- Relational waste

A **Waste Index (WI)** will be constructed as a composite of lagging indicators.

---

## 5. Study Design

This preregistration covers an observational, multi-domain, longitudinal analysis using existing datasets.

The primary design is lead–lag analysis of consent-collapse indicators and waste indicators over time within the same systems.

---

## 6. Data Sources

Candidate datasets will be drawn from at least two of the following domains (final selection prior to analysis):
- Software development organizations
- Customer service or operations workflows
- Supply chain or inventory systems
- Administrative or civic process datasets

Only datasets with time-indexed records of both consent-related signals and waste-related outcomes will be included.

---

## 7. Measures

### 7.1 Consent Collapse Indicators (Leading)

Examples include:
- Cost or friction to refuse or opt out
- Override or escalation rates
- Ignored or delayed feedback signals
- Exit or churn precursors
- Boundary-breach events

These will be standardized and combined into the Consent Collapse Index (CCI).

### 7.2 Waste Indicators (Lagging)

Examples include:
- Rework or defect rates
- Returns, spoilage, or disposal costs
- Unused output (features, reports, inventory)
- Coordination overhead (meetings, queueing)
- Attrition or burnout proxies

These will be standardized and combined into the Waste Index (WI).

---

## 8. Analysis Plan

### 8.1 Temporal Analysis

- Cross-correlation and distributed lag models will be used to assess whether changes in CCI precede changes in WI.
- Granger causality tests will be applied where assumptions are met.

### 8.2 Predictive Models

- Baseline models predicting WI from volume and demand variables will be compared against models including CCI.
- Improvement will be evaluated using out-of-sample prediction error.

### 8.3 Robustness Checks

- Sensitivity analyses with alternative index constructions
- Domain-specific subgroup analyses

---

## 9. Criteria for Inference

Support for the primary claim will be inferred if:
- CCI significantly precedes WI across multiple systems or domains, and
- The inclusion of CCI materially improves prediction of WI.

Failure to observe these patterns will be treated as evidence against the hypothesis.

---

## 10. Data Exclusion and Missingness

Data will be excluded only for:
- Missing timestamps
- Inability to align consent and waste measures temporally

Missing data will be handled using domain-appropriate imputation methods, preregistered prior to execution.

---

## 11. Ethical Considerations

This study uses de-identified, aggregate, or organizational-level data where possible.

Consent-related signals will not be used to evaluate or penalize individuals. The focus is on system-level dynamics, not personal compliance.

---

## 12. Deviations from Preregistration

Any deviations from this preregistration will be transparently documented and justified in subsequent reports.

---

## 13. Summary

This preregistration tests the claim that waste is not merely inefficiency, but the delayed signal of consent failure. By examining consent collapse as a leading indicator, the study aims to shift sustainability and systems design toward earlier, gentler, and more intelligent intervention points.

