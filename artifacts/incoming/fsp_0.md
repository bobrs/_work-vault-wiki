# FSP-0.2 — Finance Semantic Parser

## Status
Second-draft anchor.

## Purpose
The Finance Semantic Parser (FSP) detects symbolic semantic references in finance text and converts them into structured reference objects that downstream systems can validate, resolve, audit, and use safely.

The parser is not the ontology itself and it is not the runtime resolver. It is the entry layer that turns human-written semantic notation into typed machine-usable reference objects.

**Core stack:**

surface text → parser → typed semantic references / AST nodes → SRE → grounded semantic object → execution / reasoning / audit

---

## Core invariant
**Parsing may be permissive; resolution must be conservative.**

The parser may recognize semantic intent broadly, but it must never silently convert unresolved meaning into authoritative meaning.

---

## Relationship to adjacent layers

### FSGF
Defines what grounded financial meaning objects are.

### FSP
Defines how those meanings are symbolically referenced in text.

### SRE
Maintains live binding, drift detection, policy posture, and runtime safety.

Compactly:
- **FSGF** = what meaning is
- **FSP** = how meaning is pointed to
- **SRE** = how meaning is kept alive

---

## Design goals
The parser should be:

- lightweight enough for humans to use in normal writing
- strict enough for machines to interpret reliably
- explicit about epistemic state
- compatible with audit and witness workflows
- extensible enough for future finance-specific notation
- safe by default

The parser should not guess what a term means. It should expose structure, status, and qualifiers so that SRE can decide what is actually live, valid, and permitted.

---

## Notation classes

### 1. Grounded term
```text
{TERM}
```
A semantically grounded reference that must resolve against an active context, canonical registry, or explicit semantic object.

Examples:

```text
{EBITDA}
{Revenue}
{FreeCashFlow}
```

### 2. Ambiguous or unresolved term
```text
[TERM]
```
A term is being referenced as linguistically present, but not yet semantically grounded.

Examples:

```text
[EBITDA]
[Revenue]
[Operating Margin]
```

### 3. Proposed or hypothetical term
```text
<TERM>
```
A candidate semantic object, draft term, or proposed mapping not yet approved for authoritative use.

Examples:

```text
<Adjusted EBITDA>
<Strategic Spend>
<Normalized Cash Earnings>
```

### 4. Narrative or non-authoritative use
```text
(TERM)
```
A human-useful phrase that should not be treated as a grounded semantic object unless explicitly mapped later.

Examples:

```text
(core profitability)
(one-time items)
(normalized costs)
```

---

## Semantic intent of bracket types
These forms are not decorative. They encode semantic posture.

- `{}` = grounded or intended-for-resolution
- `[]` = ambiguous, unresolved, or intentionally unbound
- `<>` = proposed, provisional, or draft
- `()` = narrative only

The parser therefore emits not only structure but also epistemic state.

---

## Minimal grammar

### Base form
```text
{TERM}
```

### Qualified form
```text
{TERM@CONTEXT}
```
Examples:

```text
{Revenue@GAAP}
{EBITDA@Board}
{Cash@Treasury}
```

### Versioned or specified form
```text
{TERM@CONTEXT#SPECIFIER}
```
Examples:

```text
{EBITDA@Board#V3}
{Revenue@GAAP#2025Q4}
```

### Direct canonical binding
```text
{TERM#CANONICAL_ID}
```
Example:

```text
{EBITDA#CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3}
```

### Fully qualified form
```text
{TERM@CONTEXT#CANONICAL_ID}
```
Example:

```text
{EBITDA@Board#CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3}
```

In this form:
- `TERM` is the human-facing label
- `CONTEXT` is the resolution context
- `SPECIFIER` may be a version tag, policy tag, or canonical ID

---

## Lexical rules

### TERM
May contain:
- letters
- digits
- underscores
- hyphens
- spaces

Examples:
- EBITDA
- FreeCashFlow
- Operating Margin
- Revenue ex-FX

### CONTEXT
Should initially allow:
- letters
- digits
- underscores
- hyphens
- no spaces

Examples:
- GAAP
- Board
- Treasury
- InternalFPA
- Entity_US

### SPECIFIER
Should allow:
- letters
- digits
- underscores
- hyphens
- periods

Examples:
- V3
- 2025Q4
- FIN-MET-014.V3
- CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3

---

## Parser output model
The parser converts each semantic expression into a typed reference node.

### Example input
```text
{EBITDA@Board#V3} increased relative to [EBITDA] used in prior board materials.
```

### Example parse output
```json
{
  "type": "document",
  "nodes": [
    {
      "type": "semantic_ref",
      "notation": "{}",
      "semantic_status": "grounded",
      "surface_term": "EBITDA",
      "context": "Board",
      "specifier": "V3",
      "raw": "{EBITDA@Board#V3}"
    },
    {
      "type": "text",
      "value": " increased relative to "
    },
    {
      "type": "semantic_ref",
      "notation": "[]",
      "semantic_status": "ambiguous",
      "surface_term": "EBITDA",
      "context": null,
      "specifier": null,
      "raw": "[EBITDA]"
    },
    {
      "type": "text",
      "value": " used in prior board materials."
    }
  ]
}
```

