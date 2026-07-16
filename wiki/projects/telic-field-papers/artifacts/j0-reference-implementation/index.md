---
title: "Telic Fields J.0 — Reference Implementation and Pilot Harness"
artifact_date: "2026-07-15"
artifact_type: "executable-reference-implementation-and-pilot-harness"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "working"
processing_tier: 4
source_role: "executable-candidate-implementation-artifact"
content_canon_status: "executable-candidate"
publication_status: "unpublished"
series_position: "J.0"
---

# Telic Fields J.0 — Reference Implementation and Pilot Harness

Parent lineage: [The Telic Field Papers](../../index.md)

## Package identity

- Profile: `TF-C4`
- Bounded extension: `TF-C5` retirement
- Scenario: `TF-MVI-1` bounded model-assisted scheduling
- Gate: **PASS WITH CONDITIONS**

## Design and governance

- [Architecture](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__ARCHITECTURE__WORKING__J-0__reference-implementation-and-pilot-harness.md)
- [Conformance claim](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__CONFORMANCE-CLAIM__CANDIDATE__J-0__tf-c4-bounded-tf-c5-retirement.md)
- [Demo transcript](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMO-TRANSCRIPT__WORKING__J-0__reference-scenario.md)
- [J.0 gate review](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__GATE-REVIEW__WORKING__J-0__reference-implementation-and-pilot-harness.md)
- [Runbook](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__RUNBOOK__WORKING__J-0__reference-implementation-and-pilot-harness.md)
- [Security and threat model](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SECURITY-AND-THREAT-MODEL__WORKING__J-0__reference-implementation-and-pilot-harness.md)
- [Upstream metadata reconciliation note](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__UPSTREAM-RECONCILIATION__WORKING__J-0__metadata-reconciliation-note.md)
- [J.0 validation report](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__VALIDATION-REPORT__WORKING__J-0__reference-implementation-and-pilot-harness.md)
- [Package manifest](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__PACKAGE-MANIFEST__WORKING__J-0__package-manifest.json)

## Executable implementation

The fifteen Python implementation modules are preserved under the [standard-named source directory](../../../../../artifacts/standard-named/) with the `IMPLEMENTATION__CANDIDATE__J-0` prefix. The package includes the local-first event/object store, deterministic model adapter, external HMAC-backed action gate, scheduling simulator, correction and consequence paths, retirement handling, witness generation, verifier, threat harness, and local web interface.

The six HI-S consolidated schema families are preserved with the `SCHEMA__FROZEN__J-0` prefix. Project metadata, dependencies, demo/test runners, and the five-test-file suite are also standard-named.

## Demonstration and witness

- [Reference scenario input](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__EXAMPLE__WORKING__J-0__reference-scenario-input.json)
- [Demo result](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMO-RESULT__WORKING__J-0__demo-result.json)
- [End-to-end validation](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMO-VALIDATION__WORKING__J-0__end-to-end-validation.txt)
- [Threat results](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__THREAT-RESULTS__WORKING__J-0__threat-results.json)
- [Export verification](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__EXPORT-VERIFICATION__WORKING__J-0__tf-mvi-1-witness.json)
- [TF-MVI-1 provider-independent witness export](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__WITNESS-EXPORT__WORKING__J-0__tf-mvi-1-witness.zip)

The reference run contains 15 events and 29 objects. It proves a failed gate, a valid action, consequence return, participant correction propagation, retirement revocation, and independent witness verification. The ten-threat harness detects all ten consolidated threat fixtures.

## Validation result

```text
7 tests
0 failures
0 errors
10 threat cases detected
16 witness-export checksums verified
29 records validated
15 events verified
```

The executable demo and test runner pass. The independent witness export verifies with no errors.

## Conditions and non-claims

J.0 is an executable candidate, not production software or a certification. Conditions before a real pilot include managed credentials, participant/operator authentication, selective disclosure, policy versioning, concurrency and partial-failure testing, accessibility review, external security review, synthetic or consented data only, and provider-independent verifier hardening.

The package does not claim production security, legal or regulatory compliance, real-world accessibility adequacy, general model safety, universal Telic Field conformance, or suitability for clinical, legal, financial, employment, or public-adjudication use.

## Intake archive

- [Complete J.0 intake package](../../../../../artifacts/intake-archive/20260715__telic-fields-j0-intake/20260715__TELIC-FIELDS__PHASE-J0__REFERENCE-IMPLEMENTATION-AND-PILOT-HARNESS__v0-1.zip)

Package SHA-256: `b485e5f33ff8774bcc4dd51b3f166c54988412f6b65f7ab173aff944fcb648a9`

The exact package passed its internal SHA-256 manifest. Its witness export passed all 16 entries in its embedded checksum manifest. The archive and extracted source contents remain preserved as historical intake evidence.

## Roadmap transition

J.0 is complete at v0.1. The next pass is **J.1 — Independent Verification, Selective Disclosure, and Pilot Hardening**. J.1 should harden witness and enforcement layers without expanding the conceptual ontology.
