# Abracadabracadoo Protocol Addendum VIII: Private Consent Vector Collapse

**Status:** Draft – Cryptographic / Governance Layer
**Filed Under:** Private Aggregation, Consent 🝁 Collapse, Quorum Semantics, Selective Disclosure
**Working Name:** Private Consent Vector Collapse
**Abbreviation:** PCVC

---

## Abstract

This addendum extends the Abracadabracadoo Protocol family with a privacy-preserving mechanism for aggregating participant consent 🝁 states without requiring disclosure of each participant’s full consent vector.

Where prior addenda define explicit consent declarations, witnessable loops, nested quorums, conditional deniability, and evaluable derivative artifacts, this addendum defines a method for **private consent aggregation with verifiable collapse**.

A group may prove that a scoped consent condition has been satisfied without exposing the individual consent vectors from which that condition was derived.

In canonical form:

> **Private Consent Vector Collapse allows a group to prove that a scoped consent condition has been satisfied without exposing the individual consent states from which that condition was derived.**

This enables:

* Quorum-based consent 🝁 without full participant disclosure
* Private veto detection
* Selective revelation of aggregate permissions
* Consent-aware group finalization
* Derivative artifacts whose authority is bounded by the consent state that produced them

---

## 1. Motivation

Abracadabracadoo already supports encrypted messages, proof tokens, explicit consent confirmations, witness-readable structures, nested group loops, conditional deniability, and evaluable derivative artifacts.

The Consent Confirmation Loop Extension establishes that receipt is not consent, and that consent should be an explicit follow-up act cryptographically tied to a prior message hash. 

The Nested Loops and Group Quorums addendum defines group loop genesis, quorum thresholds, decision rules, collapse, publication, and nested semantic state formation. 

However, group consent introduces a new problem:

> A group may need to prove that consent exists without exposing how each participant consented.

Naively, a system could publish every participant’s consent vector. But this is overexposing.

It may reveal:

* Who agreed
* Who objected
* Who hesitated
* Which dimensions were sensitive
* Which minority positions existed
* Which participant carried a veto
* Which future coercion paths are available

For many domains, this violates the spirit of consent 🝁 itself.

Therefore, this addendum introduces a new construct:

> **A private consent collapse artifact**: a verifiable aggregate result derived from hidden, scoped, committed, or encrypted participant consent vectors.

The loop need not reveal everyone’s interior state. It need only prove that the collapse condition was satisfied under a declared policy.

---

## 2. Core Principle

Private Consent Vector Collapse is governed by one central invariant:

> **Consent may be aggregated, but not extracted.**

A group result is valid only if:

1. Each participant’s consent vector is bound to the loop.
2. Each vector conforms to the declared schema.
3. The aggregation policy is known, committed, or otherwise inspectable.
4. The resulting collapse state is verifiably derived.
5. The result carries scope, expiry, and allowed-use boundaries.
6. Dissent, veto, or uncertainty are preserved when required by policy.

This aligns with Addendum VII’s treatment of derived artifacts, which requires evaluability, bounded context, dissent-preserving compression, and scoped use for downstream interpretations or decisions. 

A consent aggregate is not merely a tally.

It is a **derived artifact with authority**.

---

## 3. Definitions

### 3.1 Consent Vector

A **Consent Vector** is a structured representation of a participant’s scoped permissions, prohibitions, conditions, and limits within a loop.

Example:

```json
{
  "receive": true,
  "read": true,
  "store": false,
  "summarize": true,
  "quote": false,
  "forward": false,
  "witness_readable": true,
  "public_verifiable": false,
  "train_on": false,
  "derive_from": true,
  "expires_at_epoch": 42,
  "confidence": 0.86,
  "intensity": 0.74,
  "hard_veto": false
}
```

A Consent Vector may contain:

* Boolean values
* Numeric values
* Threshold values
* Expiry fields
* Conditional clauses
* Veto flags
* Scope tags
* Purpose limitations
* Derivative-use permissions

A Consent Vector is not global. It is always scoped to:

```text
loop + artifact + purpose + evaluator/context + time/epoch
```

---

### 3.2 Vector Schema

A **Vector Schema** defines the meaning, type, and allowed range of each consent dimension.

Example:

```json
{
  "schema_id": "pcvc.basic.v0.1",
  "fields": {
    "store": "boolean",
    "quote": "boolean",
    "summarize": "boolean",
    "derive_from": "boolean",
    "train_on": "boolean",
    "hard_veto": "boolean",
    "expires_at_epoch": "integer"
  }
}
```

