# OSF Preregistration
## Title
**Consent as a Cross-Substrate Invariant: Measuring Re-key Costs and Influence Radius in Multi-Agent Systems**

---

## 1. Research Question
Do consent boundaries function as a cross-substrate invariant that constrains which interactions are allowed to close loops between agents, and are consent updates disproportionately costly because they require re-keying shared reality?

---

## 2. Theoretical Background
Across domains (brains, norms, law, cryptography, protocol, culture, machines), agents coordinate via repeated interactions that update shared state. We propose that **consent** can be modeled as an admissibility constraint on loop closure events. When consent changes (grant, withdrawal, narrowing, revocation), systems must re-key shared expectations, permissions, and access patterns. This re-keying is hypothesized to be the primary driver of the observed coordination cost associated with consent change.

---

## 3. Hypotheses

### H1 (Invariant Role Hypothesis)
In multi-agent systems with shared mutable state, there exists a consent-like variable that partitions interactions into admissible vs inadmissible loop closures. Violations of this boundary will produce measurable coherence or coordination costs.

### H2 (Re-key Cost Hypothesis)
Consent updates incur disproportionately higher coordination costs than routine interactions because they re-key shared reality.

### H3 (Scaling Hypothesis)
The cost of a consent update scales with the **influence radius** (the number and strength of dependent shared states affected by the update).

### H4 (Design Mitigation Hypothesis)
Systems designed to minimize influence radius will exhibit lower Revocation Cost Ratios (RCR) without increasing the rate of consent violations.

---

## 4. Operational Definitions

- **Agent:** An entity whose internal state predicts its future actions better than external observation alone.
- **Loop Closure:** An interaction that results in a mutual state update between agents.
- **Consent State:** The current set of admissible interaction types or scopes for an agent.
- **Consent Update:** Any modification to the consent state (grant, withdraw, narrow, revoke).
- **Influence Radius:** The number of dependent shared states (permissions, expectations, data, roles) affected by a consent update.
- **Coordination Cost:** Measured time, communication overhead, computational work, or number of state changes required to restore system stability.
- **Revocation Cost Ratio (RCR):**
  
  RCR = (Cost of consent update) / (Median cost of routine interaction)

---

## 5. Study Design

### 5.1 Substrate Focus
Primary empirical focus will be on **protocol and cryptographic coordination systems**, where consent boundaries can be precisely instrumented.

### 5.2 Experimental Conditions
Two simulated or implemented systems will be compared:

- **Localized-Consent System (LCS):** Scoped permissions, short-lived capabilities, local revocation, compartmentalized state.
- **Global-Consent System (GCS):** Broad permissions, long-lived keys, centralized policy, global invalidation on revocation.

Both systems will support identical interaction workloads.

---

## 6. Data Collection

For each system, we will measure:

- Cost of routine interactions
- Cost of consent updates (revocations)
- Revocation Cost Ratio (RCR)
- Influence radius per consent update
- Time to restore admissible interaction state after revocation
- Rate of continued inadmissible interactions post-withdrawal (violation persistence)

Data will be collected via instrumentation of the simulation or protocol logs.

---

## 7. Analysis Plan

- Compare mean and distributional RCR between LCS and GCS systems.
- Test correlation between influence radius and coordination cost.
- Evaluate whether reductions in RCR are associated with increases in violation rates.
- Use non-parametric tests where distributional assumptions are violated.

---

## 8. Criteria for Falsification

The hypotheses will be considered falsified if:

- Consent updates do not exhibit higher coordination cost than routine interactions.
- Coordination cost does not scale with influence radius.
- Systems with reduced influence radius show higher violation persistence or instability.
- No consent-like admissibility variable can be identified in the studied systems.

---

## 9. Scope Conditions and Limitations

This preregistration applies to systems with:

- Distinct semi-autonomous agents
- Repeated interactions
- Shared mutable state

The claims do not extend to purely agentless or fully deterministic physical systems.

---

## 10. Transparency and Deviations

All deviations from this preregistered plan will be explicitly documented and justified in subsequent reporting. All analysis code and synthetic data (where applicable) will be made publicly available.

---

## 11. Summary
This preregistration formalizes a testable claim that consent functions as a cross-substrate invariant governing admissible loop closures, and that the cost of consent change arises from re-keying shared reality. The Revocation Cost Ratio provides a falsifiable quantitative handle on this claim.

