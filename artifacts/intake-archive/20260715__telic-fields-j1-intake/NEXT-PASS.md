# Next Pass

# J.2 — External Review, Multi-Party Trial, and Release Candidate

## Objective

Move the hardened local reference system into a controlled external-review exercise without widening into production deployment.

## Required outputs

1. external-verifier custody and execution procedure;
2. split signing-key and rotation ceremony;
3. authenticated participant, operator, auditor, and verifier roles;
4. multi-party scheduling trial with at least four affected centers;
5. participant-specific refusal and correction workflow;
6. policy migration and rollback exercise;
7. concurrent request and fault-injection suite;
8. selective-disclosure privacy review;
9. assistive-technology accessibility review;
10. external security and misuse review;
11. release-candidate manifest and reproducible build;
12. J.2 gate review and Stage K transition recommendation.

## Required demonstrations

- a verifier controlled by a separate operator validates the export;
- no single operator holds every signing and execution credential;
- two participants submit conflicting corrections without silent overwrite;
- one participant refuses optional memory while remaining in the service;
- a policy migration fails safely and rolls back;
- a simulated network or queue failure produces idempotent recovery;
- an accessibility finding changes the operative interface;
- a privacy reviewer verifies that public and participant views disclose only intended fields;
- a release candidate rebuilds reproducibly from the package manifest.

## Proposed conformance target

```text
TF-C4 release candidate
+
expanded TF-C5 policy, key, operator, and retirement succession
```

Complete TF-C5 should not be claimed until provider or operator transfer and successor custody are exercised by distinct parties.

## Shared gate

J.2 passes only if:

- external verification is organizationally independent, not merely a separate script;
- authentication and key custody are role-separated;
- concurrent corrections preserve every valid event;
- refusal remains usable and does not silently reduce core service access;
- fault recovery does not replay authority or duplicate action;
- accessibility and privacy reviews produce tracked repairs;
- the release candidate makes only bounded conformance claims;
- repository and wiki ingestion are independently verified.
