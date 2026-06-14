# Chinese Learning Sources Research Plan

[繁體中文](chinese-learning-sources_zh.md)

## Purpose

This document tracks Chinese learning materials that can inspire original English teaching content for this repository.

The goal is **not** to translate or copy articles directly. Instead, we use public Chinese tutorials, videos, discussions, and technical posts as references to understand how learners ask questions, what concepts are difficult, and what examples are useful.

---

## Source Types to Research

- Zhihu articles and discussions
- Bilibili technical tutorials
- WeChat technical posts
- Chinese GitHub repositories
- Chinese developer blogs
- Chinese AI community notes

---

## Topics to Collect

### Agent Basics

Look for materials about:

- what an AI Agent is
- ReAct pattern
- tool calling
- planning and execution
- agent loop

### MCP

Look for materials about:

- Model Context Protocol introduction
- MCP client and server examples
- filesystem MCP
- database MCP
- browser/search MCP
- MCP security risks

### Memory

Look for materials about:

- long-term memory
- vector database memory
- user profile memory
- multi-agent shared memory
- memory pollution
- memory governance

### Workflow and LangGraph

Look for materials about:

- LangGraph state machine
- graph-based agent workflow
- planner-executor-reviewer pattern
- retry and fallback
- human-in-the-loop

### Multi-Agent Systems

Look for materials about:

- CrewAI
- AutoGen
- LangGraph multi-agent
- supervisor-worker pattern
- debate agents
- role specialization

### Production Agent Systems

Look for materials about:

- agent evaluation
- RAG evaluation
- tracing and observability
- Langfuse
- prompt injection
- tool permission control

---

## How to Convert Chinese Sources into Original English Teaching Material

Use this transformation process:

```text
Chinese source
   ↓
Extract concepts, learner questions, and examples
   ↓
Remove original wording and structure
   ↓
Create an original English explanation
   ↓
Add hands-on tasks
   ↓
Add diagrams and checklists
   ↓
Add attribution as reference, not copied content
```

---

## Content Transformation Template

For each source, record:

```text
Source title:
Source URL:
Platform:
Topic:
Key ideas:
Learner pain points:
Example used:
How to transform into original English lesson:
Potential exercise:
Reference status:
```

---

## Candidate English Lesson Types

- Concept explanation
- Architecture walkthrough
- Step-by-step tutorial
- Hands-on coding lab
- Debugging guide
- Comparison table
- Safety checklist
- Production design pattern

---

## Initial Research Notes

Current public search results suggest the most useful content clusters are:

1. MCP as the integration layer between agents and external tools.
2. LangGraph as a workflow/state-machine framework for controllable agents.
3. Agent memory as a separate design problem, not just vector search.
4. Multi-agent systems as role-based workflows, not agent roleplay.
5. Production safety around tool permissions, prompt injection, and memory governance.

---

## Copyright Policy

Do not copy Chinese articles or video transcripts directly.

Allowed:

- summarize high-level ideas
- cite source links
- create original explanations
- create original diagrams
- create new code examples
- create new exercises

Not allowed:

- direct translation of full articles
- copying tutorial structure line-by-line
- reusing screenshots without permission
- copying code without license verification
- removing attribution
