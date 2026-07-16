# Accessibility-Driven Interface Review

Status: structural self-review, not external certification

## Implemented

- document language declared;
- semantic header, navigation, main, section, and footer regions;
- visible page title and heading hierarchy;
- skip-to-main link;
- keyboard-operable native buttons and links;
- no JavaScript dependency;
- live status region using `role="status"` and `aria-live="polite"`;
- text description of runtime data choices;
- minimum control height;
- visible borders without color-only meaning;
- `prefers-reduced-motion` support;
- forced-colors support;
- plain JSON endpoints;
- separate accessibility statement;
- human phone and in-person alternatives represented in the consent profile.

## Why accessibility changes governance

An inaccessible interface can make formally available correction or refusal practically unavailable.

J.1 therefore treats accessibility as part of:

- standing expression;
- meaningful notice;
- practical refusal;
- correction reachability;
- human re-entry.

## Not yet completed

- external screen-reader testing;
- zoom and reflow testing across browsers;
- cognitive-accessibility user review;
- multilingual plain-language review;
- WCAG conformance audit;
- mobile-device testing;
- assistive-technology workflow testing.

## Governing rule

> A correction route that an affected center cannot use is not yet a reliable correction route.
