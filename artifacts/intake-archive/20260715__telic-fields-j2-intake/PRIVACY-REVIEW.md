# Privacy Review

Status: internal structured review; external privacy review not complete

## Data-flow finding

The pilot requires participant scheduling projections, protected-condition status, operator authority, and action evidence.

The public witness does not require direct protected source language or participant-specific consent details. Those fields are replaced with canonical commitments.

## Runtime-use boundary

```text
service use:
  allowed

cross-session memory:
  refused where specified

evaluation use:
  refused where specified

training reuse:
  refused
```

The failed policy migration confirms that runtime service consent cannot be expanded into training authorization.

## Retention

Optional memory is deleted at retirement. Bounded event and correction witness records remain for the declared review period.

## Open conditions

- external privacy counsel or independent reviewer;
- jurisdiction-specific retention review;
- real participant comprehension testing;
- deletion verification outside the local simulator;
- review of linkability across selective views.
