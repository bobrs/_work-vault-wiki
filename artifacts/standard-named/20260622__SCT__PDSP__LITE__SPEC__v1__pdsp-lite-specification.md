# Personal Data Sovereignty Protocol (PDSP-lite) Specification v0.1

Status: Draft 02 - 11 May 2025

## 1. Introduction

PDSP-lite v0.1 defines the minimal, forward-compatible packet header and validation rules required for any implementation of the Personal Data Sovereignty Protocol. It freezes the field names, cryptographic primitives, and error codes needed by independent teams to interoperate while the full PDSP specification evolves.

The scope intentionally excludes advanced features such as group-loop quorums, Merkle-tree pruning, and moderator policy languages. Those are deferred to later drafts of the full PDSP spec.

## 2. Packet Header Schema

Every PDSP packet MUST carry a JSON header object with the fields below. Any unknown field MUST be ignored without error.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `loop_id` | hex-string (SHA-3-256) | Yes | Stable identifier for the loop; constant for its lifetime. |
| `pulse_n` | uint64 | Yes | Current ratchet epoch within the loop. |
| `participants` | array<pub_key> | Yes | List of participant Ed25519 public keys. |
| `roles` | map<pub_key,string> | No | Maps public keys to roles such as `moderator` or `witness`. |
| `ruleset_cid` | string (CID) | No | Content-addressed hash of a WASM or JSON-LD ruleset module. |
| `moderator_sig` | base64 | Conditional | Ed25519 signature by the moderator over the canonical header, excluding this field. Absent if no moderator. |
| `p_token` | base64 | No | Abracadabradoo proof-of-receipt token for the payload. |
| `merkle_tip` | hex-string (SHA-3-256) | Yes | Leaf hash of sender's personal Merkle log after writing this packet. |

## 3. Validation and Error Codes

Relay nodes and clients MUST reject packets that fail any mandatory check, returning one of the numeric error codes below. Codes in the 1xxx range are reserved for header-level validation.

| Code | Name | Condition |
| --- | --- | --- |
| 1001 | MISSING_FIELD | A required field is absent. |
| 1002 | INVALID_SIGNATURE | `moderator_sig` is present but fails verification. |
| 1003 | STALE_PULSE | `pulse_n` is not greater than the last accepted pulse. |
| 1004 | DUPLICATE_PULSE | `pulse_n` duplicates a previously accepted packet. |
| 1005 | UNAUTHORIZED_ROLE | Sender claims a role not assigned in `roles`. |

## 4. Security Considerations

All cryptographic hashes MUST be computed using SHA-3-256. All signatures MUST use Ed25519 with the context string `PDSP-lite-v0.1`.

Implementations SHOULD protect against replay by persisting the highest accepted `pulse_n` per loop.

## 5. Change Log

- v0.1 (Draft 02, 2025-05-11) - Initial public draft extracted from the PDSP Integration Bundle.
