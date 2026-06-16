# Paper Reading Roadmap

This roadmap maps papers to the course modules. Read papers after running the matching local example, not before.

## How To Use This Roadmap

For each paper:

1. Run the local example first.
2. Read the paper introduction and method.
3. Ask which agent component the paper changes.
4. Write one engineering takeaway.
5. Add one eval case inspired by the paper.

## By Course Module

| Course module | Papers to read | Local practice |
|---|---|---|
| 00 Foundations | WebGPT, RAG, A Survey on LLM-based Autonomous Agents | `examples/01-single-agent` |
| 01 Agent Architecture | ReAct, Generative Agents, Voyager | `examples/01-single-agent`, `examples/06-agent-colony` |
| 02 Tool Calling | Toolformer, ReAct, WebGPT | `examples/02-tool-using-agent` |
| 03 MCP | Toolformer, WebGPT, Prompt Injection | `examples/03-mcp-agent`, `examples/14-modern-mcp-gateway` |
| 04 RAG and Embeddings | RAG, RAGAS, Lost in the Middle | `examples/08-mini-rag` |
| 05 Workflow Orchestration | Self-Refine, Tree of Thoughts, Reflexion | `examples/05-multi-agent-workflow`, `examples/09-graph-approval-agent` |
| 06 Graph-based Agents | Tree of Thoughts, ReAct, SWE-agent | `examples/09-graph-approval-agent` |
| 07 Multi-Agent Systems | Generative Agents, AutoGen, ChatDev, Voyager | `examples/05-multi-agent-workflow`, `examples/06-agent-colony` |
| 08 Human-in-the-loop | WebGPT, Constitutional AI, LLM-as-a-Judge | `examples/09-graph-approval-agent` |
| 09 Production Systems | SWE-agent, AgentBench, RAGAS | `examples/10-observable-agent`, `benchmarks/benchmark_runner.py` |
| 13 Observability | WebGPT, SWE-agent, AgentBench | `examples/10-observable-agent` |
| 14 Security | Prompt Injection, Sleeper Agents, Constitutional AI | `examples/11-prompt-injection-defense` |
| 15 Cost and Latency | Toolformer, WebGPT, SWE-agent | `examples/12-cost-aware-agent` |
| 16 Durable Runtime | Voyager, Reflexion, SWE-agent | `examples/13-durable-workflow-agent` |
| 18 Memory Governance | Generative Agents, Reflexion, Lost in the Middle | `examples/15-memory-governance-agent` |
| 22 Advanced Evaluation | AgentBench, RAGAS, LLM-as-a-Judge | `examples/17-advanced-eval-harness` |

## By Research Lab Or Organization

| Organization | Papers | What to learn |
|---|---|---|
| OpenAI | WebGPT | Browsing environment, citations, human feedback, factuality evaluation |
| Google / DeepMind / Princeton | ReAct, Tree of Thoughts | Reasoning plus action, planning as search |
| Meta AI | Toolformer, RAG | Tool learning and retrieval-augmented generation |
| Microsoft Research | AutoGen | Multi-agent conversation framework, human input, tool use, and agent interaction patterns |
| Anthropic | Constitutional AI, Sleeper Agents | Safety principles, AI feedback, deceptive behavior risks |
| Stanford | Generative Agents, Lost in the Middle | Memory architecture and long-context limitations |
| Princeton | ReAct, Reflexion, Tree of Thoughts, SWE-agent | agent loops, reflection, search, software-agent interfaces |
| Tsinghua / OpenBMB | ChatDev, AgentBench | multi-agent software workflows and agent evaluation |

## Three Reading Tracks

### Fast Track: Agent Builder

1. ReAct
2. Toolformer
3. RAG
4. Generative Agents
5. AgentBench
6. Prompt Injection

Outcome: You understand the core pieces behind tool-using, memory-aware, evaluated agents.

### Production Track

1. WebGPT
2. Lost in the Middle
3. RAGAS
4. SWE-agent
5. LLM-as-a-Judge
6. Sleeper Agents

Outcome: You understand why production agents need evidence, evals, traces, and threat models.

### Research Track

1. A Survey on LLM-based Autonomous Agents
2. ReAct
3. Reflexion
4. Tree of Thoughts
5. Voyager
6. AutoGen
7. ChatDev

Outcome: You can compare different agent architectures instead of memorizing framework names.

## Paper Club Format

Use this for a study group:

| Time | Activity |
|---|---|
| 0-10 min | One learner explains the paper problem |
| 10-25 min | Group identifies the agent component affected |
| 25-45 min | Run or inspect the matching local example |
| 45-65 min | Discuss engineering takeaways and limitations |
| 65-80 min | Add one eval case or design note |
| 80-90 min | Decide whether the paper should change the roadmap |

## Deliverable

After reading any paper, create a short note:

- one-sentence summary
- component affected
- engineering takeaway
- limitation
- matching local example
- one possible repo improvement
