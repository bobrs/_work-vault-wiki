# Work Vault

A git-backed personal work vault, artifact wiki, and AI-managed continuity system.

This repository is intended to hold a body of work in a form that can be inventoried, versioned, linked, classified, reconciled, and navigated over time.

The initial operating principle:

> Witness before mutation.

No file should be renamed, moved, deleted, merged, or overwritten until it has first been inventoried.

## Directory Map

```text
artifacts/   actual work files
wiki/        human-readable navigation layer
manifest/    machine-readable inventory, logs, and reconciliation state
scripts/     executable maintenance tools
agents/      instructions for AI management agents
.vault/      configuration and schemas
```

## First Steps

1. Add unsorted files to `artifacts/incoming/`.
2. Add already organized files under `artifacts/sorted/` or another deliberate substructure.
3. Run or create the first inventory script.
4. Commit the baseline inventory before moving or renaming anything.
5. Use the wiki as a navigation layer, not the source of truth.

## Source of Truth

```text
Files     = what exists.
Manifest  = what the system knows.
Git       = how things changed.
Wiki      = how humans navigate.
Agents    = how coherence is maintained.
```

## Root Protocol

See:

`20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-1__initial-vault-operating-protocol.md`
