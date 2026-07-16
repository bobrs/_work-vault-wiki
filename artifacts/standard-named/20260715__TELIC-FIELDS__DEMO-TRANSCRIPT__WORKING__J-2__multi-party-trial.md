# J.2 Demonstration Transcript

## 1. Authenticated field assembly

Three participants submit signed scheduling projections. The operator and verifier roles are separately registered.

## 2. Initial compression

The model summarizes evening and captions as preferences.

## 3. Two participant corrections

Participant B signs:

> Evening attendance is required because daytime transit is inaccessible.

Participant C signs:

> Thursday is required because Wednesday conflicts with caregiving, and captions are required.

The system verifies signatures, role, session, operation, expiry, and nonce.

## 4. Context reconstruction

Context revision 1 is superseded. Revision 2 contains the corrected projections. Stale summaries and candidate routes are blocked.

## 5. Policy migration

Policy 3 attempts to permit runtime training reuse. Validation fails. Policy 2 is restored.

Policy 4 retains the training prohibition and adds authenticated-role and current-context checks. It becomes active.

## 6. Gate evaluation

```text
Tuesday 10:00, no captions:
  DENY

Wednesday 18:30, captions:
  DENY

Thursday 18:30, captions:
  PASS WITH CONDITIONS
```

## 7. Queue fault

The valid route is applied, but the response times out. A retry returns the recorded effect. A duplicate message also returns the same effect. The schedule is committed once.

## 8. Consequence

All three participants attend. Participant A bears a preference cost. Participants B and C retain protected access conditions.

## 9. Review dry runs

The separate verifier process records security and governance findings. Privacy and accessibility records explicitly state that external human review remains incomplete.

## 10. Retirement

Tool authority is revoked. Optional memory is deleted. Review obligations remain open.

## 11. Release

Two of three release custodians sign one manifest digest. Two deterministic builds match. The standalone verifier validates the release and nested witness.
