# Telic Field Papers — HI-0 Controlled Branch Opening

This package opens H — Public Reader Path and I — Technical Specification Branch together.

## Included

### Technical branch

- `I0-CANONICAL-SEMANTIC-SPINE-SPECIFICATION.md`
- `I0-CONFORMANCE-MATRIX.md`
- `schemas/core-envelope.schema.json`
- `schemas/center-reference.schema.json`
- `schemas/telic-projection.schema.json`
- `schemas/semantic-trail-event.schema.json`
- `schemas/route-and-gate.schema.json`
- `schemas/model-role-authority.schema.json`
- `schemas/decision-witness.schema.json`
- `schemas/contest-correction-event.schema.json`

### Public branch

- `H0-PUBLIC-READER-ARCHITECTURE.md`

### Worked examples

- `examples/EXAMPLE-A-PERSONAL-REVERSIBLE-DECISION.md`
- `examples/example-a-personal-reversible-decision.json`
- `examples/EXAMPLE-B-DYADIC-MEDIATED-DISAGREEMENT.md`
- `examples/example-b-dyadic-mediated-disagreement.json`
- `examples/EXAMPLE-C-MODEL-MEDIATED-INSTITUTIONAL-ACTION.md`
- `examples/example-c-model-mediated-institutional-action.json`

### Review and transition

- `VALIDATION-REPORT.md`
- `HI0-GATE-REVIEW.md`
- `PHASE-STATUS.md`
- `NEXT-PASS.md`
- `SHA256SUMS.txt`

## I.0 result

I.0 defines a minimum normative spine:

```text
center
→ source object
→ telic projection
→ semantic trail event
→ active context selection
→ receiver mirror
→ field map
→ route
→ governance gate
→ authorized action
→ consequence
→ decision witness
→ contest, correction, or release
```

It defines four conformance profiles:

- P0 Documentary;
- P1 Source-Aware Navigation;
- P2 Action-Bearing;
- P3 Contestable.

## H.0 result

H.0 creates a public path beginning with the ordinary problem:

> A system is about to act on a representation of what matters.

The public sequence introduces technical terms only after the reader understands the practical question each term answers.

## Worked-example result

All three examples pass the bridge:

1. personal reversible decision;
2. dyadic mediated disagreement;
3. model-mediated institutional action.

They preserve:

- source/inference separation;
- protected conditions;
- consent and other authority bases;
- minimum necessary disclosure;
- model-role boundaries;
- meaningful correction and exit.

## Validation result

- 8 valid Draft 2020-12 candidate JSON Schemas;
- 0 schema-validation errors;
- selected example instances validated successfully;
- 0 selected instance-validation errors.

This is structural validation, not legal, scientific, ethical, security, or production certification.

## Gate result

```text
PASS WITH CONDITIONS
```

Proceed to HI-1:

- I.1 — Provenance, Event, and Correction Specification;
- H.1 — What Matters Before the System Acts.
