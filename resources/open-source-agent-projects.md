# Open Source Agent Projects

This page curates open-source projects that are useful for learning agent engineering.

The goal is not to list every popular repository. The goal is to help learners know what to study, when to study it, and how it maps to this roadmap.

## How To Use This Page

Use these projects after you understand the local examples in this repository.

Suggested order:

1. Learn the concept from the roadmap chapter.
2. Run the matching local dependency-free example.
3. Read one external open-source project to see how the idea appears in a real ecosystem.
4. Compare the project design against this course's checklists: tools, memory, workflow, evals, observability, safety, and governance.

Companion guides:

- [Agent Framework Selection Matrix](agent-framework-selection-matrix.md) helps you choose what to study or use.
- [How To Read Open Source Agent Repositories](how-to-read-open-source-agent-repos.md) gives a repeatable reading method.
- [DeepEval And RAGAS Evaluation Frameworks](eval-frameworks-deepeval-ragas.md) explains practical eval frameworks.
- [Portfolio Projects](../projects/portfolio-projects.md) turns these projects into buildable GitHub demos.

## Agent Frameworks And Runtimes

| Project | Best for | Study with |
|---|---|---|
| [openai/openai-agents-python](https://github.com/openai/openai-agents-python) | Lightweight agent orchestration, tools, handoffs, guardrails, tracing | Modules 09, 13, 22 |
| [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) | Stateful, long-running, graph-based agent workflows | Modules 06, 16 |
| [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) | Role-based multi-agent automation | Modules 07, 12 |
| [microsoft/autogen](https://github.com/microsoft/autogen) | Multi-agent collaboration patterns and research history | Modules 07, 12 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | Enterprise-oriented orchestration, planners, connectors, and skills | Modules 05, 12, 25 |

Notes:

- OpenAI Agents SDK is useful for studying minimal primitives: agents, tools, handoffs, guardrails, and tracing.
- LangGraph is especially useful once learners care about durable state and explicit workflow control.
- AutoGen is valuable historically and conceptually, but check the repository status before choosing it as a production dependency.

## MCP And Tool Integration

| Project | Best for | Study with |
|---|---|---|
| [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) | Reference MCP servers and community server patterns | Modules 03, 17 |
| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk) | Building MCP clients and servers in Python | Modules 03, 17 |
| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk) | Building MCP clients and servers in TypeScript | Modules 03, 17 |
| [punkpeye/awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | Browsing community MCP server examples | Modules 03, 17, 19 |

What to inspect:

- tool schema design
- resource naming
- authorization and token boundaries
- how servers handle unsafe inputs
- what should require human approval

## RAG, Indexing, And Knowledge Agents

| Project | Best for | Study with |
|---|---|---|
| [run-llama/llama_index](https://github.com/run-llama/llama_index) | Document agents, retrieval, indexing, workflows, and data connectors | Modules 04, 22 |
| [langchain-ai/langchain](https://github.com/langchain-ai/langchain) | LLM application components, tools, retrievers, chains, integrations | Modules 02, 04, 12 |
| [deepset-ai/haystack](https://github.com/deepset-ai/haystack) | Search, RAG pipelines, and production retrieval systems | Modules 04, 09 |
| [chroma-core/chroma](https://github.com/chroma-core/chroma) | Vector database and retrieval experiments | Modules 03, 04 |
| [qdrant/qdrant](https://github.com/qdrant/qdrant) | Vector search infrastructure | Modules 04, 09 |

What to inspect:

- chunking strategy
- metadata handling
- no-answer behavior
- source attribution
- retrieval evaluation
- security around retrieved content

## Evaluation, Red Teaming, And Safety

| Project | Best for | Study with |
|---|---|---|
| [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) | LLM evals, red teaming, and CI-based prompt/application testing | Modules 14, 22 |
| [confident-ai/deepeval](https://github.com/confident-ai/deepeval) | Pytest-style LLM app, agent, prompt, RAG, safety, and regression evals | Modules 07, 14, 22 |
| [explodinggradients/ragas](https://github.com/explodinggradients/ragas) | RAG evaluation metrics, synthetic test data, grounding, and answer quality checks | Modules 04, 22 |
| [guardrails-ai/guardrails](https://github.com/guardrails-ai/guardrails) | Output validation and structured guardrails | Modules 02, 14 |
| [ProtectAI/rebuff](https://github.com/protectai/rebuff) | Prompt injection detection patterns | Modules 14, 21 |

What to inspect:

- adversarial cases
- refusal tests
- regression gates
- golden traces
- CI integration
- incident replay tests

## Observability And Production Monitoring

| Project | Best for | Study with |
|---|---|---|
| [langfuse/langfuse](https://github.com/langfuse/langfuse) | Open-source LLM tracing, evals, monitoring, and debugging | Modules 13, 21 |
| [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) | LLM observability, tracing, evals, and experimentation | Modules 13, 22 |
| [openlit/openlit](https://github.com/openlit/openlit) | OpenTelemetry-native LLM observability | Modules 13, 21 |
| [helicone/helicone](https://github.com/Helicone/helicone) | LLM observability, proxying, cost, and latency monitoring | Modules 13, 15 |
| [open-telemetry/opentelemetry-specification](https://github.com/open-telemetry/opentelemetry-specification) | Telemetry conventions and instrumentation design | Modules 13, 21 |

What to inspect:

- trace schema
- span naming
- token and cost tracking
- error grouping
- eval-to-trace connection
- redaction and data retention

## Deployment, Routing, And Operations

| Project | Best for | Study with |
|---|---|---|
| [BerriAI/litellm](https://github.com/BerriAI/litellm) | Model routing, proxying, budget controls, and provider abstraction | Modules 15, 25 |
| [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel) | Enterprise integration patterns and orchestration | Modules 12, 25 |
| [ray-project/ray](https://github.com/ray-project/ray) | Distributed Python workloads and scalable background execution | Modules 16, 25 |
| [temporalio/sdk-python](https://github.com/temporalio/sdk-python) | Durable workflows and retryable long-running processes | Modules 16, 21 |

What to inspect:

- retry policy
- workflow state
- cost routing
- fallback behavior
- deployment topology
- owner and operational boundaries

## Learning Repositories

| Project | Best for | Study with |
|---|---|---|
| [langchain-ai/langgraph-101](https://github.com/langchain-ai/langgraph-101) | Hands-on LangGraph learning tracks | Modules 05, 06, 16 |
| [crewAIInc/crewAI-examples](https://github.com/crewAIInc/crewAI-examples) | End-to-end CrewAI applications | Modules 07, 12 |
| [openai/openai-cookbook](https://github.com/openai/openai-cookbook) | Practical OpenAI API examples and patterns | Modules 00, 02, 09 |
| [microsoft/semantic-kernel/tree/main/python/samples](https://github.com/microsoft/semantic-kernel/tree/main/python/samples) | Semantic Kernel examples | Modules 05, 12 |

## How To Compare Projects

When studying any project, ask:

- What is the smallest primitive: agent, graph, task, tool, span, or workflow?
- Where is state stored?
- How are tool permissions represented?
- How are errors retried or recovered?
- How are prompts, tools, and traces tested?
- What is the observability story?
- What would break if this ran in a regulated domain?

## Contribution Idea

If you add a new external project to this list, include:

- link
- category
- what to study
- matching roadmap modules
- one caution or limitation

Do not copy code or documentation from the external project into this repository.
