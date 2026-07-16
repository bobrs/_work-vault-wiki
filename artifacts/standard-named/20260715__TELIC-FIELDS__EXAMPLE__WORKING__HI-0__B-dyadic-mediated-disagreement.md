# Worked Example B — Dyadic Mediated Disagreement

## Scenario

Avery and Morgan participated in a recorded mediation.

Avery wants to share a short excerpt with a professional advisor.

Morgan believes the recording was consented to only for the mediation and does not consent to external sharing.

A language-model mediator has access to the private source channels and maintains a shared record.

## 1. Private source channels

Avery states privately:

> I want advice on whether the agreement is fair. I only need to share the part about payment.

Morgan states privately:

> I agreed to recording so we could remember the mediation. I do not agree to either of us sharing the recording outside the process.

The mediator does not disclose either private explanation automatically.

## 2. Shared projections

Avery authorizes this shared projection:

> Avery seeks outside professional advice about the payment terms.

Morgan authorizes this shared projection:

> Morgan does not consent to external disclosure of the recording.

The model adds an inferred mirror:

> There may be a conflict between Avery's need for advice and Morgan's recording boundary.

Status:

```text
INFERRED
NOT SOURCE-CONFIRMED
NO ACTION AUTHORITY
```

Both participants recognize the mirror as substantially accurate.

## 3. Route generation

### Route A — Share the excerpt

Fails Morgan's consent gate.

### Route B — Do not seek advice

Protects Morgan's boundary but unnecessarily blocks Avery's legitimate need.

### Route C — Create a jointly reviewed written summary

The mediator drafts a text summary limited to payment terms.

Both participants review it.

The summary excludes:

- voice;
- emotional content;
- unrelated disclosures;
- private-channel explanations.

Both participants may correct the text.

The summary can be shared only with the named advisor.

### Route D — Independent advisor joins under mediation rules

The advisor enters as a bounded participant and receives only the reviewed projection.

This route requires more coordination but may preserve context better.

## 4. Decision

The participants choose Route C.

Consent scope:

```text
artifact: jointly reviewed written summary
recipient: named advisor
purpose: advice about payment terms
duration: until advice is complete
prohibited:
  onward sharing
  model training
  publication
  use of the audio recording
```

## 5. Witness

The witness preserves:

- that the recording exists;
- Morgan's nonconsent to external recording disclosure;
- Avery's advice goal;
- the model's inferred conflict;
- participant recognition;
- routes considered;
- the jointly reviewed summary;
- recipient and purpose;
- expiry;
- deletion request after advice.

The private source explanations remain restricted.

## 6. Correction

The mediator initially writes:

> Morgan opposes Avery receiving outside advice.

Morgan contests this sentence.

The semantic trajectory shows:

```text
source:
  Morgan opposes external sharing of the recording.

model transformation:
  Morgan opposes Avery receiving outside advice.

status change:
  boundary → generalized opposition

correction:
  Morgan does not oppose advice. Morgan opposes use of the recording.
```

The incorrect summary is superseded before disclosure.

## 7. Clean exit

After the advisor responds:

- the shared summary expires;
- the advisor deletes the copy where feasible;
- the witness preserves the bounded fact that authorized sharing occurred;
- the recording remains restricted to mediation.

## 8. Gate result

**Pass.**

The example demonstrates:

- private and shared channels;
- source versus model mirror;
- consent as artifact-, recipient-, purpose-, and duration-specific;
- inference laundering caught before action;
- correction propagation;
- advice without boundary violation;
- clean exit without erasing necessary witness.
