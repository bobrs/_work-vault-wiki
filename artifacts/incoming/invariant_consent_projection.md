```json
{
  "invariant_id": "INV-CoP-001",
  "name": "Consent Projection",
  "category": "Systems / Agency / Consent",
  "core_statement": "Systems maintain legitimacy by projecting consent across time and participation boundaries.",
  "short_form": "Legitimacy requires counterfactual consent.",
  "expanded_definition": "Any system that imposes constraints or distributes outcomes must sustain a believable account of why those constraints are legitimate for participants who are not actively consenting in the moment. Because participation is often continuous (citizenship, employment, platform use, family membership) and consent is episodic, systems project consent forward in time (prior agreement binds future situations) and backward in time (present enforcement is justified by presumed consent). This projection stabilizes cooperation and reduces renegotiation overhead.",
  "mechanism": {
    "problem": "Consent cannot be continuously re-collected for every constraint, update, or enforcement action.",
    "solution": "The system emulates continuity of consent using contracts, norms, membership narratives, defaults, and implied consent rules.",
    "result": "Participants treat enforcement as legitimate even when they are not explicitly consenting in the moment."
  },
  "cross_domain_examples": {
    "contracts": "A signature projects consent into future conditions and disputes.",
    "law": "Citizens are treated as bound by laws through membership, representation, and due process narratives.",
    "medicine": "Informed consent authorizes future procedures within defined scope and contingencies.",
    "platforms": "Terms of service project consent across updates and unseen data flows.",
    "relationships": "Boundaries and agreements project consent into ambiguous future scenarios.",
    "markets": "Voluntary exchange assumes consent, even amid unequal bargaining power.",
    "religion": "Covenant and belonging narratives project consent across generations and rites.",
    "ai_systems": "Delegation and deployment contexts project human consent into automated decisions."
  },
  "consent_primitives": {
    "explicit": "Direct, informed agreement (signed, spoken, opted-in).",
    "scoped": "Consent bounded by domain, duration, intensity, and revocability.",
    "delegated": "Consent granted to an agent or process to act within defined constraints.",
    "defaulted": "Consent assumed unless actively withdrawn (opt-out).",
    "implied": "Consent inferred from participation or context (high-risk for abuse)."
  },
  "shadow": {
    "statement": "When projected consent becomes fiction, legitimacy becomes coercion with paperwork.",
    "failure_modes": [
      "Implied consent used as a loophole for extraction",
      "Retroactive consent claims ("You agreed by being here")",
      "Scope creep beyond what was knowingly authorized",
      "Consent made non-revocable or practically unreachable",
      "Information asymmetry weaponized to manufacture assent"
    ],
    "tell": "If exit is costly and refusal is punished, consent projection is likely fictional."
  },
  "diagnostic_questions": [
    "What is the claimed basis of consent (explicit, scoped, delegated, defaulted, implied)?",
    "What did the participant actually know at the time of consenting?",
    "Is consent revocable in practice (not just in theory)?",
    "Did the scope expand beyond the original agreement?",
    "Is refusal or exit meaningfully available without retaliation?"
  ],
  "repair_strategies": [
    "Make consent basis explicit (no hidden implied-only binding)",
    "Add scope, duration, and revocation handles",
    "Separate 'participation' from 'permission' (membership ≠ blanket consent)",
    "Require re-consent on scope changes",
    "Provide auditable consent logs and plain-language summaries"
  ],
  "pairing": {
    "paired_with": "INV-CP-001",
    "paired_name": "Consequence Projection",
    "paired_relationship": "Consequences project forward in time; consent projects binding justification across time.",
    "joint_claim": "Stable, just systems require both persistent consequence and legitimate consent."
  },
  "memetic_compressions": [
    "Consequences bind behavior; consent binds legitimacy.",
    "If you can’t say no, it wasn’t consent.",
    "Legitimacy is consent that still holds when no one is asking."
  ],
  "loop_mapping": {
    "loop_0": "Binary distinction between consent / no-consent (and implied vs explicit)",
    "loop_1": "Scoped consent with revocation and renegotiation",
    "loop_2": "Adaptive consent governance: continuous audit + periodic re-consent on scope change"
  },
  "status": "draft",
  "version": "0.9.0"
}
```

