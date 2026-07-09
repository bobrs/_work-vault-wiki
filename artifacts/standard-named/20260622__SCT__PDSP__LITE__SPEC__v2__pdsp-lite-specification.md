# Personal Data Sovereignty Protocol (PDSP-lite) Specification v0.2

Status: Draft 03 - 11 May 2025

## 1. Introduction

PDSP-lite v0.2 supersedes v0.1 by adding minimal fields and API verbs required for multi-party loops that include AI assistants, human facilitators, and a rule-enforcing Moderator.

The objective remains a lightweight, forward-compatible header and validation surface while the full PDSP specification matures.

## 2. Packet Header Schema

The v0.1 fields remain, with the additions below highlighted.

| Field | Type | Required | Description |
| --- | --- | --- | --- |
| `loop_id` | hex-string (SHA-3-256) | Yes | Stable identifier for the loop; constant for its lifetime. |
| `pulse_n` | uint64 | Yes | Current ratchet epoch within the loop. |
| `participants` | array<pub_key> | Yes | List of participant Ed25519 public keys. |
| `participants_delta` | array<pub_key> | No (join packets) | New. Keys added or removed by this packet. |
| `roles` | map<pub_key,string> | No | Maps public keys to roles such as `participant`, `assistant`, `facilitator`, `moderator`, `witness`. |
| `turn_type` | string | No | New. Semantic tag such as `proposal`, `reply`, or `meta`. |
| `ruleset_cid` | string (CID) | No | Content-addressed hash of a WASM or JSON-LD ruleset module. |
| `moderator_sig` | base64 | Conditional | Moderator signature over canonical header; omit if no moderator. |
| `p_token` | base64 | No | Abracadabradoo proof-of-receipt token. |
| `merkle_tip` | hex-string (SHA-3-256) | Yes | Leaf hash of sender's personal Merkle log after writing this packet. |

## 3. Validation and Error Codes

Validation semantics are unchanged from v0.1 except for two additional checks:

- If `participants_delta` is present, it MUST be consistent with the signed loop state.
- If `turn_type` is provided, it MUST be a non-empty ASCII string no longer than 32 bytes.

## 4. New API Verbs

| Verb | Path | Authorization | Description |
| --- | --- | --- | --- |
| POST | `/loop/participants` | loop token | Append or remove keys via `participants_delta`; returns updated roles map. |
| POST | `/loop/role` | loop token | Assign or change a role for a given `pub_key`; requires moderator or loop creator. |
| POST | `/loop/ruleset` | loop token | Attach or replace `ruleset_cid`; relay fetches the ruleset and returns 200 if loaded. |

## 5. Change Log

- v0.2 (Draft 03, 2025-05-11) - Added `participants_delta`, `turn_type`, new roles `assistant` and `facilitator`, and API verbs `/loop/participants`, `/loop/role`, `/loop/ruleset`.
- v0.1 (Draft 02) - Initial public draft.
