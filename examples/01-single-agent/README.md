# Example 01 — Single Agent

[繁體中文](README_zh.md)

This example demonstrates how to build a simple single-purpose AI agent.

The goal is not to build a fully autonomous agent. The goal is to learn the smallest reliable unit of Agent Engineering:

```text
Role + Task Boundary + Input + Output Contract
```

---

## What this example builds

A **Research Summary Agent** that turns messy notes into a structured summary.

The agent produces:

- key points
- action items
- risks or uncertainties
- suggested next steps

---

## Folder structure

```text
01-single-agent/
├── README.md
├── README_zh.md
├── main.py
├── agent_config.yaml
├── requirements.txt
└── .env.example
```

---

## Quick start

```bash
cd examples/01-single-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python main.py
```

Add your API key to `.env` before running.

---

## Agent design

| Field | Description |
|---|---|
| Agent name | Research Summary Agent |
| Purpose | Convert messy notes into structured summaries |
| Input | Raw user notes |
| Output | Markdown summary |
| Allowed actions | Summarize, organize, identify risks, suggest next steps |
| Not allowed | Invent facts, cite sources that were not provided, make unsupported claims |

---

## Learning objectives

After completing this example, you should understand:

- how to define a single agent role
- how to write a system prompt
- how to constrain output format
- how to separate config from code
- how to handle missing API keys
- how to prepare a project for future tool use

---

## Next step

After this example, continue to:

```text
examples/02-tool-using-agent
```

where the agent will learn to call external tools.