The schema itself SHOULD be hashed:

```text
schema_hash = H(vector_schema)
```

All committed or encrypted consent vectors MUST bind to the schema hash.

This prevents semantic bait-and-switch, where a participant consents under one schema but the aggregate is interpreted under another.

---

### 3.3 Consent Vector Commitment

A **Consent Vector Commitment** is a cryptographic binding to a participant’s vector without necessarily revealing the vector.

Possible constructions include:

```text
C_i = Commit(consent_vector_i, nonce_i)
```

or:

```text
E_i = Enc_agg_key(consent_vector_i)
```

or:

```text
ZKCommit(consent_vector_i, schema_hash, loop_id)
```

The specific primitive is implementation-dependent.

The protocol-level requirement is:

> The participant binds a consent vector to a loop, schema, and policy context without requiring premature disclosure of the vector itself.

---

### 3.4 Aggregation Policy

An **Aggregation Policy** defines how private vectors produce a collapse result.

Examples:

```json
{
  "policy_id": "7_of_9_no_veto",
  "rule": {
    "quorum": {
      "type": "threshold",
      "required": 7,
      "eligible": 9
    },
    "hard_veto_allowed": false,
    "field_rules": {
      "witness_readable": "threshold",
      "train_on": "unanimous",
      "quote": "unanimous",
      "summarize": "majority_with_dissent_marker"
    }
  }
}
```

The policy SHOULD be hashed:

```text
policy_hash = H(aggregation_policy)
```

Participants SHOULD know or be able to inspect the policy before submitting their vectors.

---

### 3.5 Collapse Result

A **Collapse Result** is the aggregate consent state produced by applying the Aggregation Policy to the committed or encrypted vectors.

Example:

```json
{
  "loop_id": "H(loop_genesis)",
  "schema_hash": "H(schema)",
  "policy_hash": "H(policy)",
  "result": {
    "witness_readable": true,
    "store": true,
    "quote": false,
    "summarize": true,
    "train_on": false,
    "hard_veto_present": false
  },
  "confidence": {
    "valid_inputs": true,
    "quorum_satisfied": true,
    "aggregation_verified": true
  },
  "scope": {
    "artifact_id": "H(artifact)",
    "purpose": "mediation_review",
    "expires_at_epoch": 42,
    "transferable": false
  }
}
```

The Collapse Result is the thing that may be shared.

The underlying vectors remain hidden unless selectively disclosed.

---

### 3.6 Private Consent Collapse Artifact

A **Private Consent Collapse Artifact** is the full record of aggregate consent, including:

* Loop identifier
* Schema hash
* Policy hash
* Input commitment references
* Aggregate result
* Proof of correct aggregation
* Scope of use
* Expiry or reversal conditions
* Optional dissent markers
* Optional disclosure controls

Canonical structure:

```json
{
  "artifact_type": "private_consent_vector_collapse",
  "version": "0.1",
  "loop_id": "H(loop_genesis)",
  "artifact_id": "H(target_artifact)",
  "schema_hash": "H(vector_schema)",
  "policy_hash": "H(aggregation_policy)",
  "input_commitments": [
    "C_1",
    "C_2",
    "C_3"
  ],
  "collapse_result": {
    "quorum_satisfied": true,
    "hard_veto_present": false,
    "allowed_actions": [
      "store",
      "witness_readable",
      "summarize"
    ],
    "disallowed_actions": [
      "quote",
      "train_on",
      "public_disclosure"
    ]
  },
  "proof": {
    "type": "implementation_specific",
    "value": "..."
  },
  "scope": {
    "valid_for": "target_artifact_only",
    "audience": "loop_participants_and_authorized_witnesses",
    "expires_at_epoch": 42,
    "non_transferable": true
  },
  "dissent": {
    "minority_position_exists": true,
    "hard_veto_present": false,
    "dissent_disclosed": false
  },
  "reversal_conditions": [
    "new audience",
    "new purpose",
    "new storage tier",
    "epoch_expiry",
    "participant revocation"
  ]
}
```

---

## 4. Privacy Goals

This addendum separates privacy into distinct goals. Implementations MUST NOT assume that one cryptographic primitive satisfies all of them.

### 4.1 Value Privacy

Hide the content of each participant’s consent vector.

Example:

```text
The system learns that 7 of 9 consented to storage, but not which 7.
```

### 4.2 Identity Privacy

