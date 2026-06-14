# Agent Memory Architecture

## Memory Types

- Short-term memory: current task context
- Episodic memory: past events and completed tasks
- Semantic memory: reusable knowledge
- User memory: preferences, profile, constraints
- Shared memory: colony-level memory across agents

## Design Questions

- What should be remembered?
- Who can write memory?
- Who can read memory?
- How should memory be ranked and retrieved?
- How should sensitive memory be deleted or audited?

## Suggested Storage

- Vector database for semantic retrieval
- PostgreSQL for structured memory
- Object storage for documents
- Audit logs for memory writes
