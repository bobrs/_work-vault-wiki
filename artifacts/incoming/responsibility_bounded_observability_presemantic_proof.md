# Responsibility-Bounded Observability (Presemantic Proof)

> This is not a semantic claim, an ethical preference, or a governance policy.
> It is a **structural invariant** required for any multi-agent system where action, information, and consequence coexist.

---

## 0. Substrate assumptions (below language)

Assume only:

1. **World state** \(W\) evolves over time.
2. **Agents** \(A_i\) take actions that causally affect future states.
3. **Signals** exist: partial functions of world state available to agents.

No morality. No law. No words.

---

## 1. Two primitives

### Observability (information access)
An agent \(A\) observes variable \(X\) if it receives a signal \(S\) such that:

\[
I(X; S \mid A) > 0
\]

Observation is defined purely as **uncertainty reduction**.

---

### Responsibility (control + stake)
An agent \(A\) is responsible for outcome \(Y\) if:

- **Control**: \(\partial Y / \partial a_A \neq 0\)
- **Stake**: \(\partial U_A / \partial Y \neq 0\)

Responsibility = *ability to influence* + *exposure to consequence*.

---

## 2. The invariant

Define the **responsibility domain** \(R_A\): the set of outcomes an agent both influences and bears cost/credit for.

> **Responsibility-bounded observability** requires:

\[
\text{Obs}(A) \subseteq \sigma(R_A)
\]

Meaning: an agent may only observe what is functionally downstream of what it is responsible for.

---

## 3. Impossibility result I: unbounded observability

Assume the negation:

- Agent \(A\) observes variable \(X\)
- \(X \notin R_A\)

So:
\[
I(X; S_A) > 0 \quad \text{and} \quad X \notin R_A
\]

### Lemma 1: Information advantage

In any partially observable environment, additional information expands achievable control policies and expected utility.

Observation strictly increases potential advantage.

---

### Lemma 2: Externalities amplify

If information can be extracted without bearing the cost of its use or misuse, competitive dynamics push toward **maximal extraction**.

This is an externality. Externalities scale.

---

### Lemma 3: Observation converts to control

Observation enables:
- prediction
- selection
- bargaining advantage
- strategic manipulation

Information asymmetry becomes **causal leverage**.

---

### Conclusion

Unbounded observability admits a stable attractor:

> **Extractive observation → asymmetry → pooled power**

This is not a moral failure.
It is a dynamical inevitability.

---

## 4. Impossibility result II: responsibility without observability

Assume:
- Agent \(A\) is responsible for outcome \(Y\)
- \(A\) lacks sufficient observability of state variables influencing \(Y\)

Then control error increases.

Failure modes:

- **Scapegoating**: blame without sensing
- **Paralysis**: refusal to act due to uncertainty

Responsibility without observability is operationally incoherent.

---

## 5. Reciprocity (the core invariant)

> Responsibility requires observability.
> Observability requires responsibility.

Any system violating either side collapses into known pathologies.

---

## 6. Boundary as conservation law

Information access enables work in the world.
Work requires energy.

Unbounded observability is **free energy**.

Responsibility-bounded observability is the conservation mechanism that prevents runaway dynamics.

---

## 7. Minimal axiom set

**Axiom A — Information advantage**
More information expands achievable control.

**Axiom B — Externality amplification**
Advantages without cost scale competitively.

**Axiom C — Observation is action-relevant**
Signals influence decisions; decisions influence the world.

From A+B+C:

> Stable multi-agent systems require observability and responsibility to be co-scoped.

---

## 8. Glyph-layer mapping (presemantic)

- **loop 🝳** — closed causal circuit
- **witness 🜹** — signal tap
- **boundary 🝚** — circuit breaker
- **consent 🝁** — explicit coupling agreement

> Witness 🜹 may exist only within a boundary 🝚 of a loop 🝳 where repair and credit pathways exist.

Without this:
- witness without loop → surveillance
- loop without witness → superstition
- boundary without consent → coercion
- consent without artifact → theater

---

## 9. Final statement

> **No system should be allowed to observe what it is not prepared to be responsible for.**

This is not ethics.
It is systems hygiene.
