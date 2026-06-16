# 18 Agent Memory Governance

## Goal

Learn how to govern what agents remember, merge, redact, decay, and delete.

## Why It Matters

Memory is not just a vector database. Production memory is a governed data system.

An agent memory layer needs policies for:

- what can be stored
- what must be redacted
- what can become long-term memory
- what should expire
- how duplicate facts merge
- how confidence decays
- how users can request deletion
- how memory writes are audited

## Mental Model

```text
candidate memory
   ↓
classification
   ↓
redaction
   ↓
write / merge / reject
   ↓
decay / review / delete
```

The model may suggest a memory, but the governance layer decides whether it may be stored.

## Common Failure Modes

### Store Everything

The agent remembers sensitive, stale, or irrelevant information.

### Vector-Only Memory

The system can retrieve memories, but cannot explain who wrote them, why they exist, or when they should be deleted.

### No Merge Policy

Repeated facts become noisy duplicates.

### No Forget Policy

Users cannot remove sensitive or outdated memories.

## Practical Exercise

Run:

```bash
python examples/15-memory-governance-agent/main.py
```

Inspect how the example redacts contact information, merges a repeated preference, decays confidence, and deletes session PII.

## Production Checklist

- [ ] Memory categories are explicit
- [ ] PII is redacted before storage
- [ ] Long-term memory requires a reason
- [ ] Memory writes are audited
- [ ] Duplicate facts merge
- [ ] Confidence can decay
- [ ] Users can request deletion
- [ ] Memory retrieval respects scope and sensitivity

