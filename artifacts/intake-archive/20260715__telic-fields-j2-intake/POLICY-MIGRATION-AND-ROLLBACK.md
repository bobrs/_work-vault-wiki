# Policy Migration and Rollback

## Baseline

Policy version 2 authorizes bounded model-assisted scheduling and prohibits training reuse.

## Failed migration

A candidate version 3 expands the declared purpose to runtime improvement and permits training reuse.

The migration test rejects it because service participation did not authorize model training.

```text
candidate policy v3:
  validation failed
  activation reversed
  policy v2 restored
```

The failed migration remains in history. Rollback does not pretend the migration was never attempted.

## Corrected migration

Policy version 4 preserves:

- participant standing;
- authenticated roles;
- current-context checks;
- protected conditions;
- target authority;
- explicit prohibition of training reuse;
- operator assertion before commitment.

Version 4 becomes active. The runtime authority record is updated to the new version and digest.

## Key consequence

The action-gate key rotates after migration. The prior key is revoked. Authority minted under the earlier key cannot silently cross the policy boundary.

> Policy continuity is not permission continuity.
