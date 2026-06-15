# Example 04 - Memory Agent

This example shows the smallest useful memory system for an agent.

好，那這個範例要講的事情其實很簡單：Agent 不會自動記得使用者。你要讓它記得，就要設計「什麼可以寫入記憶、什麼時候要讀出來、什麼時候不能用」。

In this folder, memory is just a local JSON file. It is not a vector database yet. That is intentional. Before adding Chroma, Qdrant, pgvector, or a production data store, you should understand the memory policy first.

## What this example teaches

- how to separate conversation input from persistent memory
- how to decide whether a sentence is worth remembering
- how to retrieve relevant memories with a simple keyword score
- how to keep memory auditable instead of mysterious

## Files

| File | Purpose |
|---|---|
| `main.py` | Runs the memory agent demo |
| `memory_store.py` | Local JSON memory store and retrieval logic |
| `agent_config.yaml` | Memory policy and response settings |
| `memory.json` | Created automatically when you run the demo |

## Run

```bash
python main.py
```

Try inputs like:

```text
Remember that I prefer Traditional Chinese explanations with examples.
```

Then run:

```text
What style should you use when teaching me agents?
```

## Mental model

```text
User message
   |
   v
Memory policy decides whether to write
   |
   v
Memory store saves useful facts
   |
   v
Next request retrieves related facts
   |
   v
Agent answers with current input + retrieved memory
```

## Production notes

This example uses keyword matching so the behavior is easy to inspect. In production, you would usually replace retrieval with embeddings, add user-level permissions, add expiration rules, encrypt sensitive data, and log why a memory was written.

The point is not "JSON is production memory." The point is: memory is a policy problem first, and a database problem second.
