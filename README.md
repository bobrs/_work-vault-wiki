# Work Vault

A git-backed personal work vault, artifact wiki, and AI-managed continuity system.

This repository is prepared to hold a body of work in a form that can be inventoried, versioned, linked, classified, reconciled, and navigated over time.

Right now it is a blank operating scaffold: the structure, instructions, scripts, and review pages exist, but substantive vault content has not been added yet.

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
docs/        repository operating instructions
.vault/      configuration and rules
```

## Current Phase

The wiki should stay neutral until content exists. Do not pre-seed projects, concepts, canon pages, or named attractors without artifact evidence.

## First Content Intake

1. Add source files to `artifacts/incoming/`.
2. Run `python3 scripts/inventory.py`.
3. Run `python3 scripts/detect_duplicates.py` when needed.
4. Run `python3 scripts/build_wiki_index.py`.
5. Review the generated state before any move, rename, merge, or canon decision.

## Source Of Truth

```text
Files     = what exists.
Manifest  = what the system knows.
Git       = how things changed.
Wiki      = how humans navigate.
Agents    = how coherence is maintained.
```

## Operating Instructions

See:

- [`docs/README.md`](docs/README.md)
- [`docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-2__empty-vault-operating-protocol.md`](docs/20260621__WORKVAULT__INSTRUCTIONS__ROOT__v0-2__empty-vault-operating-protocol.md)

## Public Site

The wiki web layer is prepared as a fully static Cloudflare Pages build.

- Build command: `npm run build`
- Landing page output: `dist/index.html`
- Raw vault browser: `dist/vault/index.html`
- Public source repository: `https://github.com/bobrs/_work-vault-wiki`
