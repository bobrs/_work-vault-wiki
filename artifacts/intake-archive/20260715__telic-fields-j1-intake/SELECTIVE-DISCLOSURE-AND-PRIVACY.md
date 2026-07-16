# Selective Disclosure and Privacy

## Governing rule

> Witnessability does not require total visibility.

J.1 exports four views.

## Public view

Includes:

- route and gate outcomes;
- action and consequence;
- correction events at bounded scope;
- retirement and residual obligations.

Excludes:

- direct protected source wording;
- participant-specific consent detail;
- unnecessary standing and context records.

Every omitted object receives a canonical SHA-256 commitment.

## Participant view

Includes:

- the participant's own standing, source, projection, and correction;
- shared route and action records;
- consequence and retirement.

Other participants' direct source content is redacted and committed.

## Operator view

Includes records required to:

- apply standing;
- enforce policy;
- evaluate context;
- operate the gate and tool;
- process correction and repair;
- retire the pilot.

It does not grant training reuse.

## Verifier view

Includes the full bounded synthetic record set.

The verifier receives no private signing key and no model-provider connection.

## Runtime data controls

```text
service:
  allowed

cross-session memory:
  denied

evaluation use:
  denied

training use:
  denied

public export of direct private content:
  denied
```

## Commitment limitation

A hash commitment proves consistency with the full export available to the verifier.

It does not by itself prove:

- truth of the committed content;
- lawful collection;
- absence of dictionary attacks against predictable private text;
- safe publication in every domain.

Production selective disclosure may require salted commitments, encryption, access control, or zero-knowledge methods.
