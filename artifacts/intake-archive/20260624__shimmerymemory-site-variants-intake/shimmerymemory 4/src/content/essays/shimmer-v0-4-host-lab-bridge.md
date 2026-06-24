---
title: "Shimmer v0.4 Prototype: Host Lab + Bridge"
subtitle: "A working proof that exposed anchors can be tuned, encoded, restored, and witnessed."
description: "Prototype notes for the Shimmer v0.4 host lab, bridge script, demo shimmer-enabled site, and the mechanics of portable field state."
date: 2026-06-10
draft: false
tags:
  - shimmer
  - prototype
  - host-lab
  - bridge
  - anchors
  - field-seed
  - shimmerprint
  - portable-state
attribution:
  label: "Shimmery Memory"
  url: "/"
canonical_glyphs:
  - name: "shimmer"
    glyph: "⋆✴︎˚｡⋆"
  - name: "artifact"
    glyph: "▣"
  - name: "loop"
    glyph: "🝳"
  - name: "witness"
    glyph: "🜹"
  - name: "home"
    glyph: "🪺"
related_elements:
  - label: "P3 — Authorization and Consent Gate"
    site: "Quantum Invariants"
    url: "https://quantuminvariants.com/spine/primitives#P3"
    type: "primitive"
  - label: "C6 — Composite 6"
    site: "Quantum Invariants"
    url: "https://quantuminvariants.com/spine/composites#C6"
    type: "composite"
---

## What the Prototype Proves

Shimmer v0.4 is tuned for color interaction, but color is not the important part.

The important part is that the prototype proves the Shimmer mechanics:

```text
surface exposes anchor points
host discovers them
controls are generated
state mutates live
state is encoded
encoded state can travel
surface can reconstitute itself from the seed
```

The prototype currently calls these anchor points CSS variables. Structurally, they are more general than that. A CSS variable is simply the first friendly anchor type.

## Working Pieces

The prototype contains three working pieces:

```text
shimmer-host-lab.html
shimmer-bridge.js
demo-shimmer-site.html
```

Together, they establish a complete minimal loop:

```text
projection surface
→ exposes manifest
→ bridge announces manifest
→ host generates controls
→ user tunes anchors
→ host sends mutations
→ surface applies mutations
→ host encodes field seed
→ link restores field
→ shimmerprint witnesses trace
```

That is enough to treat Shimmer as a protocol family, not merely a visual idea.

## The Deep Pattern

The prototype is not a color picker.

It is an anchor manipulation system.

A projection surface exposes anchor points. Shimmer discovers them. The user grooms them. The state is encoded. The projection can be reconstituted elsewhere.

In the demo, the anchor points are CSS variables such as:

```text
--cream
--sun-a
--sun-size
--sky
--field-x
--speckle-opacity
--card-opacity
```

But the generalized form is:

```text
anchor_id
label
type
range/default/options
current value
projection behavior
seed encoding rule
```

That same structure can apply to:

- colors
- typography
- spacing
- glyph density
- document compression
- metaphor level
- reader expertise
- loop awareness
- semantic echoes
- protocol diagrams
- identity fields
- merch/poster generation
- Rosetta translations
- consent graphs

The key abstraction is:

```text
A shimmer-enabled artifact exposes groomable anchors.
```

The anchor may be visual, semantic, symbolic, relational, procedural, or generative.

## Why Color Is the Correct First Demo

Color is not the destination, but it is a very good first projection because it is:

- immediate
- low-risk
- visible
- playful
- shareable
- intuitive
- fast
- portable

Color teaches the protocol without forcing the user to understand the protocol.

A visitor does not need to know what a field seed is to enjoy making a tiny world. But after they do, the concepts become obvious:

```text
I changed the field.
The link remembered.
The trace remained.
```

That is enough.

The color-focused demo should remain, but it should be framed clearly as:

```text
The first playground for portable field state.
```

Not theme picker. Not brand color editor. Not CSS toy.

It is the first visible proof that shimmer state can travel.

## Canonical Operating Model

```text
1. Canonical artifact exists.
2. Artifact exposes anchors through a manifest.
3. Shimmer host reads the manifest.
4. User tunes anchors.
5. Projection updates.
6. Field seed captures reversible state.
7. Shimmerprint captures public trace.
8. Restorable link reconstitutes the projection.
```

More compressed:

```text
Expose → Tune → Seed → Restore → Witness
```

Or in Shimmery terms:

```text
Artifact → Anchor → Groom → Reconstitute → Trace
```

The deepest roadmap phrase may be:

```text
Shimmer lets artifacts expose anchor points that can be groomed, exploded, reconstituted, and witnessed.
```

## Generalizing from Variables to Anchors

The current manifest has variables:

```js
variables: [
  { key: "--cream", label: "Top cream", type: "color", default: "#fff7e6" }
]
```

The conceptual upgrade is anchors:

```js
anchors: [
  {
    id: "field.cream",
    target: "css",
    key: "--cream",
    label: "Top cream",
    type: "color",
    default: "#fff7e6"
  }
]
```

Why this matters:

```text
variables implies CSS.
anchors implies generality.
```

Semantic anchors can then exist:

```js
{
  id: "semantic.metaphor",
  target: "document",
  label: "Metaphor",
  type: "scalar",
  min: 1,
  max: 5,
  default: 3
}
```

Glyph anchors can exist:

```js
{
  id: "glyph.symbolDensity",
  target: "glyph-layer",
  label: "Symbol Density",
  type: "scalar",
  min: 0,
  max: 5,
  default: 2
}
```

Protocol anchors can exist:

```js
{
  id: "loop.echoDepth",
  target: "echo-stack",
  label: "Echo Depth",
  type: "integer",
  min: 0,
  max: 7,
  default: 2
}
```

This is the key evolution from color lab to shimmer substrate.

## Governance Principle

A shimmer-enabled surface should only expose anchors it consents to have tuned.

The manifest is not just technical metadata. It is a consent boundary.

```text
This surface allows these dimensions to be changed.
This surface does not allow those dimensions to be changed.
This seed can restore this state.
This shimmerprint can witness this trace.
```

So the Shimmer Manifest is also a consent surface.

```text
No manifest, no tuning.
No exposed anchor, no authorized mutation.
No seed, no reversible return.
No trace, no public witness.
```

This protects Shimmer from becoming an extractive overlay that tries to modify anything arbitrarily. The bridge is opt-in. The manifest is permission. The seed is bounded. The source remains intact.

## Product Language

```text
Sites expose anchors. Shimmer tunes them. Seeds remember.
```

```text
A field seed returns you home. A shimmerprint leaves a trace.
```

```text
The artifact stays still. The projection shimmers.
```

```text
Shimmer is not the sunset. Shimmer is how the sunset travels.
```

```text
A manifest is a consent boundary for transformation.
```

```text
Anything can become a seed. Not everything can return you home.
```

```text
Read the artifact. Tune the field. Carry the seed. Leave a trace.
```

## Prototype Verdict

The prototype proves that:

```text
an artifact can expose anchors,
a host can discover them,
a field can be groomed,
a state can be encoded,
a projection can be reconstituted,
and an encounter can leave a trace.
```

That is the beginning.
