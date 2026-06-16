# Paper Notes

These are short engineering notes. They are intentionally concise and original. Read the official paper for full details.

## ReAct

- Link: https://arxiv.org/abs/2210.03629
- PDF: https://arxiv.org/pdf/2210.03629
- Organizations: Google Research, Princeton
- Related modules: 01, 02, 05, 06
- Related examples: `examples/02-tool-using-agent`, `examples/09-graph-approval-agent`

One sentence: ReAct interleaves reasoning and action so an agent can think, call tools, observe results, and continue.

Engineering takeaway: A tool-using agent should not be designed as one giant prompt. It needs an explicit loop: reason, act, observe, update.

Limitation: Reasoning traces can help debugging, but they are not a substitute for tool validation, traces, or evals.

Practice: Add an eval case where a tool result contradicts the first plan and the agent must revise its next step.

## Toolformer

- Link: https://arxiv.org/abs/2302.04761
- PDF: https://arxiv.org/pdf/2302.04761
- Organization: Meta AI
- Related modules: 02, 03, 15
- Related examples: `examples/02-tool-using-agent`, `examples/12-cost-aware-agent`

One sentence: Toolformer studies how language models can learn when to call tools and how to incorporate tool results.

Engineering takeaway: Tool calls need schemas, call timing, result integration, and cost control.

Limitation: Learning to call APIs in a paper setting is not the same as safely calling production tools.

Practice: Add a bad-tool-choice eval where the agent should avoid a costly tool when a cheaper route is enough.

## WebGPT

- Link: https://arxiv.org/abs/2112.09332
- PDF: https://cdn.openai.com/WebGPT.pdf
- Organization: OpenAI
- Related modules: 00, 02, 04, 08, 13
- Related examples: `examples/08-mini-rag`, `examples/10-observable-agent`

One sentence: WebGPT trains a model to browse, collect references, and answer long-form questions with human feedback.

Engineering takeaway: Grounded answers need evidence collection, not just confident prose.

Limitation: Browsing helps factuality, but source selection and citation quality still need evaluation.

Practice: Add citation-quality checks to a RAG or browsing-style agent.

## Retrieval-Augmented Generation

- Link: https://arxiv.org/abs/2005.11401
- PDF: https://arxiv.org/pdf/2005.11401
- Organizations: Meta AI, UCL, NYU, FAIR
- Related modules: 04, 09, 22
- Related examples: `examples/08-mini-rag`

One sentence: RAG combines parametric model knowledge with retrieved non-parametric memory.

Engineering takeaway: Retrieval is not a feature bolted onto a chatbot. It is a system component that needs indexing, ranking, grounding, and no-answer behavior.

Limitation: Better retrieval does not automatically mean faithful generation.

Practice: Add eval cases for irrelevant retrieval, missing answer, and conflicting sources.

## Lost in the Middle

- Link: https://arxiv.org/abs/2307.03172
- PDF: https://arxiv.org/pdf/2307.03172
- Organizations: Stanford, UC Berkeley, Samaya AI
- Related modules: 03, 04, 18
- Related examples: `examples/08-mini-rag`, `examples/15-memory-governance-agent`

One sentence: Long-context models can fail to use information reliably when relevant facts appear in the middle of context.

Engineering takeaway: Do not treat a huge context window as a memory system. Retrieval order, compression, and evaluation matter.

Limitation: The exact failure pattern changes by model and task, so teams need their own eval cases.

Practice: Create a test where the relevant memory appears between irrelevant chunks.

## Generative Agents

- Link: https://arxiv.org/abs/2304.03442
- PDF: https://arxiv.org/pdf/2304.03442
- Organizations: Stanford, Google
- Related modules: 03, 07, 18
- Related examples: `examples/04-memory-agent`, `examples/06-agent-colony`

One sentence: Generative Agents demonstrates believable agents with observation, memory, reflection, and planning.

Engineering takeaway: Agent memory should include retrieval and reflection policies, not just raw chat history.

Limitation: Believable simulation is not the same as reliable production automation.

Practice: Add a reflection step that summarizes repeated observations before storing long-term memory.

## Reflexion

- Link: https://arxiv.org/abs/2303.11366
- PDF: https://arxiv.org/pdf/2303.11366
- Organizations: Princeton, Northeastern
- Related modules: 03, 05, 16, 18
- Related examples: `examples/05-multi-agent-workflow`, `examples/13-durable-workflow-agent`

One sentence: Reflexion improves agent behavior by storing verbal feedback in episodic memory.

Engineering takeaway: Feedback should be converted into reusable memory only when it is specific, validated, and safe.

Limitation: Storing bad reflections can amplify errors across future attempts.

Practice: Add memory governance rules for storing evaluator feedback.

## Self-Refine

- Link: https://arxiv.org/abs/2303.17651
- PDF: https://arxiv.org/pdf/2303.17651
- Organizations: Allen AI, CMU, University of Washington, others
- Related modules: 05, 07, 22
- Related examples: `examples/05-multi-agent-workflow`, `examples/17-advanced-eval-harness`

One sentence: Self-Refine uses generate, feedback, and refine loops to improve outputs without additional training.

Engineering takeaway: Reviewer agents should have explicit review criteria and stop conditions.

Limitation: Self-feedback can reinforce a model's blind spots.

Practice: Add a reviewer that must cite which rubric item caused a revision.

## Tree of Thoughts

- Link: https://arxiv.org/abs/2305.10601
- PDF: https://arxiv.org/pdf/2305.10601
- Organizations: Princeton, Google DeepMind
- Related modules: 05, 06, 07
- Related examples: `examples/09-graph-approval-agent`

