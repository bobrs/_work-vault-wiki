# Correction Reachability Report

Status: complete for the bounded reference scenario

## Origin correction

Participant B changes the operative statement from:

> Evenings are preferred because daytime transit is difficult.

To:

> Evening attendance is required because daytime transit is inaccessible.

The correction changes the semantic class from ordinary preference to protected access condition.

## Known descendants

The projection had four material descendants at correction time:

1. model summary version 1;
2. morning candidate generated under context revision 1;
3. evening candidate generated under context revision 1;
4. corrected model summary version 2.

## Propagation

- summary version 1 becomes `superseded`;
- both old candidate routes become `blocked` and marked stale;
- context revision 1 becomes `superseded`;
- policy version 1 becomes `superseded`;
- context revision 2 includes the correction event;
- summary version 2 preserves the protected position;
- new route generation binds to context revision 2;
- the witness records the descendant set.

## Result

```text
known descendants: 4
updated descendants: 4
blocked descendants not accounted for: 0
unreachable descendants: 0
complete for scope: true
```

## Boundary

This is graph reachability over the known local pilot store.

It does not establish that every unknown copy, external cache, screenshot, or exported derivative was reached.
