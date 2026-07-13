---
title: "Lineage Without Erasure"
subtitle: "Editorial transcript on historical standing in a living wiki"
date: 2026-07-13
document_type: transcript
standing: historical
authority: provenance
canonical_treatment: /wiki/lineage-markup-convention/
derived_documents:
  - /wiki/lineage-markup-convention/
  - /wiki/lineage-markup-implementation-guide/
preservation_note: >
  This is an editorially compressed transcript. A raw conversation export
  should be preserved separately as the primary conversational record.
---

# Lineage Without Erasure

## Editorial note

This transcript preserves the exchange that produced the lineage-markup convention for the wiki at shimmermemory.com. It has been lightly compressed and organized for readability. The raw conversation should remain available beside it as the fullest provenance artifact.

The important movement in the conversation was not from “old document” to “archive.” It was from an undifferentiated idea of document age toward a grammar capable of saying what a document once was, what it is now, and where its substance went.

## The question

**Bobby Simpson**

I am going to put a large amount of material into my wiki as foundation in a way that grounds and simultaneously clarifies almost all of my existing work.

That feeling brought me to this question: are there conventions for emphasizing or deemphasizing different wiki articles? I do not mean that older articles should not exist, remain available, or be referenced. I mean that some articles represent a historical snapshot in the lineage.

Perhaps what I am really asking is whether there is a convention for lineage visual markup.

## The initial answer

**Assistant**

Yes. What you are reaching for appears across mature knowledge systems as a combination of **document status, version identity, and explicit lineage relations**, although there is no single universal wiki convention.

Several established systems illustrate parts of the pattern:

- RFCs preserve earlier documents while explicitly declaring that a later document **updates** or **obsoletes** them.
- W3C publications distinguish a dated version from a latest version and include a visible statement of the document’s present status.
- MediaWiki commonly uses top-of-page historical notices to retain pages for historical interest without presenting them as current guidance.

These practices converge on a useful principle:

> **Preserve the artifact. Annotate its present standing. Point clearly toward what followed.**

A simple “deprecated” badge would be too blunt for this wiki. It would collapse several meanings that should remain distinguishable:

- once current but no longer current;
- still conceptually valid but incorporated into a larger synthesis;
- exploratory work that did not become canonical;
- an original articulation whose later language is better;
- a position later contradicted;
- authoritative evidence of a historical moment but not present implementation guidance.

The wiki therefore needs more than archival status. It needs **documentary lineage markup**.

### Present standing

Present standing answers:

> What role does this page have now?

A compact initial vocabulary is:

- **Canonical** — the current governing treatment within a stated scope.
- **Active** — current work that remains under development.
- **Historical** — a preserved representation of an earlier moment.
- **Exploratory** — a candidate branch, hypothesis, or incomplete treatment.
- **Retired** — no longer active and without a current governing role.

### Authority

Authority answers:

> How may this page be used now?

A useful vocabulary is:

- **Governing**
- **Supporting**
- **Contextual**
- **Provenance**

This matters because a document may be historical in standing while remaining canonical as provenance. Calling such a document obsolete would erase information rather than clarify it.

### Lineage disposition

Lineage relations answer:

> What happened to this page’s substance?

Useful relations include:

- **derived from**
- **refines**
- **incorporates**
- **supersedes**
- **forks**
- **contradicts**
- **current treatment**

A page may have several of these relationships at once. For example, an article may be historical, retain provenance authority, have been incorporated into one synthesis, and have one claim contradicted by another later document.

## The visual convention

The top-of-page element should be called a **Lineage Notice**, rather than a warning, archive banner, or deprecation notice.

A historical article might begin:

> **Historical snapshot · June 17, 2026**  
> This page preserves the model as it stood at this point in the lineage. It is not the current canonical treatment, but later work depends upon, incorporates, or responds to it.  
> **Current synthesis:** Consentful Systems Stack  
> **Incorporated into:** Witness Foundation; LoopEverything Architecture  
> **Preserved because:** Original articulation of witnessed interloop exchange.

A superseded article might begin:

> **Superseded treatment**  
> This article has been replaced as the current treatment by a later article. It remains available as a preserved step in the concept’s development.  
> **Superseded on:** July 11, 2026  
> **What changed:** The person-level model was replaced by a constitutional or federated account of self.

An incorporated article should not be mislabeled as superseded:

> **Incorporated into a later synthesis**  
> The central claims of this page remain active but are now maintained within the current synthesis. This page is preserved because it records their original context and formulation.

The distinction is consequential. **Superseded** means that a later treatment now governs in place of this one. **Incorporated** means that the substance survives, although its maintained home has changed.

## How emphasis should work

The distinction should be visible in three places.

### On the article

A calm, prominent Lineage Notice appears immediately below the title. It uses text and links, never color alone.

### In indexes and concept maps

Canonical treatments appear first. Historical material remains visible under a heading such as **Lineage and Earlier Treatments**. Historical entries may be visually muted, but they should look layered rather than discarded.

### In search

Historical articles remain searchable. Search results should:

- rank the current canonical treatment above ancestors when both are relevant;
- display standing and authority;
- link directly to the current treatment;
- permit filtering by standing, authority, relation, or date.

The objective is deemphasis without concealment.

## A restraint

The wiki’s conceptual glyphs should not be overloaded with documentary status meanings. Witness, consent, loop, boundary, and related glyphs already carry substantive semantic force. A historical article may itself be a witnessed artifact, but “historical” should not become a second meaning of witness.

Ordinary language should identify documentary standing. The existing glyph language should remain available for the concepts the documents contain.

## Governing compression

> **Nothing is erased merely because the model moved. Every preserved page declares when it spoke, how it now stands, and where its substance went.**

## Resulting documents

This conversation produces two maintained documents:

1. **Lineage Markup Convention** — the semantic and editorial policy.
2. **Lineage Markup Implementation Guide** — front matter, notices, visual behavior, search behavior, and migration procedure.

The transcript is evidence of emergence. The convention governs. The implementation guide operationalizes.
