# How To Read Open Source Agent Repositories

Open-source repositories are not just code samples. They are design documents hiding in plain sight.

This reading method helps learners extract engineering judgment from agent frameworks, MCP servers, RAG systems, evaluation tools, and observability projects.

## The 30-Minute Repository Reading Loop

| Minute | What to read | What to learn |
|---|---|---|
| 0-5 | README, quickstart, examples index | What the project thinks its smallest useful demo is |
| 5-10 | One minimal example | The core abstraction: agent, graph, task, chain, span, tool, or workflow |
| 10-15 | Configuration files | How the project expects users to declare state, tools, models, and integrations |
| 15-20 | Tests or eval examples | What behavior the maintainers consider important enough to protect |
| 20-25 | Error handling and logging code | What can go wrong in real usage |
| 25-30 | Issues, releases, migration notes | Whether the API and maintenance story fit your risk tolerance |

## What To Look For

### 1. The Smallest Primitive

Ask:

- Is everything an agent?
- Is the main unit a graph node, workflow step, task, tool, message, or span?
- Can you explain the primitive without naming the framework?

If you cannot explain the primitive, you are probably copying the tool instead of learning the design.

### 2. State And Memory

Ask:

- Where does state live between steps?
- Can the system resume after failure?
- Is memory user-specific, task-specific, shared, or global?
- What gets deleted, redacted, or summarized?

Good agent engineering treats memory as policy, not vibes.

### 3. Tool Boundaries

Ask:

- How are tool schemas declared?
- What validates tool inputs?
- Which tools require approval?
- Are tool results trusted, filtered, or treated as untrusted context?
- Is every tool call traceable?

A tool is not just a function. It is a permission boundary.

### 4. Evaluation

Ask:

- Are there regression tests for expected behavior?
- Are adversarial cases included?
- Can failures be reproduced?
- Are evals connected to CI?
- Does the project test refusal, no-answer, and bad-tool behavior?

If a repo has many demos but no evaluation story, treat it as a learning reference, not a production pattern.

### 5. Observability

Ask:

- Can you inspect every model call?
- Can you inspect every tool call?
- Are prompts, retrieved context, outputs, latency, cost, and errors recorded?
- Is sensitive data redacted?
- Can an incident be replayed?

In production, the question is not "did the agent answer?" The question is "can we explain what happened?"

### 6. Maintenance Risk

Ask:

- Is the project actively maintained?
- Are breaking changes documented?
- Are examples updated with the current API?
- Are issues answered?
- Is the license compatible with your use case?

Popular does not always mean stable. Stable does not always mean suitable.

## Repository Review Template

Use this when adding a project to the course or choosing a dependency:

```md
## Project

- Repository:
- Category:
- License:
- Last reviewed:

## Why It Matters

- Best learning value:
- Best production value:
- Matching roadmap modules:

## Core Abstractions

- Smallest primitive:
- State model:
- Tool model:
- Eval model:
- Observability model:

## Risks

- API stability:
- Operational risk:
- Security or privacy concern:
- Learning curve:

## Recommended Use

- Use for:
- Avoid for:
- First file/example to read:
```

## Reading Assignment

Pick one framework and one observability or eval project.

Deliver:

- one architecture sketch
- one list of core abstractions
- one limitation or risk
- one local course example that could be rewritten with the project
- one pull request idea for this roadmap

This turns open-source reading into visible learning progress.
