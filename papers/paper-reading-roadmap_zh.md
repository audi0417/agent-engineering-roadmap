# Paper Reading Roadmap 論文閱讀路線

這份 roadmap 把論文對應到課程章節。建議先跑本機 example，再讀論文。

## 怎麼使用？

每讀一篇 paper：

1. 先跑對應的 local example。
2. 讀 introduction 與 method。
3. 問：這篇改變了哪個 agent component？
4. 寫下一個工程啟發。
5. 根據 paper 補一個 eval case。

## 依課程章節閱讀

| 課程章節 | 建議論文 | 本機練習 |
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

## 依研究組織閱讀

| 組織 | 論文 | 學什麼 |
|---|---|---|
| OpenAI | WebGPT | browsing environment、citation、human feedback、factuality evaluation |
| Google / DeepMind / Princeton | ReAct, Tree of Thoughts | reasoning + action、planning as search |
| Meta AI | Toolformer, RAG | tool learning、retrieval-augmented generation |
| Microsoft Research | AutoGen | multi-agent conversation framework、human input、tool use、agent interaction patterns |
| Anthropic | Constitutional AI, Sleeper Agents | safety principles、AI feedback、deceptive behavior risk |
| Stanford | Generative Agents, Lost in the Middle | memory architecture、long-context limitation |
| Princeton | ReAct, Reflexion, Tree of Thoughts, SWE-agent | agent loop、reflection、search、software-agent interface |
| Tsinghua / OpenBMB | ChatDev, AgentBench | multi-agent software workflow、agent evaluation |

## 三條閱讀路線

### Fast Track: Agent Builder

1. ReAct
2. Toolformer
3. RAG
4. Generative Agents
5. AgentBench
6. Prompt Injection

成果：看懂 tool-using、memory-aware、evaluated agent 的核心元件。

### Production Track

1. WebGPT
2. Lost in the Middle
3. RAGAS
4. SWE-agent
5. LLM-as-a-Judge
6. Sleeper Agents

成果：看懂 production agent 為什麼需要 evidence、eval、trace、threat model。

### Research Track

1. A Survey on LLM-based Autonomous Agents
2. ReAct
3. Reflexion
4. Tree of Thoughts
5. Voyager
6. AutoGen
7. ChatDev

成果：能比較不同 agent architecture，而不是只背 framework 名稱。

## Paper Club 格式

| 時間 | 活動 |
|---|---|
| 0-10 min | 一位同學說明 paper problem |
| 10-25 min | 大家找出影響的 agent component |
| 25-45 min | 跑或閱讀對應 local example |
| 45-65 min | 討論工程啟發與限制 |
| 65-80 min | 補一個 eval case 或 design note |
| 80-90 min | 決定這篇 paper 是否要改變 roadmap |

## 讀完交付成果

每讀一篇 paper，產出一份短筆記：

- 一句話摘要
- 影響的 component
- 工程啟發
- 限制
- 對應 local example
- 一個可以改善 repo 的想法
