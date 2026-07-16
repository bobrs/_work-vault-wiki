---
title: "Telic Fields J.1 — Independent Verification, Selective Disclosure, and Pilot Hardening"
artifact_date: "2026-07-15"
artifact_type: "independent-verification-selective-disclosure-and-pilot-hardening"
domain: "TELIC-FIELDS"
scope: "WORKING"
lineage: "THE-TELIC-FIELD-PAPERS"
status: "working"
processing_tier: 4
source_role: "executable-candidate-implementation-artifact"
content_canon_status: "executable-candidate"
publication_status: "unpublished"
series_position: "J.1"
---

# Telic Fields J.1 — Independent Verification, Selective Disclosure, and Pilot Hardening

Parent lineage: [The Telic Field Papers](../../index.md)

## Package identity

- Profile: `TF-C4`
- Bounded extension: `TF-C5` retirement
- Scenario: `TF-MVI-1` bounded model-assisted scheduling
- Gate: **PASS WITH CONDITIONS**
- Production claim: none

J.1 hardens the J.0 reference pilot without widening its domain claim. Its central path is:

```text
source → projection → standing → versioned policy and authority
→ current context → non-sovereign model route → signed external gate
→ transactional tool attempt → consequence → correction
→ selective witness export → independent verification → retirement
```

## Design and governance

- [Architecture](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__ARCHITECTURE__WORKING__J-1__independent-verification-and-pilot-hardening.md)
- [Conformance claim](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__CONFORMANCE-CLAIM__CANDIDATE__J-1__tf-c4-bounded-tf-c5-retirement.md)
- [Policy, key, and context hardening](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__POLICY-HARDENING__WORKING__J-1__versioned-keys-and-context.md)
- [Selective disclosure and privacy](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SELECTIVE-DISCLOSURE-PRIVACY__WORKING__J-1__four-witness-views.md)
- [Correction reachability report](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__CORRECTION-REACHABILITY__WORKING__J-1__known-descendants.md)
- [Partial failure and recovery](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__PARTIAL-FAILURE-RECOVERY__WORKING__J-1__transactional-compensation.md)
- [Accessibility review](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__ACCESSIBILITY-REVIEW__WORKING__J-1__no-javascript-interface.md)
- [Security and threat model](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__SECURITY-AND-THREAT-MODEL__WORKING__J-1__pilot-hardening.md)
- [J.1 gate review](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__GATE-REVIEW__WORKING__J-1__independent-verification-and-pilot-hardening.md)
- [J.1 validation report](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__VALIDATION-REPORT__WORKING__J-1__independent-verification-and-pilot-hardening.md)
- [Runbook](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__RUNBOOK__WORKING__J-1__independent-verification-and-pilot-hardening.md)
- [Upstream metadata reconciliation note](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__UPSTREAM-RECONCILIATION__WORKING__J-1__metadata-reconciliation-note.md)
- [Package manifest](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__PACKAGE-MANIFEST__WORKING__J-1__package-manifest.json)

## Hardening delivered

The package preserves nineteen Python implementation modules, twelve frozen schemas, versioned immutable authorization policy, HMAC key rotation and revocation, canonical stale-context rejection, serialized concurrent appends, optimistic object revisions, correction-descendant reachability, partial-failure compensation, runtime privacy enforcement, and an accessible no-JavaScript interface.

It also includes four selective witness views — public, participant, operator, and verifier — with commitments for omitted records, an Ed25519-signed witness manifest, and a standalone verifier that imports no `telic_j1` implementation code.

## Demonstration and witness

- [Reference scenario input](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__EXAMPLE__WORKING__J-1__reference-scenario-input.json)
- [Hardened demo transcript](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMO-TRANSCRIPT__WORKING__J-1__hardened-reference-scenario.md)
- [Demo result](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMO-RESULT__WORKING__J-1__reference-scenario.json)
- [End-to-end validation](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__DEMO-VALIDATION__WORKING__J-1__end-to-end.txt)
- [Implementation verification](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__IMPLEMENTATION-VERIFICATION__WORKING__J-1__reference-pilot.json)
- [Independent verification result](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__INDEPENDENT-VERIFICATION__WORKING__J-1__standalone-verifier.json)
- [Threat results](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__THREAT-RESULTS__WORKING__J-1__sixteen-case-harness.json)
- [Witness export](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__WITNESS-EXPORT__WORKING__J-1__tf-mvi-1-j1-witness.zip)
- [Standalone verifier](../../../../../artifacts/standard-named/20260715__TELIC-FIELDS__INDEPENDENT-VERIFIER__CANDIDATE__J-1__verify-witness.py)

## Validation result

```text
13 tests
0 failures
0 errors
12 schemas checked
16 threat cases detected
34 witness-export checksums verified
46 records validated
20 events verified
4 selective views verified
Ed25519 manifest signature verified
```

The reference scenario reaches retirement with policy version 2 active, gate keys `gate-k1` and `gate-k2` revoked, `gate-k3` active, tool authority revoked, four correction descendants updated, and no unreachable descendants. The independent verifier succeeds without importing the implementation package or requiring a provider connection.

## Conditions and non-claims

J.1 is an executable candidate, not production software, a certification, or a complete TF-C5 implementation. Remaining conditions include externally controlled signing-key custody, authenticated participants and operators, domain-specific privacy review, external accessibility testing, distributed-failure testing, independent security review, and a real multi-party correction exercise.

The package contains synthetic demonstration records only. It does not claim legal or regulatory compliance, production security, real-world privacy protection, external accessibility conformance, high-stakes safety, or suitability for clinical, legal, financial, employment, benefits, credit, insurance, election, or public-adjudication use.

## Intake archive

- [Complete J.1 intake package](../../../../../artifacts/intake-archive/20260715__telic-fields-j1-intake/20260715__TELIC-FIELDS__PHASE-J1__INDEPENDENT-VERIFICATION-SELECTIVE-DISCLOSURE-AND-PILOT-HARDENING__v0-1.zip)

Package SHA-256: `e8bd00ed91c99cb02fba44e37348c84ec36ad74e9f592d8b62458a0f9d254126`

The exact package passed its internal SHA-256 manifest. Its embedded witness export passed standalone verification with 34 checksums, 46 records, 20 events, four selective views, and a valid Ed25519 signature. The archive and extracted source contents remain preserved as historical intake evidence.

## Roadmap transition

J.1 is complete at v0.1 artifact level. J.2 — External-Review Readiness, Multi-Party Trial, and Release Candidate — is now installed as a bounded candidate release. The next pass is **J.3 — Observed External Exercise, Governance Handoff, and Pilot Admission**.
