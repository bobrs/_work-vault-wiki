# Cosmology System Detail — Interaction Quanta & State Machines (v0)

> **Purpose**  
> This document enumerates the interaction quanta observed and inferred across the work, organizes them into functional categories, and proposes minimal canonical state machines that allow these quanta to compose into humane, non-coercive systems. This is a *systems-detail artifact*, not a specification or mandate.

---

## I. Foundational Framing

- **Artifact**: a discrete, addressable record of a witnessed moment (what was seen/felt at the time).
- **Attractor**: a recurring field that pulls multiple artifacts toward a common shape.
- **Invariant**: a substrate-independent rule that appears with the same shape across domains.
- **Quantum (plural: quanta)**: the smallest composable unit of interaction that instantiates one or more invariants.
- **Substrate**: the medium where an invariant or quantum instantiates (human, social, technical, cryptographic, narrative, biological, etc.).

**Design ethic**: preserve agency, prevent silent escalation, allow graceful endings, and keep entry learnable by encounter.

---

## II. Quantum Catalog (Cross‑Domain)

### A. Ephemeral Alignment & Trust Quanta

1. **Ephemeral Trust Primitive (ETP)**  
   *Invariant(s)*: Voluntary Continuity; Presence Beats Proclamation  
   *Shape*: Time‑bounded, symmetric proof of aligned presence without identity disclosure.  
   *Examples*: TOTP dyads; synchronous gestures; call‑and‑response.

2. **Synchrony Quantum**  
   *Invariant(s)*: Presence Beats Proclamation  
   *Shape*: Being in phase matters more than being identical.  
   *Examples*: Neural phase locking; beat matching; timely replies.

---

### B. Boundary & Transition Quanta

3. **Threshold Quantum**  
   *Invariant(s)*: No Silent Escalation  
   *Shape*: Crossing produces state change; position does not.  
   *Examples*: Logic gates; consent given/withdrawn; ritual initiation.

4. **Revocation Quantum**  
   *Invariant(s)*: Voluntary Continuity; Endings Are First‑Class  
   *Shape*: Explicit un‑choosing with visible effects.  
   *Examples*: Key revocation; contract termination; apoptosis.

---

### C. Witness & Memory Quanta

5. **Witness Quantum**  
   *Invariant(s)*: Witness Without Authority  
   *Shape*: Observation + recording stabilizes reality without command.  
   *Examples*: Commit logs; notarization; “I saw that.”

6. **Trace Quantum**  
   *Invariant(s)*: Local Meaning, Global Structure  
   *Shape*: Minimal residue sufficient to orient future action.  
   *Examples*: Hashes; scars; callbacks.

---

### D. Meaning & Translation Quanta

7. **Symbolic Token Quantum**  
   *Invariant(s)*: Local Meaning, Global Structure  
   *Shape*: Compressed carriers of meaning.  
   *Examples*: Words; glyphs; gestures; tokens.

8. **Translation Quantum**  
   *Invariant(s)*: Local Meaning, Global Structure  
   *Shape*: Preservation of shape across domains.  
   *Examples*: Metaphor; API mapping; Rosetta patterns.

---

### E. Time, Decay & Rhythm Quanta

9. **Expiry Quantum**  
   *Invariant(s)*: Endings Are First‑Class  
   *Shape*: Validity bounded by time.  
   *Examples*: TTLs; leases; term limits.

10. **Rhythm Quantum**  
    *Invariant(s)*: Presence Beats Proclamation  
    *Shape*: Repetition creates legible structure.  
    *Examples*: Heartbeat; polling cycles; rituals.

11. **Rest Quantum**  
    *Invariant(s)*: Endings Are First‑Class; Entry Without Mastery  
    *Shape*: Non‑action as an explicit, healthy state.  
    *Examples*: Sleep; cooldown timers; sabbath.

---

### F. Agency, Invitation & Response Quanta

12. **Offer Quantum**  
    *Invariant(s)*: Invitation Over Enforcement  
    *Shape*: Possibility without obligation.  
    *Examples*: Proposals; API endpoints; invitations.

