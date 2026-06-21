# Work Vault Operating Protocol

## 0. Status

Version: `0.2`
Date initiated: `2026-06-21`
Repository state: scaffolding only; no substantive work-vault content has been loaded yet.

This protocol defines how the repository should behave before and during initial content intake.

## 1. Present Goal

The immediate goal is not to infer projects, canon, or concepts.

The immediate goal is to establish a safe operating system for future intake so that:

- files can be added without losing history;
- structure can evolve without premature commitments;
- the wiki remains navigable while mostly empty;
- AI agents act conservatively until evidence exists.

## 2. Core Rules

1. Witness before mutation.
2. Path is not identity.
3. Prefer `null` over invented meaning.
4. Propose high-impact changes before applying them.
5. Human approval is required for canonization, supersession, deletion, or irreversible consolidation.

## 3. Empty-State Guidance

Until real content is added:

- `artifacts/` is the only place expected to receive work files.
- `wiki/` should remain a neutral navigation layer, not a speculative knowledge base.
- `projects/`, `concepts/`, and `timelines/` should stay sparse and structural.
- agent prompts should optimize for caution, intake, and reviewability.
- canon behavior is mostly inactive.

Do not preload recurring ideas, attractors, or named domains into the wiki unless they are evidenced by actual artifacts in the repository.

## 4. Repository Roles

```text
artifacts/   work files and future source material
wiki/        human-readable navigation and review pages
manifest/    machine-readable inventory and audit outputs
scripts/     maintenance and reporting tools
agents/      AI operating prompts
docs/        repository instructions and operating protocol
.vault/      configuration and rules
```

## 5. Intake Workflow

1. Add source files to `artifacts/incoming/`.
2. Run `scripts/inventory.py` to witness the new state.
3. Run `scripts/detect_duplicates.py` if needed.
4. Run `scripts/build_wiki_index.py` to refresh the artifact navigation layer.
5. Review `wiki/incoming-review.md`, `wiki/duplicate-review.md`, and `wiki/missing-files.md`.
6. Only after review, propose moves, renames, merges, classification, or canon decisions.

## 6. Instruction Boundaries

### Inventory

The inventory layer records what exists. It does not impose interpretation.

### Reconciliation

The reconciliation layer compares witnessed states and proposes reversible actions.

### Classification

The classification layer suggests structure only when supported by evidence.

### Wiki

The wiki layer exposes navigation and review pages. It must not overstate certainty.

### Canon

Canon and supersession remain explicit human decisions, not automated outcomes.

## 7. Naming

For new generated repository documents, prefer the Artifact Spine convention:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

Use that convention for new reports, instructions, or exports when it adds clarity.

Do not rename inbound files to fit the convention before inventory has recorded them.

## 8. Ready State

This repository is considered ready for content intake when:

- the directory structure is stable;
- the docs describe the present empty-state workflow accurately;
- the wiki links resolve;
- the agent prompts avoid speculative behavior;
- the first real artifacts can be added under `artifacts/incoming/` without further setup.
