---
title: "Shimmer Lab Concept and Code Summary"
subtitle: "Sites expose anchors. Shimmer tunes them. Seeds remember."
description: "A protocol note for Shimmer Lab: projection surfaces, field seeds, shimmerprints, bridge scripts, manifests, and portable state."
date: 2026-06-10
draft: false
tags:
  - shimmer
  - protocol
  - field-seed
  - shimmerprint
  - portable-state
  - projection-surface
  - bridge
  - manifest
attribution:
  label: "Shimmery Memory"
  url: "/"
canonical_glyphs:
  - name: "shimmer"
    glyph: "⋆✴︎˚｡⋆"
  - name: "artifact"
    glyph: "▣"
  - name: "home"
    glyph: "🪺"
  - name: "witness"
    glyph: "🜹"
  - name: "loop"
    glyph: "🝳"
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

## Core Concept

Shimmer Lab is a seed, matrix, and projection workbench for making small digital fields portable.

At its simplest:

```text
A site exposes anchors.
Shimmer tunes them.
A field seed remembers the state.
A shimmerprint leaves a public trace.
```

Shimmer is not itself a single color scheme, aesthetic, or projection. It is the tuning instrument and state substrate.

Individual sites - such as ULiUA, Abracadabracadoo, ProgramSelf, or future project pages - can become shimmer-enabled by exposing tunable anchors. Shimmer can then load the site, tune its visible field, generate a reversible field seed, and export a restorable link.

The separation is important:

| Term | Role |
| --- | --- |
| Site | The projection surface. |
| Shimmer | The external tuning lab. |
| Field seed | Reversible state, used to restore the exact look. |
| Shimmerprint | One-way public trace or fingerprint. |
| Projection | An interpretation of seed, matrix, or state into a visual, semantic, or interactive form. |

A good short framing:

```text
Shimmer is not the sunset.
Shimmer is how the sunset travels.
```

## Why Shimmer Exists

Shimmer began as a color lab for the ULiUA sunlit field, but the architecture generalized.

Instead of embedding a full color lab into every project site, each site can expose a small manifest of tunable values. Shimmer reads that manifest, builds a control surface, and sends updates into the site through a bridge. The user can then keep the resulting look as a URL.

This makes it possible to shimmer-enable many sites without duplicating lab code everywhere.

## Current Use Case

A visitor opens a Shimmer Lab page, enters or loads a shimmer-enabled site, adjusts its exposed values, and receives:

- a reversible field seed
- a shimmerprint
- a restorable site link
- optional CSS variable export
- optional social copy

Example restorable link pattern:

```text
https://uliua.com/#shimmer=field:v1:<encoded-field-state>
```

A bare site reload returns to the site's default field. A shimmer link restores the chosen field.

## Field Seed vs Shimmerprint

A field seed returns you home.

It contains enough information to restore the exact visible or tunable state.

A shimmerprint does not return you home.

It is a one-way trace of the field state, useful for public sharing, identity, comparison, provenance, or growing a new field from the trace.

Canonical rule:

```text
Field seed returns you home.
Shimmerprint leaves a trace.
```

## Shimmer-Enabled Site Contract

A shimmer-enabled site needs only a small opt-in bridge.

The site should:

1. Define tunable anchors, often CSS variables.
2. Publish a manifest describing those anchors.
3. Listen for Shimmer messages.
4. Apply incoming values safely.
5. Read `#shimmer=` or `#field=` from its own URL when opened directly.
6. Optionally send current state back to the Shimmer host.

## Example Conceptual Manifest

```js
window.SHIMMER_MANIFEST = {
  name: "ULiUA",
  version: "1",
  variables: [
    {
      key: "--cream",
      label: "Cream",
      type: "color",
      default: "#fff7e6"
    },
    {
      key: "--sun-a",
      label: "Sun Opacity",
      type: "percent",
      min: 0,
      max: 100,
      default: 56
    },
    {
      key: "--speckle-dot-size",
      label: "Clover Dot Size",
      type: "px",
      min: 1,
      max: 40,
      default: 21
    }
  ]
};
```

## Bridge Script

The bridge script is the lightweight code included by shimmer-enabled sites.

Responsibilities:

- announce the site manifest to the parent Shimmer host
- receive variable updates through `postMessage`
- apply CSS variables to `document.documentElement`
- encode and decode field state
- restore state from URL hash
- optionally report current state back to the host

Core message pattern:

```js
window.addEventListener("message", (event) => {
  const data = event.data;
  if (!data || data.type !== "shimmer:setVars") return;

  for (const [key, value] of Object.entries(data.vars || {})) {
    document.documentElement.style.setProperty(key, value);
  }
});
```

Manifest announcement pattern:

