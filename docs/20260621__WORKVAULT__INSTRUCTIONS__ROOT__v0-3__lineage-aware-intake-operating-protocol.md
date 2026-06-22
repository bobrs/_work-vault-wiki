# Work Vault Operating Protocol

## 0. Status

Version: `0.3`
Date initiated: `2026-06-21`
Repository state: active intake, lineage splitting, duplicate review, and archived snapshot tracking.

This protocol supersedes the initial v0-2 operating note for current work.

## 1. Present Goal

The goal is to preserve evidence while allowing the corpus to become structurally legible.

The immediate goal is to establish a safe operating system for intake so that:

- files can be added without losing history;
- structure can evolve without premature commitments;
- the wiki stays navigable while content grows;
- sub-projects can become stand-alone lineage pages when the files justify it;
- AI agents act conservatively until evidence exists.

## 2. Core Rules

1. Witness before mutation.
2. Path is not identity.
3. Prefer `null` over invented meaning.
4. Treat `.zip` files as auxiliary unless explicitly noted otherwise.
5. Split out evidenced sub-projects using lineage-aware names rather than forcing everything to remain under one parent.
6. After witness is complete, exact duplicates may be collapsed into a coherent set when that does not alter file content and the collapse-parent metadata is preserved.
7. Propose high-impact changes before applying them.
8. Human approval is required for canonization, supersession, deletion, or irreversible consolidation.

## 3. Intake Guidance

- Add source files to `artifacts/incoming/`.
- Preserve original file content.
- Use project pages to reflect observed branch structure, not imagined structure.
- When a branch becomes stable enough to stand alone, give it a lineage label and keep links back to the parent corpus.
- Use review pages to track duplicates, archive snapshots, and uncertain classifications.

## 4. Duplicate and Collapse Guidance

- Exact duplicates are not content changes; they are navigation and metadata decisions.
- Collapse may remove redundant copies from active navigation, but it must preserve the fact that the surviving record has multiple collapse parents when that applies.
- Do not rewrite a file just to make it easier to classify.
- If a duplicate set is only partially witnessed, leave it open.

## 5. Repository Roles

```text
artifacts/   work files and future source material
wiki/        human-readable navigation and review pages
manifest/    machine-readable inventory and audit outputs
scripts/     maintenance and reporting tools
agents/      AI operating prompts
docs/        repository instructions and operating protocol
.vault/      configuration and rules
```

## 6. Intake Workflow

1. Add source files to `artifacts/incoming/`.
2. Run `scripts/inventory.py` to witness the new state.
3. Run `scripts/detect_duplicates.py` if needed.
4. Run `scripts/build_wiki_index.py` to refresh the artifact navigation layer.
5. Review `wiki/incoming-review.md`, `wiki/duplicate-review.md`, and `wiki/missing-files.md`.
6. Only after review, propose moves, renames, merges, classification, or canon decisions.

## 7. Instruction Boundaries

### Inventory

The inventory layer records what exists. It does not impose interpretation.

### Reconciliation

The reconciliation layer compares witnessed states and proposes reversible actions.

### Classification

The classification layer suggests structure only when supported by evidence.

### Wiki

The wiki layer exposes navigation and review pages. It must not overstate certainty, but it can split out real lineage branches when the corpus supports them.

### Canon

Canon and supersession remain explicit human decisions, not automated outcomes.

## 8. Naming

For new generated repository documents, prefer the Artifact Spine convention:

```text
YYYYMMDD__DOMAIN__TYPE__SCOPE__LINEAGE__SLUG.ext
```

Use that convention for new reports, instructions, or exports when it adds clarity.

Do not rename inbound files to fit the convention before inventory has recorded them.

## 9. Ready State

This repository is considered ready for content intake when:

- the directory structure is stable;
- the docs describe the present intake workflow accurately;
- the wiki links resolve;
- the agent prompts avoid speculative behavior;
- the first real artifacts can be added under `artifacts/incoming/` without further setup.
