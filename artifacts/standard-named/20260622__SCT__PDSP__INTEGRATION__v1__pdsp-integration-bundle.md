# PDSP Integration Bundle v0.1

Formerly "Loop Cosmos v0.1 - SSI Bridge and Dialogica"

Status draft02 (20250511). This bundle aligns the original Loop Cosmos assets with the Personal Data Sovereignty Protocol (PDSP-lite v0.1) and the newly introduced Moderator role.

## Table of Contents

- PDSP-lite Header Specification v0.1
- External Credential Declaration Module (`EC Decl`)
- Dialogica Integration Specification v0.1
- TypeScript Monorepo Scaffold
- Glossary Reference and Change Log

## 1. PDSP-lite Header Specification v0.1

A minimal, forward-compatible JSON header that every PDSP packet MUST carry, even if some fields are null.

```json
{
  "loop_id": "sha3256",
  "pulse_n": 42,
  "participants": ["A_pub", "B_pub"],
  "roles": {
    "M_pub": "moderator",
    "C_pub": "witness"
  },
  "ruleset_cid": "bafy...",
  "moderator_sig": "base64(ed25519)",
  "p_token": "b64",
  "merkle_tip": "sha3256"
}
```

Field notes:

- `loop_id`, `pulse_n`, and `moderator_sig` together replace the earlier `session_id` + `JWT` combo.
- If a loop defines no moderator, `moderator_sig` is omitted and downstream engines MUST enforce semantics themselves.

## 2. External Credential Declaration Module (`EC Decl`)

Supersedes the earlier bridge specification.

### 2.1 Purpose

Bind an external credential such as a Google OIDC subject to a PDSP loop without leaking the raw identifier.

### 2.2 Data Model

```json
{
  "ecd_id": "uuidv4",
  "loop_id": "sha3256",
  "credential_hash": "sha3256",
  "issued_pulse": 17,
  "expiry_pulse": 317,
  "bridge_sig": "base64(ed25519)"
}
```

### 2.3 Handshake

1. Subject authenticates with Google and obtains an `id_token`.
2. Subject POSTs `{id_token, loop_id, sig}` to `BridgeAgent`.
3. `BridgeAgent` validates and forms a Bridge Dyad via LoopLink.
4. `BridgeAgent` writes the declaration into its log and into the subject's loop via Abracadabradoo declaration.
5. The client stores the declaration URI returned by the response.

No global ledger is required; inclusion proofs live in each party's Merkle mesh.

## 3. Dialogica Integration Specification v0.1

### 3.1 Purpose and Scope

Deliver a browser-centric demo where two agents, human and bot, exchange structured PDSP-scoped messages over a relay node. The bundle adds Moderator enforcement and removes all persistence on server identifiers.

### 3.2 Architecture

```text
Browser SPA ---WS--- Relay Node ---gRPC--- Bot Worker
Browser SPA: Next.js + libsodium-wasm + pdspsdk
Relay Node: Fastify (HTTP + WS) + PostgreSQL (turn buffer only)
```

### 3.3 Data Model

| Object | Required Fields |
| --- | --- |
| `DialogueSession` | `loop_id`, `created_pulse`, `participants[]` |
| `Turn` | `turn_id`, `loop_id`, `sender`, `ciphertext`, `p_token`, `pulse_n`, `moderator_sig` |
| `WitnessLog` | `turn_id`, `witness_sig` |

The former `session_id`, `ratchet_token`, and `timestamp` fields are deprecated.

### 3.4 API

| Verb | Path | Change |
| --- | --- | --- |
| POST | `/loop/start` | Expects `ExternalCredentialDeclaration` plus loop header; returns `loop_id`, `ws_token`. |
| POST | `/turn` | Requires PDSP header in the WS frame; relay checks `moderator_sig` before persist/forward. |
| GET | `/sync` | Unchanged; WS upgrade delivers new turns. |

### 3.5 Security Updates

- WS tokens remain short-lived JWTs but audience = `loop_id`.
- Each turn must carry a fresh `pulse_n`; relay rejects stale or duplicate pulses.
- Moderator cosigns each accepted turn and the signature is recorded in the header.

## 4. TypeScript Monorepo Scaffold

```text
pdspbundle/
├─ packages/
│  ├─ pdspsdk/      # LoopLink + Abracadabradoo helpers
│  ├─ bridgecli/    # moved to extensions/bridgecli
│  ├─ relaynode/    # accepts PDSP headers; drops session_id auth
│  ├─ botworker/    # must append moderator_sig on replies
│  └─ spaclient/    # uses pdspsdk to form loops and turns
└─ README.md
```

Run scripts:

- `pnpm dev:relay`
- `pnpm dev:bot`
- `pnpm dev:client`

## 5. Glossary Reference and Change Log

Terminology now imports from PDSP Glossary v0.2. All references to `FractalIdentity` were removed.

Change log:

- Replaced SSIBridge with `ExternalCredentialDeclaration`.
- Introduced PDSP-lite header, `moderator_sig`, and `pulse_n` fields.
- Deprecated `session_id`, `ratchet_token`, and `timestamp`.
- Purged FractalIdentity references.
- Moved `bridgecli` to `extensions/`.
- Updated API verb paths and JWT audience.
- Status bumped to draft02.

## End of Bundle

Ready for internal review and alignment with the PDSP-lite implementation roadmap.
