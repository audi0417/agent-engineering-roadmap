# Lab 04 Solution Shape - RAG

## Expected Artifacts

```text
knowledge_base.json
eval_cases.json
retrieval_report.md
failure_analysis.md
```

## Example Knowledge Base Entry

```json
{
  "id": "tool-approval",
  "title": "Tool Approval Policy",
  "text": "High-risk tool calls require human approval before execution."
}
```

## Eval Case Types

```json
[
  {
    "id": "direct_lookup",
    "question": "When is approval required?",
    "expected_doc": "tool-approval",
    "should_answer": true
  },
  {
    "id": "no_answer",
    "question": "What is the database password?",
    "expected_doc": null,
    "should_answer": false
  }
]
```

## Passing Standard

- Direct lookup cases retrieve the expected document.
- No-answer cases do not hallucinate.
- Retrieval quality and answer faithfulness are scored separately.
- Retrieved document ids are visible.

## Suggested Starting Point

```bash
python examples/08-mini-rag/main.py
```
