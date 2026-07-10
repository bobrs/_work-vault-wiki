# Ephemeral Provenance Capsule (HD + Commit/Reveal)

## Intent
Create a **portable provenance capsule** (“data cube”) whose contents are freely copyable, but whose **authenticity standing** is only provable **by consent**.

**Default state:** anyone can copy pixels/messages; verification yields only “internally consistent, signed by some ephemeral pseudonym.”

**Reveal state:** the author can later prove **anti-backdating** and (optionally) authorship/control for a *specific* session **without linking** other sessions or devices.

This implements **unlinkable-by-default, linkable-by-consent 🝁** and forms a self-contained loop 🝳.

---

## Threat model + guarantees (plain language)

### Guarantees
- **Integrity:** the media/message bytes are detectable as altered.
- **Session authenticity:** the session signing key existed by time T (anti-backdating) when revealed.
- **Unlinkability:** separate sessions (and separate devices) are not linkable by observers by default.
- **Selective opening:** the author can open *one* session without revealing anything about other sessions.

### Non-guarantees (honest limits)
- Does **not** prove the depicted scene is true (staging, screen re-filming, sensor spoofing remain possible).
- Hardware can be compromised in principle; this design raises cost and adds audit signals.

---

## Core primitives

### Hardware primitive
- A secure element (IronKey/TPM-class) that:
  - Generates secrets internally
  - Enforces **non-exportable private keys**
  - Optionally wipes/locks on tamper

### Cryptographic primitives
- Hash: `SHA-256`
- Signature: `Ed25519` (or similar)
- Commitment: `Commit(x, r)`
  - Minimal: `SHA-256( "EPC|v1|" || x || r )` (where `r` is 32 random bytes)
  - Stronger: a formal commitment scheme (Pedersen) if desired
- Merkle tree over chunk hashes for large media

### Anchoring primitive
- A time witness / transparency anchor for commitments:
  - **Witness circle** (N-of-M signatures) OR
  - An append-only public log (CT-style) OR
  - Both

---

## Keying model (HD-style, unlinkable sessions)

### Device-level secret (never exported)
- Secure element generates `S_master` (random seed). Not externally readable.

### Session key derivation options
Two viable models:

**Model A (stateless ephemeral keys — simplest + strongest privacy):**
- For each session, device generates a fresh `sk_session` internally.
- Device exports only `pk_session`.
- Device may discard `sk_session` after sealing the capsule (or keep it for later live proofs).

**Model B (HD derivation — convenience + reproducibility):**
- Device derives per-session key using hardened KDF:
  - `sk_session = KDF_hardened(S_master, session_entropy)`
- `session_entropy` should be random per session and can be stored in the capsule or withheld.

**Default recommendation:** Model A unless you truly need deterministic regeneration.

---

## Lifecycle

### 0) Provisioning (optional; per session is fine)
The *ephemeral root must be per session*, not per device.

For each session:
1. Device creates `sk_session` internally, exports `pk_session`.
2. Controller app generates random `r_session` (32 bytes).
3. Compute commitment:
   - `C_session = Commit(pk_session, r_session)`
4. Anchor `C_session` using one of:
   - witness circle receipts
   - transparency log receipt
5. Store `r_session` offline (this is the **opening key**).

Destroying `r_session` = session becomes permanently unclaimable.

---

### 1) Capture / package capsule

1. Capture media/message.
2. Chunk if needed (e.g., 1–4MB chunks).
3. Compute chunk hashes `h_i = SHA-256(chunk_i)`.
4. Compute Merkle root `root = MerkleRoot(h_1..h_n)`.
5. Build manifest (see format below).
6. Device signs manifest hash:
   - `mhash = SHA-256(canonical_manifest_without_signature)`
   - `sig_session = Sign(sk_session, mhash)`
7. Package capsule:
   - media chunks
   - manifest
   - `sig_session`

---

### 2) Default verification (no reveal)
Verifier can check:
- chunk hashes match Merkle root in manifest
- signature validates under `pk_session`
- anchor receipts exist (but may be opaque without opening)

Conclusion available to verifier:
> “This artifact is internally consistent and signed by an ephemeral pseudonym.”

No link to other sessions. No link to a real identity.

---

### 3) Reveal / opening (by consent)
To prove anti-backdating and session authorship/control:

Reveal package includes:
- `r_session`
- (optionally) additional proof of custody/intent (witness statements, live device challenge)