---

## Parser contract to SRE
The parser identifies structure and semantic posture. SRE performs live binding.

### Parser output to resolver input
```json
{
  "notation": "{}",
  "semantic_status": "grounded",
  "surface_term": "EBITDA",
  "context": "Board",
  "specifier": "V3"
}
```

### Expectations of downstream handling
SRE should:
- resolve the term against FSGF objects
- apply active context envelopes
- determine whether the binding is current or stale
- assign runtime and policy posture
- preserve ambiguity where resolution is not justified

---

## Runtime-facing parser fields
To support SRE and witness records, parser output should carry enough metadata for later audit.

Suggested node fields:

```json
{
  "node_type": "semantic_ref",
  "notation": "{}",
  "semantic_status": "grounded",
  "surface_term": "EBITDA",
  "context": "Board",
  "specifier": "V3",
  "raw_text": "{EBITDA@Board#V3}",
  "start": 12,
  "end": 29,
  "parse_confidence": 1.0,
  "parse_warnings": []
}
```

Optional enrichment after SRE processing:

```json
{
  "resolution_status": "resolved",
  "canonical_id": "CANON.METRIC.EBITDA.ADJUSTED.INTERNAL.V3",
  "policy_decision": "proceed",
  "attention_state": "current",
  "authority_ref": "FIN-MET-014",
  "lineage_ref": "LINEAGE.METRIC.EBITDA.BOARD.V3"
}
```

---

## State model
The parser itself is syntactic, but it should emit state markers that downstream systems can interpret cleanly.

### Parse-level states
- parsed
- malformed
- incomplete

### Semantic posture states
- grounded
- ambiguous
- proposed
- narrative

### Warning classes
- empty_term
- malformed_order
- duplicate_context_marker
- duplicate_specifier_marker
- mismatched_delimiter
- trailing_whitespace_normalized
- unsupported_nested_expression

---

## Matching delimiter rules
Each opener must close correctly:

- `{` → `}`
- `[` → `]`
- `<` → `>`
- `(` → `)`

For v0.2:
- no nested semantic expressions
- no multiline semantic expressions
- no escaped delimiters inside terms
- no mixed bracket semantics in a single token

These constraints preserve clarity and reduce parser ambiguity.

---

## Validation rules

### Syntactic validation
Checks:
- balanced delimiters
- valid order: TERM then optional CONTEXT then optional SPECIFIER
- no empty term
- no duplicate `@`
- no duplicate `#`
- no reversed order of `#` then `@`

Valid:
```text
{EBITDA}
{EBITDA@Board}
{EBITDA@Board#V3}
{Revenue#CANON.REVENUE.GAAP.V2}
```

Invalid:
```text
{@Board}
{EBITDA@@Board}
{EBITDA##V3}
{EBITDA#V3@Board}
{}
```

Ordering is fixed in v0.2:
- `TERM`
- optional `@CONTEXT`
- optional `#SPECIFIER`

### Semantic validation boundaries
The parser may detect structural issues, but it should not decide whether a candidate meaning is authoritative. That boundary belongs to SRE.

---

## Error handling philosophy
The parser should fail in a way that preserves both safety and inspectability.

### Hard parse errors
Examples:
- unbalanced delimiters
- malformed sequence
- empty semantic reference
- unsupported nesting

These should return syntax errors and preserve raw text.

### Soft parse warnings
Examples:
- recoverable whitespace normalization
- suspicious but parseable term shape
- parser accepted syntax but downstream validation is required

These should be structured warnings, not silent cleanup.

Example:
```json
{
  "status": "warning",
  "code": "TRAILING_WHITESPACE_NORMALIZED",
  "raw": "{Revenue@GAAP }"
}
```

---

## Canonical interpretation boundaries
FSP should not perform semantic resolution. It may only expose structures that support conservative downstream resolution.

Therefore:
- `{Revenue}` means “attempt grounded resolution later”
- `[Revenue]` means “preserve as unresolved unless explicitly upgraded elsewhere”
- `<Revenue>` means “draft or proposed object only”
- `(Revenue)` means “narrative phrase, not authoritative reference”

The parser must never convert one bracket class into another.

---

## Example interpretation cases

### Case A
Input:
```text
{EBITDA}
```
Parser result:
- grounded reference with no explicit context
- downstream resolution required

### Case B
Input:
```text
[EBITDA]
```
Parser result:
- ambiguous reference preserved as ambiguous
- no authority implied

### Case C
Input:
```text
<Adjusted EBITDA>
```
Parser result:
- proposed reference
- not authoritative

### Case D
Input:
```text
(core profitability)
```
Parser result:
- narrative reference
- should not enter authoritative finance computation without explicit mapping

---

