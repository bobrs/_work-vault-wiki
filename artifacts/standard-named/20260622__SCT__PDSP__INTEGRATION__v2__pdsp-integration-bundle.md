# PDSP Integration Bundle v0.2

Formerly "Loop Cosmos" bundle - aligned with PDSP-lite Specification v0.2.

Status draft03 (20250511).

## Table of Contents

- PDSP-lite Header Specification v0.2
- External Credential Declaration Module (`EC Decl`)
- Dialogica Integration Specification v0.2
- TypeScript Monorepo Scaffold
- Glossary Reference and Change Log

## 1. PDSP-lite Header Specification v0.2

This bundle pins PDSP-lite v0.2. Key additions since v0.1:

- `participants_delta` - array of keys added or removed by this packet.
- `turn_type` - optional semantic tag such as `proposal`, `reply`, or `meta`.
- New roles `assistant` and `facilitator`.
- Three new API verbs: `/loop/participants`, `/loop/role`, `/loop/ruleset`.

Refer to the standalone PDSP-lite Spec v0.2 for the full schema.

## 2. External Credential Declaration Module (`EC Decl`)

Unchanged from draft02. The module remains optional.

## 3. Dialogica Integration Specification v0.2

### 3.1 Purpose and Scope

Supports up to five parties: two humans, two AI assistants, one AI moderator, and an optional human facilitator, all in a rule-enforced dialogue.

### 3.2 Architecture

```text
Browser SPA ---WS--- Relay Node ---gRPC--- Bot Worker
```

### 3.3 Data Model

| Object | Required Fields |
| --- | --- |
| `DialogueSession` | `loop_id`, `created_pulse`, `participants[]` |
| `Turn` | `turn_id`, `loop_id`, `sender`, `ciphertext`, `p_token`, `pulse_n`, `turn_type?`, `moderator_sig` |
| `WitnessLog` | `turn_id`, `witness_sig` |

### 3.4 API

| Verb | Path | Change |
| --- | --- | --- |
| POST | `/loop/start` | Start loop with initial participant(s); returns `loop_id`, `ws_token`. |
| POST | `/loop/participants` | Append or remove keys via `participants_delta`; returns updated roles map. |
| POST | `/loop/role` | Assign or change a role; requires moderator or loop creator. |
| POST | `/loop/ruleset` | Attach or update `ruleset_cid`; relay loads WASM or JSON-LD policy. |
| POST | `/turn` | Must include PDSP header with `turn_type`; relay validates via rule engine and `moderator_sig`. |
| GET | `/sync` | Unchanged; WS upgrade delivers new turns. |

### 3.5 Security Updates

- Relay persists the highest `pulse_n` per loop and rejects stale or duplicate pulses.
- Moderator AI signs each accepted turn; missing or invalid signature means rejection with error `1002`.
- WASM ruleset modules must export `validate(turn_json) -> bool`.

## 4. TypeScript Monorepo Scaffold

```text
pdsp-bundle/
├─ packages/
│  ├─ pdsp-sdk/   # now exposes createGroupLoop(), mutateParticipants(), setRuleset()
│  ├─ relaynode/  # enforces v0.2 header + new verbs
│  ├─ botworker/  # signs turn_type="assistant_reply" and moderator_sig where relevant
│  └─ spaclient/  # UI modal for role and ruleset selection
└─ README.md
```

Run scripts remain the same:

- `pnpm dev:relay`
- `pnpm dev:bot`
- `pnpm dev:client`

## 5. Glossary Reference and Change Log

Change log:

- v0.2 (draft03, 20250511) - Aligned with PDSP-lite v0.2; added `participants_delta`, `turn_type`, new roles, and new API verbs; status bumped to draft03.
- v0.1 (draft02) - Initial PDSP Integration bundle.

## End of Bundle v0.2
