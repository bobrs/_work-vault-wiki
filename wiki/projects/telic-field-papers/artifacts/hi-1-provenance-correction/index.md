---
title: "Telic Fields HI-1 — Provenance, Correction, and Public Primer"
artifact_date: "2026-07-15"
artifact_type: "paired-technical-and-public-pass"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "working"
processing_tier: 4
source_role: "derived-technical-and-public-architecture-artifact"
content_canon_status: "unset"
publication_status: "unpublished"
series_position: "HI-1"
---

# Telic Fields HI-1 — Provenance, Correction, and Public Primer

Parent lineage: [The Telic Field Papers](../../index.md)

## Source artifacts

### I.1 technical branch

- [I.1 provenance, event, and correction specification](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SPECIFICATION__CANDIDATE__I-1__provenance-event-and-correction.md)
- [I.1 Telic Field PROV profile](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__PROV-PROFILE__WORKING__I-1__telic-field-prov.md)
- [Correction and propagation matrix](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__MATRIX__WORKING__HI-1__correction-and-propagation.md)

### H.1 public branch

- [H.1 What Matters Before the System Acts](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__PRIMER__WORKING__H-1__what-matters-before-the-system-acts.md)

### Gate and validation

- [HI-1 gate review](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__GATE-REVIEW__WORKING__HI-1__provenance-and-public-primer.md)
- [HI-1 validation report](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__VALIDATION-REPORT__WORKING__HI-1__structural-and-semantic-validation.md)
- [HI-1 negative conformance fixtures](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__FIXTURES__WORKING__HI-1__negative-conformance.json)
- [HI-1 validation results](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__VALIDATION-RESULTS__WORKING__HI-1__results.json)
- [HI-1 validation runner](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__VALIDATION-RUNNER__WORKING__HI-1__run-validation.py)
- [HI-1 participant export demo](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__PARTICIPANT-EXPORT__WORKING__HI-1__participant-export-demo.zip)

### Positive demonstrations

- [PD-1 full correction propagation](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMONSTRATION__WORKING__HI-1__FULL-CORRECTION-PROPAGATION.json)
- [PD-2 partial propagation with gap](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMONSTRATION__WORKING__HI-1__PARTIAL-PROPAGATION-WITH-GAP.json)
- [PD-3 expired authority](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMONSTRATION__WORKING__HI-1__EXPIRED-AUTHORITY.json)
- [PD-4 protected omission](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMONSTRATION__WORKING__HI-1__PROTECTED-OMISSION.json)
- [PD-5 inference-status preservation](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMONSTRATION__WORKING__HI-1__INFERENCE-STATUS-PRESERVATION.json)

### I.1 candidate schemas

- [Authority record](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__authority-record.json)
- [Correction propagation record](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__correction-propagation-record.json)
- [Correction record](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__correction-record.json)
- [Derived assertion](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__derived-assertion.json)
- [Participant export manifest](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__participant-export-manifest.json)
- [Portable identifier](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__portable-identifier.json)
- [Protected omission proof](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__protected-omission-proof.json)
- [Selective witness view](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SCHEMA__CANDIDATE__I-1__selective-witness-view.json)
- [Telic Field PROV context](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__CONTEXT__CANDIDATE__I-1__telic-field-prov.jsonld)
- [Complete HI-1 intake package](../../../../../artifacts/intake-archive/20260715__telic-fields-hi1-intake/20260715__TELIC-FIELDS__PHASE-HI1__PROVENANCE-CORRECTION-AND-PUBLIC-PRIMER__v0-1.zip)

The complete package passed its internal SHA-256 manifest before intake. The ZIP hash is 3b97b81244e28197cc000bf02d23f50af2e5546ed8dbf566189e44fb0b9afdd1.

## Working focus

HI-1 completes I.1 and H.1 as a paired pass. I.1 defines provenance, portable identifiers, bitemporal events, correction and supersession, descendant impact, protected omission, selective-disclosure witness views, independent participant export, and repeated-inference status preservation. H.1 translates those constraints into a public primer organized around six questions: what matters, what was shared, what was inferred, who may act, who bears the consequence, and how correction or exit works.

The package includes five positive demonstrations, ten negative conformance fixtures, eight candidate schemas, an independently checksummed participant export, and a public/technical consistency review. The package reports structural and internal semantic validation, not production security, cryptographic proof, legal compliance, scientific validity, or complete external descendant discovery.

## Gate and boundaries

HI-1 is complete at v0.1 with a **PASS WITH CONDITIONS** gate. Remaining conditions include descendant discovery completeness, authenticated correction authority, stronger protected-omission proofs, external-system enforcement, namespace governance, independent reader testing, privacy threat modeling, and domain review for consequential action.

The I.1 specifications, H.1 primer, schemas, demonstrations, and participant export remain working/candidate artifacts. They do not become canonical or production specifications by installation.

## Roadmap transition

The next paired pass is HI-2 — Navigation, Gates, and the Projection Boundary: I.2 Navigation, Gate, and Decision-Witness Specification alongside H.2 The Projection Is Not the Person.
