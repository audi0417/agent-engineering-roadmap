# Templates

Reusable templates for agent engineering projects.

好，那 templates 的用途是什麼呢？其實就是讓你在寫第一行 model call 以前，先把系統邊界想清楚而已。

Start with these files:

| Template | Use when |
|---|---|
| `agent-spec-template.md` | Designing a new agent |
| `memory-policy-template.md` | Deciding what an agent can remember |
| `evaluation-suite-template.yaml` | Creating regression tests and scoring rubrics |
| `safety-gate-template.md` | Adding approval and refusal rules |
| `mcp-server-template.py` | Sketching a minimal MCP-style tool server |

## Suggested order

1. Fill in `agent-spec-template.md`.
2. Define allowed actions and human approval gates.
3. Add memory policy only after the task needs memory.
4. Write at least 10 evaluation cases.
5. Build a minimal example and run the eval suite before adding more tools.

The important point: do not start with a giant prompt. Start with the task contract.
