# Memory Policy Template

## Goal

Define what the agent may remember, retrieve, update, and delete.

Memory is not "put everything in a database." Memory is a permissioned context layer.

## Memory Types

| Type | Store? | Example | Expiration | Approval |
|---|---|---|---|---|
| User preference | yes | Prefers Traditional Chinese | until changed | no |
| Project fact | yes | Project uses FastAPI | project lifetime | no |
| Task state | yes | Step 3 of workflow complete | task lifetime | no |
| Sensitive data | no by default | API key, password, diagnosis | none | explicit |
| Tool result | maybe | Search result or DB lookup | short | depends |

## Write Rules

Store memory only when:

- it will likely help future tasks
- it is stable enough to reuse
- the user explicitly asks to remember it, or the system has a clear reason
- it does not violate privacy, safety, or domain policy

## Retrieval Rules

Retrieve memory only when:

- it is relevant to the current task
- it does not override the user's latest instruction
- it is not stale
- it is safe to use in the current context

## Delete Rules

Delete memory when:

- the user asks to forget it
- it is wrong or outdated
- it is sensitive and no longer needed
- retention policy expires

## Audit Log

Each memory write should record:

```text
memory_id:
user_id:
text:
reason:
source:
created_at:
expires_at:
review_required:
```
