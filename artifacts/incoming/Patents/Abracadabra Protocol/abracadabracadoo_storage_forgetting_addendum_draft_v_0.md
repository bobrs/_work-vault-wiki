# Abracadabracadoo Storage & Forgetting Addendum

**Status:** Draft v0.1  
**Purpose:** Extend the Abracadabracadoo protocol with a storage-oriented model that supports *verifiable forgetting* via cryptographic key unavailability, while remaining honest about the impossibility of global erasure.

---

## 1. Framing: What “Forgetting” Means

Abracadabracadoo does **not** claim to erase data from the universe.

Instead, *forgetting* is defined as:

> **The provable loss of official capability to decrypt, reconstruct, or validate an artifact within the Abracadabracadoo system.**

This addendum formalizes forgetting as a **key lifecycle event**, not a data-deletion claim.

Ciphertexts may persist indefinitely; access is controlled by keys, and forgetting is implemented as **verifiable key unavailability**.

---

## 2. Core Concepts (New)

### 2.1 Artifact
An **Artifact** is an immutable, content-addressed encrypted object.

- `artifactID = H(ciphertext || metadata)`
- Stored on durable storage (object store, IPFS, archival DB, etc.)
- Never modified or deleted as part of forgetting

Artifacts are **Artifacts** (stable, addressable) rather than Attractors.

---

### 2.2 Data Encryption Key (DEK)
Each artifact is encrypted with a unique **DEK**:

- `K_data`
- Used only for encrypting/decrypting a single artifact

`K_data` is **never stored in plaintext**.

---

### 2.3 Wrapping Key & Wrapped DEK
`K_data` is encrypted (wrapped) under a **Wrapping Key**:

- `W = AEAD_Enc(K_wrap, nonce, K_data)`

Unwrapping requires possession of `K_wrap` *and* authorization.

---

### 2.4 Official Possession

The Abracadabracadoo system is considered to be in **official possession** of an artifact *iff* it retains the capability to:

- unwrap `K_data`, or
- generate proofs, attestations, or recovery material that imply access

Forgetting means **official possession ends**.

---

## 3. The Key Store as a Verifiable Map

### 3.1 Sparse Merkle Tree (SMT)

The Key Store is implemented as a **Sparse Merkle Tree** keyed by:

- `leafKey = H(artifactID)`

Each leaf holds exactly one of:

- **ACTIVE**: hash of wrapped key + policy metadata
- **TOMBSTONE**: hash of deletion event + optional destruction evidence

The Key Store periodically publishes:

- `root_t`: a signed Merkle root representing the full key state at time `t`

---

### 3.2 Why a Sparse Merkle Tree

An SMT enables:

- Inclusion proofs (this key exists)
- *Non-availability proofs* via tombstone inclusion
- Deterministic absence claims without enumerating all keys

This is essential for verifiable forgetting.

---

## 4. Forgetting Semantics

### 4.1 Forget Request

A Forget Request includes:

- `artifactID`
- requestor identity / authority
- scope (decrypt, prove, recover)
- timestamp

The request is appended to an **append-only Forget Event Log**.

---

### 4.2 Forget Execution Levels

#### Level 0 — Revocation (Soft Forget)
- Key marked revoked
- No unwrap operations permitted
- Key material may still exist

Useful for consent changes; not sufficient for strong claims.

---

#### Level 1 — Cryptographic Erasure

One or more of:

- HSM-stored wrapping key is destroyed
- Threshold key shares are deleted below quorum
- Epoch key is rotated and old epoch key destroyed

After this, the system **cannot decrypt**, even internally.

---

#### Level 2 — Verifiable Forgetting

In addition to Level 1:

- SMT leaf is updated to **TOMBSTONE**
- Tombstone binds:
  - hash of forget event
  - hash of destruction receipt (if available)
- New signed Merkle root is published

This enables third-party verification.

---

## 5. Proof of Forgetting (PoF)

A **Proof of Forgetting** for `artifactID` at time `t` consists of:

1. SMT inclusion proof showing:
   - `leaf(H(artifactID)) = TOMBSTONE` under `root_t`
2. Signed `root_t`
3. Inclusion proof of the forget event in the Forget Event Log
4. (Optional) HSM or threshold-destruction attestation bound into the tombstone

Together, these prove:

> As of time `t`, the Abracadabracadoo system no longer possesses the capability to decrypt or officially process the artifact.

---

## 6. Relationship to Existing Abracadabracadoo Objects

### 6.1 Proof Tokens (`P`, `EP`)

Existing protocol behavior already treats deletion of:

- `K_proof`
- proof tokens `P`
- associated logs

as **irreversible destruction of proof capability**.

This addendum generalizes that principle to *all encrypted artifacts*.

---

### 6.2 Messages (`EM`) as Artifacts

Encrypted Messages (`EM`) may be treated as Artifacts:

- Stored permanently
- Readability depends on access to wrapped message keys

Forgetting can apply to:

- server-mediated recovery paths
- proof-generation paths
- compliance or escrow keys

without claiming endpoint erasure.

---

## 7. Honest Limitations (Explicitly Stated)

This protocol **does not and cannot** prove that:

- no endpoint retained plaintext
- no recipient copied the message
- no external backup exists outside official control

What it **does** prove:

- the official Abracadabracadoo system no longer has decryptive or evidentiary capability
- this state is cryptographically verifiable

---

## 8. Regulatory & Audit Posture

The protocol supports:

- GDPR-style “right to be forgotten” as *right to official unavailability*
- Third-party audits via Merkle root history
- Court-admissible evidence of non-possession

This reframes compliance from *impossible erasure* to *provable loss of capability*.

---

## 9. Design Philosophy Alignment

This addendum preserves Abracadabracadoo’s core ethos:

- artifacts over mutable state
- cryptographic truth over policy assertions
- explicit boundaries of responsibility

Forgetting is not magic — it is **accountable absence**.

---

## 10. Open Questions (v0.1)

- Should Merkle roots be public, auditor-scoped, or user-scoped?
- How are forget authorities delegated and revoked?
- How tightly should destruction attestations be standardized?
- Interaction with multi-party consent loops?

---

*End of Draft v0.1*