Hide which participant submitted which vector.

Example:

```text
The system knows valid members participated, but cannot map vectors to identities.
```

### 4.3 Participation Privacy

Hide whether a specific eligible participant participated at all.

Example:

```text
The group can prove quorum without revealing whether Alice was one of the consenting participants.
```

### 4.4 Policy Privacy

Hide the full aggregation policy while proving the result satisfies a committed rule.

Example:

```text
The public sees that the disclosure rule passed but not the internal weighting model.
```

This should be used cautiously. Consent systems SHOULD default toward policy inspectability.

### 4.5 Result Privacy

Hide the aggregate result except from authorized parties.

Example:

```text
Only the mediator learns whether the group consented to witness-readable disclosure.
```

### 4.6 Dissent Privacy

Allow the existence or absence of dissent to be represented without exposing dissenters.

Example:

```text
A minority position exists, but its author and content are hidden.
```

---

## 5. Supported Cryptographic Strategies

This addendum does not mandate a single cryptographic primitive. It defines the protocol role that several primitives may satisfy.

### 5.1 Homomorphic Encryption

Useful when the system needs to compute over encrypted consent values.

Example:

```text
Enc(1) + Enc(0) + Enc(1) = Enc(2)
```

Best for:

* Counting yes votes
* Computing thresholds
* Aggregating numeric consent intensity
* Private tallying
* Weighted voting

Limitations:

* Does not automatically hide participation metadata
* Does not by itself prove input validity
* May require threshold decryption governance
* More complex key lifecycle

---

### 5.2 Commitments and Zero-Knowledge Proofs

Useful when participants must bind to consent vectors and prove properties without revealing full contents.

Best for proving:

```text
My vector was valid under schema_hash.
My value was Boolean.
My consent was included.
I did not change my vector after seeing others.
The aggregate was computed from committed inputs.
```

This is often the most general foundation for PCVC.

---

### 5.3 Secure Multiparty Computation

Useful when multiple parties jointly compute a collapse result without exposing their inputs to one another.

Best for:

* No-single-server architectures
* Sensitive group decisions
* Distributed governance
* Private veto detection
* Consent states that should never exist in plaintext outside endpoints

Limitations:

* Interactive
* Operationally more complex
* Harder to audit after the fact unless transcript commitments are preserved

---

### 5.4 Threshold Signatures

Useful when the only required public fact is that quorum was reached.

Instead of publishing individual consent signatures, a group emits one threshold signature:

```text
Sig_group(declaration)
```

Meaning:

```text
A sufficient authorized subset consented under the policy.
```

Best for:

* Clean quorum collapse
* Low-disclosure group approvals
* Governance finalization
* Public declarations where individual votes need not be exposed

This maps especially cleanly to existing group loop finalization semantics from the Nested Loops and Group Quorums addendum. 

---

### 5.5 Anonymous Credentials / Ring Signatures

Useful when the system must prove that a participant was eligible without revealing which participant acted.

Best for:

```text
Someone in the eligible group submitted a valid consent vector.
```

or:

```text
At least N eligible members participated, but their identities remain hidden.
```

---

## 6. Protocol Flow

### 6.1 Loop Genesis

A Group Loop is established using existing loop genesis semantics:

```json
{
  "loop_id": "H(genesis_payload)",
  "participants": ["P_1", "P_2", "P_3"],
  "quorum_policy": "policy_hash",
  "vector_schema": "schema_hash",
  "target_artifact": "artifact_id",
  "purpose": "declared_purpose",
  "epoch": "loop_local_epoch"
}
```

This builds on the existing group-loop model, where loop genesis may include participants, quorum threshold, synchronization context, and signed purpose. 

---

### 6.2 Schema and Policy Declaration

Before consent vectors are submitted, participants receive or inspect:

```text
schema_hash
policy_hash
target_artifact
purpose
allowed result disclosures
expiry semantics
reversal conditions
```

A participant MUST NOT be considered to have consented to an aggregation policy they could not inspect or verify, unless the policy itself is intentionally private and the participant consented to that privacy condition.

---

### 6.3 Vector Submission

Each participant constructs a Consent Vector locally.

They then submit one or more of:

```text
commitment
encrypted vector
validity proof
eligibility proof
signature or anonymous membership proof
```

Example:

```json
{
  "loop_id": "H(loop_genesis)",
  "participant_proof": "eligible_member_proof",
  "schema_hash": "H(schema)",
  "policy_hash": "H(policy)",
  "commitment": "C_i",
  "encrypted_vector": "E_i",
  "validity_proof": "ZK_i"
}
```