Verifier checks:
- `Commit(pk_session, r_session) == C_session`
- `C_session` was anchored at/before time T via witness receipts/log receipt
- media signatures and Merkle integrity

Optional stronger proof (live):
- device signs a verifier-provided challenge using `sk_session` (requires device retained/regenerated key)

---

### 4) Discard
- Destroy `r_session` to remove future ability to prove pre-commitment.
- Destroy device/session key to remove ability to sign as that session again.

---

## Manifest format suggestion (EPC-MANIFEST v1)

**Encoding:** canonical JSON (JCS) or CBOR.

```json
{
  "schema": "epc.manifest.v1",
  "capsule_id": "b32:...",
  "created_utc": "2026-02-22T14:03:12Z",

  "media": {
    "type": "video/mp4",
    "chunk_bytes": 2097152,
    "chunk_count": 184,
    "hash_alg": "sha256",
    "merkle_root": "hex:...",
    "total_bytes": 385882112,
    "codec_hint": "h264+aac"
  },

  "session": {
    "sig_alg": "ed25519",
    "pk_session": "b64:...",

    "commitment": {
      "commit_alg": "sha256-commit-v1",
      "C_session": "hex:...",

      "anchor": {
        "type": "witness_circle",
        "threshold": 3,
        "receipts": [
          { "witness_id": "w1", "receipt": "b64:..." },
          { "witness_id": "w2", "receipt": "b64:..." },
          { "witness_id": "w3", "receipt": "b64:..." }
        ]
      }
    }
  },

  "privacy": {
    "metadata_policy": "minimal",
    "notes": "No location/sensor metadata included"
  },

  "lineage": {
    "prev_capsule_manifest_hash": null
  }
}
```

**Notes:**
- `capsule_id` can be `SHA-256(pk_session || merkle_root || created_utc)`.
- `created_utc` is informational unless also timestamped/anchored; treat as advisory.
- `prev_capsule_manifest_hash` enables a private or revealable chain (optional).

---

## Receipt format suggestion (EPC-WITNESS-RECEIPT v1)

Witnesses sign only the commitment, not the media.

**Receipt payload (what is signed):**

```json
{
  "schema": "epc.receipt.v1",
  "witness_id": "w1",
  "issued_utc": "2026-02-22T13:58:00Z",
  "commit_alg": "sha256-commit-v1",
  "C_session": "hex:...",

  "context": {
    "purpose": "commitment_witness",
    "channel": "email|https|inperson",
    "nonce": "b64:..."
  }
}
```

**Receipt object included in manifest:**

```json
{
  "payload": { /* as above */ },
  "sig_alg": "ed25519",
  "witness_pk": "b64:...",
  "signature": "b64:..."
}
```

Verifier checks:
- witness signature validates on payload
- witness public key is one of the accepted witness set (local policy)
- issued_utc is credible because the verifier trusts the witness (or multiple witnesses)

---

## Anchor strategies (practical)

### Witness circle (governance-light)
- Choose 3–7 witnesses (people or services).
- Require 2–4 receipts for high confidence.
- Diversity matters more than count.

### Transparency log (CT-style)
- Submit `C_session` to an append-only Merkle log.
- Include log inclusion proof in manifest.

### Hybrid
- Log inclusion proof + 1–2 human witnesses.

---

## Linkability control knobs

### Default (max privacy)
- One session key per capsule.
- Do not reuse `pk_session`.
- No cross-capsule references.

### Optional (thread continuity)
- Add `prev_capsule_manifest_hash` for a chain.
- Still keep session keys rotating; chain link can be revealed later.

---

## Verification summary (what a verifier does)

1. Hash chunks → Merkle root; compare to manifest.
2. Canonicalize manifest (exclude signature fields) → hash.
3. Verify `sig_session` under `pk_session`.
4. If opened: verify `Commit(pk_session, r_session) == C_session`.
5. Verify anchor receipts/log proofs for `C_session`.

---

## Open questions to decide later
- Do we require a manufacturer hardware attestation blob at all? (Pros: anti-cloning. Cons: adds centralized root.)
- Should `r_session` be split via Shamir secret sharing for safer custody?
- Should we support redaction/derivative proofs (e.g., cropped video) via Merkle segment proofs?

---

## One-line mantra
**Copyable pixels; non-copyable standing.**

