# Next Pass

# J.1 — Independent Verification, Selective Disclosure, and Pilot Hardening

## Purpose

Move J.0 from a deterministic executable reference into a pilot-ready, independently reviewable implementation without broadening the domain.

## Required outputs

1. versioned identifier and namespace specification;
2. event-store ordering, idempotency, replay, and migration rules;
3. authorization-policy versioning;
4. selective-disclosure witness views;
5. participant, operator, and verifier authentication profile;
6. external credential and key-management adapter;
7. concurrency and partial-failure harness;
8. correction-propagation reachability report;
9. privacy and retention enforcement tests;
10. independent verifier packaged separately from the implementation;
11. accessibility and participant-control review;
12. pilot-readiness gate and deployment non-claims.

## Required demonstrations

- two concurrent route attempts do not create duplicate authority or action;
- stale context fails after a correction;
- an expired authority grant cannot execute;
- a selective witness proves the gate without revealing protected source content;
- verifier operation requires no provider code or secret;
- key rotation preserves verification lineage;
- partial tool failure produces a repairable event state;
- correction reachability identifies an intentionally unreachable descendant;
- retention expiry removes optional data while preserving bounded witness;
- an accessibility review changes at least one interface behavior.

## Shared gate

J.1 passes only if:

- authority enforcement remains external to the model;
- selective disclosure does not sever answerability;
- concurrent and replayed events remain idempotent;
- stale grants and stale context cannot act;
- the verifier is operationally independent;
- privacy controls change stored state rather than only policy text;
- the implementation still claims only the bounded scheduling domain.
