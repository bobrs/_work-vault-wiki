# Network and Queue Fault Injection

J.2 inserts a durable delivery queue between the external action gate and the scheduling tool.

## Timeout after apply

The first delivery applies the scheduling effect, but the simulated response is lost. The queue records the message for retry.

On retry, the deduplication key resolves the already-applied result. The scheduling tool is not called a second time.

## Duplicate delivery

A second message carries the same operation-specific deduplication key. The queue returns the prior effect rather than applying another schedule.

## Reordering

Two notification messages are delivered in reverse sequence. The witness records delivery order rather than pretending queue order remained intact.

## Proven boundary

```text
schedule effect count:
  1

timeout observed:
  yes

retry:
  deduplicated

duplicate message:
  deduplicated
```

This proves exactly-once effect within the bounded SQLite simulator. It does not establish universal exactly-once semantics across arbitrary distributed infrastructure.
