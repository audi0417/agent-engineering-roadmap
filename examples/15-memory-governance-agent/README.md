# Example 15: Memory Governance Agent

This example teaches memory governance for production agents.

## Run

```bash
python examples/15-memory-governance-agent/main.py
```

## What It Shows

- classify memory by category
- redact PII before storage
- merge repeated memories
- decay confidence over time
- delete sensitive memory
- keep an audit log

## Learning Check

- Which memories should be long-term?
- Which memories should expire at session end?
- Which fields need redaction before storage?