The participant’s vector SHOULD remain private by default.

---

### 6.4 Aggregation

An aggregator, committee, MPC network, smart contract-adjacent service, or threshold group applies the Aggregation Policy to the submitted vectors.

Depending on primitive choice, aggregation may occur over:

* Plaintext vectors inside a trusted enclave
* Encrypted values
* Secret shares
* Commitments plus proofs
* Threshold signature shares
* MPC transcripts

The aggregator produces:

```text
collapse_result
proof_of_correct_aggregation
input_set_commitment
```

---

### 6.5 Collapse

A loop collapses if the aggregate result satisfies the declared policy.

Example:

```json
{
  "quorum_satisfied": true,
  "hard_veto_present": false,
  "collapse_authorized": true
}
```

The collapse is then bound to the loop as a Private Consent Collapse Artifact.

This artifact may be:

* Stored privately
* Shared with participants
* Shared with witnesses
* Published as a public declaration
* Used as an input into a higher-order nested loop

---

### 6.6 Publication or Containment

The Collapse Artifact MUST declare its allowed use.

Example:

```json
{
  "allowed_use": [
    "mediate_dispute",
    "store_artifact_until_epoch",
    "summarize_for_participants"
  ],
  "disallowed_use": [
    "public_quote",
    "model_training",
    "external_forwarding"
  ]
}
```

This aligns with the Addendum VII principle that derived artifacts carry scope and containment semantics. 

---

## 7. Private Veto Detection

Some consent 🝁 systems require more than majority approval.

They require absence of a hard objection.

PCVC supports **private veto detection**, where the system can prove one of:

```text
No hard veto exists.
```

or:

```text
A hard veto exists.
```

without revealing the vetoing participant.

Example policy:

```json
{
  "rule": "5_of_7_and_no_hard_veto",
  "conditions": {
    "minimum_yes": 5,
    "hard_veto_present": false
  }
}
```

Possible collapse result:

```json
{
  "threshold_passed": true,
  "hard_veto_present": true,
  "collapse_authorized": false
}
```

The system learns that collapse failed, but not necessarily whose boundary prevented collapse.

This preserves the dignity of refusal.

Canonical invariant:

> **A veto may halt collapse without becoming a spectacle.**

---

## 8. Dissent-Preserving Aggregation

A consent aggregate MUST NOT erase meaningful dissent merely because the threshold passed.

When required by policy, the Collapse Artifact SHOULD include dissent markers:

```json
{
  "minority_position_exists": true,
  "minority_count_disclosed": false,
  "hard_veto_present": false,
  "reversal_conditions": [
    "audience expansion",
    "purpose change",
    "public disclosure request"
  ]
}
```

Dissent markers may be:

* Public
* Participant-only
* Witness-only
* Hidden but provable
* Revealable under dispute conditions

This prevents aggregate consent from becoming coerced semantic compression.

Canonical invariant:

> **Threshold is not unanimity. Collapse is not erasure.**

---

## 9. Relationship to Prior Addenda

### 9.1 Core Abracadabracadoo Protocol

The core protocol binds message ciphertext and proof token through nested AEAD and hash-derived nonces, allowing proof without exposing plaintext to the server. 

PCVC extends the same philosophy:

```text
Proof of consent state without exposure of consent contents.
```

---

### 9.2 Consent Confirmation Loop Extension

The Consent Confirmation Loop Extension defines explicit consent declarations tied to prior message hashes. 

PCVC generalizes this from:

```text
Participant B consents to message M.
```

to:

```text
The group’s consent vector collapsed under policy P.
```

---

### 9.3 Minimal Witness Structures

The Minimal Witness Structures addendum introduces loop headers containing participants, consent flags, witness roles, payload hashes, and timestamps. 

PCVC can use those structures to declare:

```text
who may submit
who may witness
who may aggregate
who may verify
who may receive the collapse result
```

---

### 9.4 Nested Loops and Group Quorums

The Nested Loops and Group Quorums addendum already defines quorum policies, decision rules, expiry, nested references, and group finalization. 

PCVC adds privacy-preserving input treatment to that architecture.

A higher loop may depend on a lower PCVC artifact rather than on exposed individual signatures.

---

### 9.5 Conditional Deniability

The Conditional Deniability addendum introduces recipient-contributed secrets so that verification may require participant cooperation, preserving consent-based proof exposure. 