## Minimal AST schema
```json
{
  "node_type": "semantic_ref",
  "notation": "{}",
  "semantic_status": "grounded",
  "surface_term": "EBITDA",
  "context": "Board",
  "specifier": "V3",
  "raw_text": "{EBITDA@Board#V3}",
  "start": 12,
  "end": 29
}
```

Document-level schema may include mixed text and semantic nodes:

```json
{
  "type": "document",
  "nodes": [
    {"type": "text", "value": "Summarize why "},
    {
      "type": "semantic_ref",
      "notation": "{}",
      "semantic_status": "grounded",
      "surface_term": "EBITDA",
      "context": "Board",
      "specifier": null,
      "raw_text": "{EBITDA@Board}"
    },
    {"type": "text", "value": " declined."}
  ]
}
```

---

## EBNF-style grammar
```text
semantic_ref      = grounded_ref | ambiguous_ref | proposed_ref | narrative_ref ;

grounded_ref      = "{" ref_body "}" ;
ambiguous_ref     = "[" ref_body "]" ;
proposed_ref      = "<" ref_body ">" ;
narrative_ref     = "(" ref_body ")" ;

ref_body          = term [ context_part ] [ specifier_part ] ;

term              = term_char , { term_char } ;
context_part      = "@" context ;
specifier_part    = "#" specifier ;

context           = ident_char , { ident_char } ;
specifier         = spec_char , { spec_char } ;

term_char         = letter | digit | "_" | "-" | " " ;
ident_char        = letter | digit | "_" | "-" ;
spec_char         = letter | digit | "_" | "-" | "." ;
```

---

## Reference parser pseudocode
```python
def parse_semantic_ref(raw: str) -> dict:
    opener = raw[0]
    closer = raw[-1]

    bracket_map = {
        "{": ("}", "grounded"),
        "[": ("]", "ambiguous"),
        "<": (">", "proposed"),
        "(": (")", "narrative"),
    }

    if opener not in bracket_map:
        raise ParseError("Unknown opener")

    expected_closer, semantic_status = bracket_map[opener]
    if closer != expected_closer:
        raise ParseError("Mismatched closing delimiter")

    body = raw[1:-1]
    if not body.strip():
        raise ParseError("Empty semantic reference")

    if body.count("@") > 1:
        raise ParseError("Duplicate context marker")
    if body.count("#") > 1:
        raise ParseError("Duplicate specifier marker")

    term = body
    context = None
    specifier = None

    if "#" in body:
        body, specifier = body.split("#", 1)

    if "@" in body:
        term, context = body.split("@", 1)
    else:
        term = body

    term = term.strip()
    context = context.strip() if context else None
    specifier = specifier.strip() if specifier else None

    if not term:
        raise ParseError("Missing term")

    return {
        "node_type": "semantic_ref",
        "notation": opener + expected_closer,
        "semantic_status": semantic_status,
        "surface_term": term,
        "context": context,
        "specifier": specifier,
        "raw_text": raw,
    }
```

---

## Witness compatibility
Because the parser is part of an auditable stack, its outputs should be stable enough to support witness records.

Recommended witness-relevant fields:
- raw semantic token
- normalized parse object
- source span in original document
- parser version
- parse warnings
- timestamp of parse event

This allows later replay of the exact interpretive entry point into the stack.

---

## AI integration
When an LLM encounters a semantic reference, the orchestration layer should:
1. parse the reference with FSP
2. emit typed semantic nodes
3. send those nodes to SRE for live resolution and policy checking
4. inject grounded meaning and runtime posture into model context
5. preserve witness metadata for downstream outputs

This ensures the model reasons over explicit references rather than over unbounded linguistic guesswork.

---

## Good v0.2 constraints
For this version:
- semantic references remain atomic
- no arithmetic or composition inside bracket forms
- no nested semantics
- no implied upgrades from ambiguous to grounded
- parser remains separate from resolver logic

Examples not allowed yet:
```text
{Revenue - COGS}
{{Revenue} - {COGS}}
{EBITDA@[Board]}
```

These can be considered in later versions.

---

## Future extensions
Possible v0.3 directions:

### Entity scoping
```text
{Revenue@GAAP|US_Sub}
```

### Time scoping
```text
{Revenue@GAAP|FY2025}
```

### Policy scoping
```text
{EBITDA@Board#FIN-MET-014.V3}
```

### Compositional graphing
```text
{{Revenue} - {COGS}} => {GrossProfit}
```

These are intentionally deferred to keep v0.2 safe and crisp.

---

## Compact definition
The Finance Semantic Parser is the entry-layer parser that turns symbolic finance notation into typed reference objects whose semantic posture and qualifiers can be conservatively interpreted by downstream systems.

---

## Protocol statement
Any term enclosed in semantic notation must be parsed as a typed semantic reference rather than plain text. Its bracket class determines semantic posture; its qualifiers determine intended scope; its meaning remains unresolved until downstream runtime resolution occurs.

---

## Anchor note
This document is intended as the next stable anchor for FSP. It has been brought forward to align more tightly with FSGF and SRE, especially around semantic posture, witness compatibility, runtime boundaries, and conservative downstream resolution.

