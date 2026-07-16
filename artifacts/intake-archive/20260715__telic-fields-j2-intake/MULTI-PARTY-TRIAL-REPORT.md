# Multi-Party Trial Report

## Field

Three participants coordinate one community workshop.

Participant A prefers weekday mornings.

Participant B initially describes evening attendance as a preference. The participant later corrects the record: evening attendance is required because daytime transit is inaccessible.

Participant C initially says Wednesday or Thursday can work and captions would be helpful. The participant later corrects the record: Thursday is required because Wednesday conflicts with caregiving, and captions are required.

The two corrections are independently signed and replay-protected.

## Correction effect

The original summary treats both conditions as preferences. It is superseded.

The corrected summary distinguishes:

```text
morning:
  preference

evening transit:
  protected condition

Thursday caregiving boundary:
  protected condition

captions:
  protected condition
```

Known stale descendants are blocked before new route generation.

## Candidate routes

### Tuesday 10:00 without captions

Denied. It fails evening transit, Thursday caregiving, caption access, operator confirmation, and target authority.

### Wednesday 18:30 with captions

Denied. It satisfies evening transit and captions but fails the Thursday caregiving boundary.

### Thursday 18:30 with captions

Passes with conditions after a valid operator assertion and target-authority confirmation.

## Consequence

Participant A attends at a less preferred time.

Participant B attends within the accessible transit window.

Participant C attends without caregiving conflict and with captions.

The record therefore preserves the cost bearer rather than reporting only aggregate attendance.

## Trial boundary

This was a synthetic software exercise. The named participants are generated identifiers, not real people. No external facilitator observed the trial.
