# J.0 Security and Threat Model

Status: reference implementation  
Version: 0.1

## Security posture

J.0 is a local-first demonstration with deterministic data and a simulated tool.

The security objective is not production hardening. It is to prove the constitutional controls are enforceable outside the model.

## Protected assets

- participant source statements;
- standing records;
- correction state;
- authority grants;
- protected conditions;
- tool credentials;
- gate decisions;
- event-chain integrity;
- witness portability;
- residual-state accounting.

## Implemented threat controls

| Threat | Control |
|---|---|
| Source laundering | Model output classes and source references |
| Standing exclusion | Gate standing-coverage check |
| Context collapse | Corrected context revision must match route context |
| Authority laundering | Runtime authority record and external gate |
| Consent expansion | Separate runtime-data policy fields |
| Model-role escalation | Adapter role enforcement and explicit exceptions |
| Tool-token overreach | HMAC gate token plus target-authority check |
| Correction suppression | Correction event lists descendant impact and changes route evaluation |
| Witness capture | Provider-independent checksummed ZIP and verifier |
| Lifecycle obligation loss | Retirement record, credential revocation, residual-state verification |

## Event integrity

Each event hash is:

```text
SHA-256(previous event hash + canonical event JSON)
```

The first event uses a zero hash as its predecessor.

Event identity is idempotent. Replaying identical content returns the existing event. Reusing the identity with different content raises an error.

## Tool authority

The model cannot mint a valid tool authorization token.

The external gate signs:

```text
route identity
runtime authority identity
gate result
```

The scheduling simulator verifies that token before commit.

A valid tool credential alone is insufficient.

## Retirement

Retirement must verify:

```text
runtime grant expired
tool credential revoked
optional memory deleted
bounded witness retained
open obligations named
```

## Known limitations

- the HMAC secret is demonstration-local and not production key management;
- SQLite is not configured for hostile multi-tenant operation;
- no authentication layer is provided for the web interface;
- selective disclosure is record-level rather than cryptographic;
- no remote-attestation or hardware trust model is implemented;
- no formal authorization language is implemented;
- no production secrets or personal data should be used.