```js
window.parent?.postMessage({
  type: "shimmer:manifest",
  manifest: window.SHIMMER_MANIFEST
}, "*");
```

In production, `targetOrigin` should be restricted instead of using `"*"` where possible.

## Host Lab

The Shimmer Host Lab is the external control surface.

Responsibilities:

- load a target site in an iframe
- detect whether the framed site is shimmer-enabled
- receive the site manifest
- generate controls from the manifest
- send live variable updates into the iframe
- generate field seed
- generate shimmerprint
- generate restorable site link
- export CSS variables
- optionally support raw matrix or projection tools later

The host lab should remain visually neutral. It may preview a site's projection, but it should not become that projection.

## Security and Browser Constraints

Shimmer cannot arbitrarily modify any website.

For cross-origin iframes, browser security prevents the host page from directly reading or changing the iframe DOM. Therefore, Shimmer needs opt-in cooperation through the bridge script.

There are two modes:

### Shimmer-enabled mode

The framed site includes the bridge and manifest. Shimmer can tune it live.

### Arbitrary URL mode

Shimmer may display the site if the site allows framing, but it cannot reliably tune it. Many sites also block iframe embedding through security headers.

## ULiUA Relationship

ULiUA is the first major projection surface.

ULiUA has its own default color field, top field-picker templates, shimmerprints, and ULiUA-specific lab controls. However, the long-term architecture should keep ULiUA and Shimmer separate:

- ULiUA presents the automeme and its sunlit/color field.
- Shimmer inspects, expands, translates, tunes, and exports field state.
- ULiUA can invite visitors to open the current field in Shimmer.
- Shimmer can open ULiUA as a projection surface.

## Current Prototype Lineage

The recent prototype line evolved through:

### Shimmer v0.2 - Mutant Fun

A standalone tiny-world seed lab with matrix generation, mutation buttons, field seed, shimmerprint, and ULiUA travel links.

### Shimmer v0.3 - Campfire Sunset

An exploratory prototype that folded place, light, and sunset into the field. This helped reveal that sunset belongs to the ULiUA projection, not Shimmer core.

### Shimmer v0.4 - Host Lab + Bridge

The architectural correction: Shimmer becomes an external neutral lab, with a bridge script and a demo shimmer-enabled site.

### ULiUA v9-v13

ULiUA proper gained top field templates, shimmerprints, a “Play or Hide - your choice” lab panel, hidden default field behavior, interactive shimmer invitations, and attractor glyph shortcut education.

## Code Components to Consolidate

Recommended modules:

```text
/shimmer-host-lab.html
/shimmer-bridge.js
/demo-shimmer-site.html
/lib/shimmer-codec.js
/lib/shimmer-hash.js
/lib/shimmer-manifest.js
/lib/shimmer-controls.js
/lib/shimmer-projections.js
```

### `shimmer-codec.js`

Handles field seed encoding, field seed decoding, URL-safe serialization, versioning, and validation.

### `shimmer-hash.js`

Handles shimmerprint generation, short display forms such as `shimmer:B45EB411`, and one-way trace generation.

### `shimmer-manifest.js`

Handles manifest parsing, default value extraction, type validation, and variable grouping.

### `shimmer-controls.js`

Handles generating sliders, color pickers, toggles, dropdowns, binding UI changes to state, and sending variable updates.

### `shimmer-projections.js`

Handles future projection modes: Raw Matrix, ULiUA Sunlit Field, Glyph Poster, Beach World, Rosetta Loop View, and Site Theme View.

## Minimal V1 Goal for ShimmeryMemory.com

The first stable version should do one thing beautifully:

```text
Load a shimmer-enabled site, tune its exposed variables, and produce a restorable link.
```

Minimum feature set:

- URL input
- iframe preview
- bridge detection
- manifest display
- generated control surface
- field seed output
- shimmerprint output
- copy restorable link
- copy CSS variables
- clear explanation of field seed vs shimmerprint

## Canonical Language

Use these as stable explanatory lines:

```text
Sites expose anchors. Shimmer tunes them. Seeds remember.
```

```text
A field seed returns you home. A shimmerprint leaves a trace.
```

```text
A site is a projection surface. Shimmer is the tuning instrument. The field seed is the portable state.
```

```text
Shimmer manipulates the seed. Projections interpret it. Sites embody it.
```

```text
Anything can become a seed. Not everything can return you home.
```

## Future Directions

Later, Shimmer can expand beyond colors:

- typography fields
- spacing and layout fields
- glyph posters
- merch mockups
- semantic matrices
- Rosetta Loop translation
- attractor glyph projections
- identity/protocol visualizations
- invariant-chain views
- seed-to-world generators

But V1 should remain small and fun.

The goal is not to prove the whole substrate immediately.

The goal is to make a tiny field portable enough that people want to play with it.
