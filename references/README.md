# References

[繁體中文](README_zh.md)

This folder collects public references that support the Agent Engineering Roadmap.

References are used to improve educational quality, not to copy content. Lessons in this repository should remain original explanations, original examples, and original diagrams.

---

## Core Research References

| Area | Reference | Year | Use in this repository |
|---|---|---:|---|
| Reasoning + Acting | ReAct: Synergizing Reasoning and Acting in Language Models | 2022 | Supports the idea that agents combine reasoning steps with actions against external tools or environments. |
| Agent Reliability | On the Brittle Foundations of ReAct Prompting for Agentic Large Language Models | 2024 | Reminds learners that prompting patterns can be brittle and should be evaluated rather than trusted blindly. |
| Multi-Agent Systems | Multi-Agent Collaboration Mechanisms: A Survey of LLMs | 2025 | Supports the curriculum modules on multi-agent structures, roles, and coordination protocols. |
| Agent Memory | Memory for Autonomous LLM Agents: Mechanisms, Evaluation, and Emerging Frontiers | 2026 | Supports memory design, write/read loops, memory governance, and evaluation. |

---

## MCP References

| Area | Reference | Use in this repository |
|---|---|---|
| MCP concept | Model Context Protocol public documentation and ecosystem descriptions | Supports the MCP-style client/server architecture used in Example 03. |
| MCP risks | Recent public security reports on MCP-style integrations | Supports the production safety and tool permission sections. |

---

## How to Use References

Each curriculum module should eventually include a short `References` section.

Good references should support:

- a concept
- a design pattern
- a known limitation
- a safety concern
- an evaluation method

References should not be used to copy article structure or text.

---

## Citation Style

Use short, readable references:

```text
- Yao et al. (2022), ReAct: Synergizing Reasoning and Acting in Language Models.
```

When the document is a tutorial or code example, citations should be placed near the end under `References`.

---

## Reference Expansion Plan

Planned categories:

- Tool use and function calling
- RAG and retrieval evaluation
- Agent memory
- Workflow orchestration
- Multi-agent systems
- Human-in-the-loop systems
- Agent evaluation
- MCP and tool security
- Healthcare AI safety
- Finance AI risk controls