PCVC may optionally adopt the same philosophy:

```text
Aggregate verification may require threshold cooperation.
```

This prevents a leaked aggregator key from making all participant vectors retroactively exposed or verifiable beyond consent.

---

### 9.6 Storage & Forgetting

The Storage & Forgetting addendum defines forgetting as official loss of decryptive or evidentiary capability, not impossible global erasure. 

PCVC collapse artifacts SHOULD specify what can be forgotten:

* Raw vectors
* Decryption shares
* Aggregation transcripts
* Eligibility mappings
* Proof material
* Public result
* Witness logs

A system may retain the aggregate while forgetting the constituents.

Or it may forget the aggregate while retaining commitments.

Or it may retain only a tombstone proving official unavailability.

---

### 9.7 Evaluation and Derivation Stewardship

Addendum VII governs derivative cognition: summaries, advice, rankings, recommendations, and automated actions derived from prior artifacts. It requires evaluator signatures, snapshot pointers, dissent-preserving compression, and scoped containment. 

PCVC collapse artifacts are derived artifacts.

Therefore, they SHOULD carry:

```text
Evaluator / Aggregator Signature
Snapshot Pointer
Aggregation Policy
Input Commitment Set
Dissent Markers
Allowed Use Scope
Reversal Conditions
```

---

## 10. FractalIdentity Interaction

Because identity may be contextual, plural, and relationship-specific, consent vectors SHOULD NOT be assumed to attach to a single global identity.

The FractalIdentity protocol defines identity channels as contextual relationship links between agents, with visibility, continuity, interpretive notes, and context-specific boundaries. 

Therefore, PCVC MAY bind consent vectors to identity channels rather than global identities.

Example:

```json
{
  "identity_channel": "bob_as_mediator_participant",
  "consent_vector": {
    "witness_readable": true,
    "public_verifiable": false,
    "train_on": false
  }
}
```

The same human or agent may have different consent vectors across different identity channels.

Canonical invariant:

> **Consent follows context, not merely identity.**

---

## 11. Security and Privacy Considerations

### 11.1 Aggregator Trust

If an aggregator sees plaintext vectors, it becomes a high-trust party.

Implementations SHOULD prefer:

* Homomorphic aggregation
* MPC
* Threshold decryption
* Trusted execution only with explicit disclosure
* Zero-knowledge validity proofs

where stronger privacy is required.

---

### 11.2 Coercion Risk

Even if vectors remain private, participants may be coerced into revealing their own vector after the fact.

Mitigations may include:

* Deniable vector openings
* Selective disclosure credentials
* Expiring proof material
* Threshold-controlled verification
* Policy-level prohibition on individual vector disclosure

---

### 11.3 Minority Exposure

Small groups make privacy fragile.

Example:

```text
If 2 of 3 consented and Alice knows she voted no, she can infer both others voted yes.
```

PCVC cannot eliminate all inference risk.

The Collapse Artifact SHOULD optionally include a privacy warning when group size or policy structure makes inference likely.

---

### 11.4 Schema Ambiguity

Consent vectors are only meaningful if the schema is stable and human-legible.

A field like:

```json
"share": true
```

is dangerously ambiguous.

Better:

```json
"share_with_named_witness_for_mediation_until_epoch_42": true
```

or schema-bound equivalent.

---

### 11.5 Consent Laundering

A system MUST NOT use private aggregation to launder weak consent into strong public authority.

Example failure:

```text
“70% consented to some form of analysis”
```

becomes:

```text
“The group consented to unrestricted model training.”
```

This is invalid.

The aggregate result cannot exceed the declared vector schema, policy, and scope.

Canonical invariant:

> **Aggregate consent cannot authorize more than its least-scoped valid derivation.**

---

### 11.6 Veto Semantics

A hard veto should be treated as a boundary, not merely a negative vote.

Policies MUST distinguish:

```text
no
abstain
not applicable
conditional yes
hard veto
expired consent
invalid vector
```

Failure to distinguish these collapses consent 🝁 into preference polling.

---

### 11.7 Result Reuse

A Collapse Artifact is not universally portable.

A result valid for:

```text
private mediation summary
```

does not authorize:

```text
public disclosure
model training
commercial reuse
legal filing
press quotation
```

unless explicitly included.

---

## 12. Example Use Cases

### 12.1 Mediated Agreement

A group enters a mediation loop.

Participants privately submit vectors indicating whether a mediator may read plaintext records.

