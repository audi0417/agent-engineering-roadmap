# Agent Framework Selection Matrix

This guide helps learners choose an open-source agent framework by engineering need instead of popularity.

Use it after reading [Open Source Agent Projects](open-source-agent-projects.md). The goal is not to crown one winner. The goal is to know which tradeoff you are accepting.

## Quick Decision Table

| If you need | Start with | Why |
|---|---|---|
| Minimal agent primitives with tools, handoffs, guardrails, and tracing | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Good for studying the smallest useful production-aware building blocks |
| Explicit state machines, graph transitions, retries, and long-running workflows | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Good for workflows where control flow matters more than conversational freedom |
| Role-based multi-agent task automation | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Good for learning manager-worker and specialist-agent patterns |
| Enterprise integration with planners, connectors, and typed orchestration | [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | Good for teams already thinking about application architecture and governance |
| RAG-heavy document systems and data connectors | [run-llama/llama_index](https://github.com/run-llama/llama_index) | Good for document agents, indexing, retrieval workflows, and knowledge apps |
| Provider routing, budgets, fallback, and gateway operations | [BerriAI/litellm](https://github.com/BerriAI/litellm) | Good when model operations are the bottleneck |
| Tracing, prompt history, evals, and production debugging | [langfuse/langfuse](https://github.com/langfuse/langfuse) or [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | Good when you need evidence for why an agent behaved a certain way |
| Red teaming and CI-based LLM behavior tests | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | Good for regression tests, adversarial prompts, and release gates |
| MCP server and tool ecosystem learning | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Good for learning how tools, resources, and prompts are exposed to agents |

## Compare By Engineering Dimension

| Dimension | What to inspect | Strong signals |
|---|---|---|
| Control flow | How the framework represents steps, branches, retries, and approval | Explicit graph, workflow, state, or task model |
| State | Where memory and intermediate artifacts live | Serializable state, clear checkpoints, replay support |
| Tooling | How tools are declared, validated, authorized, and logged | Typed schemas, permission checks, tool-call trace |
| Evaluation | How behavior is tested before release | Eval cases, test runner, golden outputs, CI examples |
| Observability | Whether you can debug a bad answer after the fact | Traces, spans, inputs, outputs, cost, latency, redaction |
| Safety | How unsafe requests, tool misuse, and prompt injection are handled | Guardrails, refusal policy, approval gates, adversarial tests |
| Operations | How failure, cost, rate limits, and ownership are managed | Retries, fallback, budgets, owner registry, incident playbook |
| Learning curve | How quickly a learner can run and modify one example | Small examples, local demos, clear docs, few required services |

## Framework Fit By Course Module

| Course area | Useful projects |
|---|---|
| Tool calling | OpenAI Agents SDK, LangChain, Semantic Kernel |
| MCP | MCP Python SDK, MCP TypeScript SDK, MCP servers |
| Memory | LangGraph, LlamaIndex, LangChain, Chroma, Qdrant |
| Workflow | LangGraph, Semantic Kernel, Temporal Python SDK |
| Multi-agent | CrewAI, AutoGen, OpenAI Agents SDK handoffs |
| Evaluation | promptfoo, DeepEval, RAGAS, Phoenix |
| Observability | Langfuse, Phoenix, OpenLIT, Helicone, OpenTelemetry |
| Cost and latency | LiteLLM, Helicone, OpenTelemetry |
| Governance | Semantic Kernel, LiteLLM, Langfuse, OpenTelemetry |

## Practical Selection Rules

1. If the agent can damage data, money, privacy, or trust, choose the stack with the clearest control flow and audit trail.
2. If the task is mostly search and synthesis over documents, optimize the retrieval and evaluation stack before adding multi-agent roles.
3. If the task needs approvals or retries, prefer graph or workflow primitives over a single long prompt.
4. If your demo is for a portfolio, choose a framework only after you can explain why a simpler local implementation was not enough.
5. If your team cannot inspect traces, do not call the system production-ready.

## Study Exercise

Pick two frameworks and fill this table:

| Question | Framework A | Framework B |
|---|---|---|
| Smallest primitive |  |  |
| State model |  |  |
| Tool schema model |  |  |
| Approval support |  |  |
| Eval story |  |  |
| Trace story |  |  |
| Best use case |  |  |
| Main risk |  |  |

The learning outcome is not "which one is best." The learning outcome is being able to defend an engineering choice.