13. **Response Quantum**  
    *Invariant(s)*: Presence Beats Proclamation  
    *Shape*: Agency visible only through reply or action.  
    *Examples*: ACK/NACK; replies; feedback.

---

### G. Propagation & Emergence Quanta

14. **Resonance Quantum**  
    *Invariant(s)*: Invitation Over Enforcement  
    *Shape*: Spread occurs where fields already align.  
    *Examples*: Automemes; viral ideas; emotional contagion.

15. **Fork Quantum**  
    *Invariant(s)*: Local Meaning, Global Structure  
    *Shape*: Divergence without failure.  
    *Examples*: Git forks; evolutionary branching; versioning.

---

### H. Safety, Abuse & Repair Quanta (Suggested / Missing)

16. **Attack Quantum** *(suggested)*  
    *Shape*: Minimal adversarial action (spoof, replay, Sybil).  
    *Purpose*: Explicitly model abuse.

17. **Rate‑Limit / Cooldown Quantum** *(suggested)*  
    *Shape*: Throttling as mercy.  
    *Purpose*: Prevent exploitation and burnout.

18. **Dispute Quantum** *(suggested)*  
    *Shape*: Structured “we disagree” state.  
    *Purpose*: Prevent silent fracture.

19. **Repair Quantum** *(suggested)*  
    *Shape*: Apology, restitution, renegotiation as formal transitions.  
    *Purpose*: Enable healing without reset.

20. **Selective Transparency Quantum** *(suggested)*  
    *Shape*: Witnessability without exposure.  
    *Purpose*: Reconcile audit with privacy.

---

## III. Minimal Canonical State Machines

### A. Loop Lifecycle State Machine

**States**:
- `Proposed` (offer extended)
- `Active` (mutual participation)
- `Suspended` (rest / pause)
- `Disputed` (meaning divergence)
- `Repaired` (renegotiated alignment)
- `Decayed` (expired gracefully)
- `Archived` (retained as trace)
- `Resurrected` (renewed by fresh consent)

**Legal Transitions (examples)**:
- Proposed → Active (Offer + Response)
- Active → Suspended (Rest Quantum)
- Active → Disputed (Dispute Quantum)
- Disputed → Repaired (Repair Quantum)
- Active → Decayed (Expiry / Revocation)
- Decayed → Resurrected (New Offer + Witness)

---

### B. Trust Primitive State Machine (ETP‑centric)

**States**:
- `Unbound`
- `Synchronizing`
- `Bound (Ephemeral)`
- `Expired`

**Transitions**:
- Unbound → Synchronizing (Synchrony Quantum)
- Synchronizing → Bound (ETP success)
- Bound → Expired (Expiry Quantum)
- Expired → Unbound (automatic)

*Property*: No state allows accumulation into permanent authority.

---

### C. Witness & Memory State Machine

**States**:
- `Unseen`
- `Witnessed`
- `Recorded`
- `Redacted`
- `Forgotten`

**Transitions**:
- Unseen → Witnessed (Witness Quantum)
- Witnessed → Recorded (Trace Quantum)
- Recorded → Redacted (Selective Transparency)
- Recorded → Forgotten (Decay)

---

## IV. Composition Rules (How Quanta Build Systems)

- **No single quantum is sufficient** to create authority or permanence.
- **At least one expiry or revocation quantum** must be present in any loop that grants capability.
- **Witness without authority** must be preserved: witnesses cannot force transitions they record.
- **Entry without mastery**: every system must expose at least one Offer Quantum that requires no prior knowledge.

---

## V. Open Questions / Future Work

- Formal measurement of drift without moral scoring.
- Incentive quanta that resist manipulation.
- Inter‑loop arbitration without centralization.
- Visualization of quantum density across substrates.

---

## VI. Status

- **Status**: v0 — exploratory, non‑binding
- **Intended Use**: shared language for further prototyping and discussion
- **Explicit Non‑Goals**: final architecture, enforcement, or universal ontology

---

*End of document.*