One sentence: Tree of Thoughts treats problem solving as search over multiple reasoning paths.

Engineering takeaway: Hard planning tasks benefit from explicit branching, scoring, and backtracking.

Limitation: Search can be expensive and unnecessary for simple tasks.

Practice: Add a graph-agent branch where two plans are scored before execution.

## Voyager

- Link: https://arxiv.org/abs/2305.16291
- PDF: https://arxiv.org/pdf/2305.16291
- Organizations: NVIDIA, Caltech, UT Austin, Stanford, ASU
- Related modules: 06, 07, 16, 18
- Related examples: `examples/06-agent-colony`, `examples/13-durable-workflow-agent`

One sentence: Voyager uses an automatic curriculum, executable skill library, environment feedback, and self-verification for open-ended learning.

Engineering takeaway: Skills become more useful when they are executable, reusable, and tested.

Limitation: Open-ended game environments differ from enterprise systems with permissions and safety constraints.

Practice: Add a small skill library to a colony example and test skill reuse.

## AgentBench

- Link: https://arxiv.org/abs/2308.03688
- PDF: https://arxiv.org/pdf/2308.03688
- Organizations: Tsinghua, Ohio State, UC Berkeley
- Related modules: 09, 22
- Related examples: `examples/17-advanced-eval-harness`, `benchmarks/benchmark_runner.py`

One sentence: AgentBench evaluates LLMs as agents across interactive environments.

Engineering takeaway: Agent evaluation needs tasks with actions, state, and multi-turn failure modes.

Limitation: Benchmarks are useful signals, but production tasks need domain-specific evals.

Practice: Add one benchmark that tests recovery after a wrong intermediate action.

## AutoGen

- Link: https://arxiv.org/abs/2308.08155
- PDF: https://arxiv.org/pdf/2308.08155
- Organization: Microsoft Research
- Related modules: 07, 08, 12, 25
- Related examples: `examples/05-multi-agent-workflow`, `examples/06-agent-colony`

One sentence: AutoGen frames LLM applications as conversations among customizable agents that can involve models, tools, and humans.

Engineering takeaway: Multi-agent systems need explicit conversation patterns, role boundaries, and human/tool integration rules.

Limitation: Conversation-based orchestration can become hard to debug without traces, turn limits, and evals.

Practice: Rewrite the multi-agent workflow example as a conversation protocol with supervisor, worker, and human proxy roles.

## RAGAS

- Link: https://arxiv.org/abs/2309.15217
- PDF: https://arxiv.org/pdf/2309.15217
- Organizations: Exploding Gradients, CardiffNLP
- Related modules: 04, 22
- Related examples: `examples/08-mini-rag`, `examples/17-advanced-eval-harness`

One sentence: RAGAS proposes evaluation dimensions for retrieval-augmented generation without relying entirely on human labels.

Engineering takeaway: RAG evaluation should separate retrieval quality, grounding, and answer quality.

Limitation: Automated metrics still need calibration against real user needs.

Practice: Split a RAG eval into retrieval pass, grounding pass, and answer pass.

## SWE-agent

- Link: https://arxiv.org/abs/2405.15793
- PDF: https://arxiv.org/pdf/2405.15793
- Organization: Princeton
- Related modules: 09, 13, 16, 25
- Related examples: `examples/10-observable-agent`, `examples/13-durable-workflow-agent`

One sentence: SWE-agent shows that agent-computer interfaces can strongly affect software engineering agent performance.

Engineering takeaway: The interface is part of the agent system. File editing, navigation, tests, and feedback should be designed for agent use.

Limitation: Coding-agent results do not automatically transfer to every enterprise workflow.

Practice: Add a trace format that records file operation, test command, failure, and retry.

## Prompt Injection

- Link: https://arxiv.org/abs/2306.05499
- PDF: https://arxiv.org/pdf/2306.05499
- Organizations: Nanyang Technological University, Zhejiang University, others
- Related modules: 03, 14, 21
- Related examples: `examples/11-prompt-injection-defense`

One sentence: Prompt injection attacks exploit the difficulty of separating instructions from untrusted data.

Engineering takeaway: Retrieved documents, tool results, web pages, and user files should be treated as untrusted input.

Limitation: Filters are not enough; defenses need permissions, least privilege, logging, and evals.

Practice: Add indirect prompt injection cases to every RAG or MCP example.

## Constitutional AI

- Link: https://arxiv.org/abs/2212.08073
- PDF: https://arxiv.org/pdf/2212.08073
- Organization: Anthropic
- Related modules: 08, 14, 22
- Related examples: `examples/11-prompt-injection-defense`, `examples/17-advanced-eval-harness`

One sentence: Constitutional AI trains helpful and harmless behavior using critique, revision, and AI feedback guided by principles.

Engineering takeaway: Safety policies should be explicit enough to review, test, and revise.

Limitation: A principle list is not a full operational safety system.

Practice: Turn a safety policy into eval cases and refusal tests.

## Sleeper Agents

- Link: https://arxiv.org/abs/2401.05566
- PDF: https://arxiv.org/pdf/2401.05566
- Organization: Anthropic and collaborators
- Related modules: 14, 21, 22
- Related examples: `examples/11-prompt-injection-defense`, `examples/17-advanced-eval-harness`

One sentence: Sleeper Agents studies hidden deceptive behaviors that can persist through standard safety training.

Engineering takeaway: Safety testing should include hidden triggers, distribution shifts, and adversarial release gates.

Limitation: The paper uses proof-of-concept settings; production risk assessment still needs domain context.

Practice: Add hidden-trigger adversarial eval cases to the advanced eval harness.