The result reveals:

```json
{
  "witness_readable": true,
  "public_verifiable": false,
  "hard_veto_present": false
}
```

The mediator receives authority to read, but not to publish.

---

### 12.2 DAO Governance Without Vote Exposure

A DAO needs to approve an action without exposing individual member votes.

Participants submit encrypted consent bits.

The system publishes:

```json
{
  "quorum_satisfied": true,
  "threshold": "67_percent",
  "action_authorized": true
}
```

Individual votes remain hidden.

---

### 12.3 Private Anti-Training Consent

A group contributes documents to an AI-assisted workspace.

Each participant privately indicates whether their contributions may be used for training.

Collapse result:

```json
{
  "summarization_allowed": true,
  "retrieval_allowed": true,
  "training_allowed": false,
  "hard_veto_present": true
}
```

The workspace may summarize but not train.

---

### 12.4 Witness-Readable but Not Publicly Verifiable

Participants allow a witness to see plaintext, but do not allow public validation unless later consent is given.

This combines PCVC with witness-readable controlled verifiability from Addendum V and conditional deniability from Addendum VI. The witness may see or attest, while public proof remains participant-controlled.  

---

### 12.5 Nested Consent Collapse

A local committee privately collapses its consent vector.

A higher-order governance loop receives only:

```text
Committee A: consent satisfied under policy_hash_X.
```

The higher loop need not see individual committee vectors.

This supports federated governance without overexposing lower-level participants.

---

## 13. Open Questions

1. Should the default PCVC construction use commitments plus ZK proofs, homomorphic encryption, MPC, or threshold signatures?

2. Should private veto detection reveal only `hard_veto_present`, or should it reveal classes of veto?

3. Can a participant submit multiple vectors through different FractalIdentity channels within the same group loop?

4. Should aggregation policies be public by default, or can policy privacy be consentfully invoked?

5. What is the minimum viable proof object for early prototypes?

6. How should expired vectors affect previously collapsed artifacts?

7. Can a collapse result be partially revoked?

8. What is the right distinction between:

   * failed quorum,
   * active dissent,
   * hard veto,
   * invalid vector,
   * non-participation?

9. Should the system support “dissent escrow,” where minority objections are hidden unless later dispute conditions arise?

10. How should PCVC interact with Proof of Forgetting when the aggregate remains useful but the constituent vectors should become officially unavailable?

---

## 14. Minimal Prototype Path

For a first implementation, avoid full homomorphic complexity.

A practical prototype could use:

```text
commitments + plaintext local aggregation + signed aggregate result
```

Then evolve toward:

```text
commitments + ZK validity proofs + threshold aggregation
```

Then:

```text
homomorphic or MPC-based private aggregation
```

Suggested v0.1 implementation:

1. Define a simple Boolean consent vector schema.
2. Hash the schema.
3. Define a simple aggregation policy: `N-of-M and no hard veto`.
4. Each participant signs and commits to their vector.
5. A trusted aggregator computes the result.
6. Aggregator publishes:

   * input commitment list,
   * policy hash,
   * schema hash,
   * result,
   * signature,
   * allowed-use scope.
7. Later versions replace the trusted aggregator with MPC, homomorphic tallying, or ZK proofs.

This gives the semantic object first, then upgrades the cryptography.

---

## 15. Canonical Invariants

* Consent may be aggregated, but not extracted.
* A vector is not a vote; it is a scoped boundary object.
* Threshold is not unanimity.
* Collapse is not erasure.
* A veto may halt collapse without becoming a spectacle.
* Aggregate consent cannot exceed the scope of its inputs.
* Consent follows context, not merely identity.
* The group may speak without exposing every voice.
* Privacy-preserving collapse is valid only when the policy itself was consented to.
* A consent aggregate is a derived artifact and must carry containment.

---

## 16. Conclusion

Abracadabracadoo began by proving receipt without exposing plaintext.

It then extended into explicit consent, declarations, witnesses, nested groups, subjective epochs, conditional deniability, storage, forgetting, and derivative stewardship.

Private Consent Vector Collapse adds the next missing layer:

> **proof that a group consent condition has been satisfied without forcing each participant’s consent state into the open.**

The loop may now collapse without confession.

The group may authorize without exposing every boundary.

The artifact may carry authority, but only within the scope that produced it.

Consent 🝁 remains sovereign, even when aggregated.

**The vector stays private.
The collapse becomes provable.
The boundary survives the group.**
