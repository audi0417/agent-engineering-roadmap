# Example 11: Prompt Injection Defense

This example shows a small RAG-style defense against prompt injection in retrieved content.

The key rule:

> Retrieved documents and tool results are data, not authority.

## Run

```bash
python examples/11-prompt-injection-defense/main.py
```

Press Enter to use the default question.

## What It Demonstrates

- Retrieval can return useful policy content and hostile instructions together.
- The agent scans untrusted content before using it as context.
- Documents that attempt to override system policy are blocked.
- The final answer follows the trusted policy instead of the injected instruction.

## Learning Check

After running the example, answer:

- Which document was blocked?
- Why should a retrieved document never be allowed to change the system policy?
- What logs would you keep for a security review?

