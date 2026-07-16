# Candidate Public Training Profile

Status: research artifact  
Content canon status: unset

A public profile should disclose enough to evaluate training claims without exposing sensitive source data or security details.

## Identity and release

```yaml
model_family:
model_version:
provider:
release_regime:
intended_purposes:
prohibited_purposes:
```

## Source authority coverage

Report percentages or bounded qualitative coverage for:

```text
SOURCE KNOWN
LICENSE KNOWN
AUTHORITY KNOWN
COMMUNITY GOVERNANCE REVIEWED
MATERIAL UNKNOWN
MATERIAL CONTESTED
```

## Source-class table

For each material class:

```yaml
source_class:
provenance_status:
authority_basis:
purpose_scope:
license_or_governance:
privacy_status:
withdrawal_support:
benefit_terms:
known_disputes:
```

## Human contribution

Disclose:

- contributor roles;
- recruitment region and structure;
- compensation method;
- psychological-risk controls;
- disagreement handling;
- downstream-use notice.

## Preference and constitution

Disclose:

- RLHF, DPO, RLAIF, or other method;
- evaluator population and coverage;
- aggregation rule;
- disagreement handling;
- constitution authorship;
- revision authority;
- protected standing;
- known gaps.

## Synthetic data

Disclose:

- generating models;
- approximate proportion;
- source lineage;
- recursive depth;
- contamination and diversity testing.

## Withdrawal and unlearning

Disclose supported rungs:

```text
COLLECTION STOP
SOURCE DELETION
FUTURE EXCLUSION
RUNTIME RETRIEVAL BLOCK
APPROXIMATE UNLEARNING
RETRAINING
MODEL RETIREMENT
```

State verification limits.

## Succession and derivatives

Disclose:

- derivative models;
- open-weight implications;
- restrictions and duties propagated;
- responsible successor.

## Benefit and accountability

Disclose:

- contributor and community benefit;
- audit;
- challenge;
- repair;
- responsible contact.

## Material caveat

> This profile describes training lineage. It does not establish that every deployment of the model is consentful, lawful, safe, or legitimate.
