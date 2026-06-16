# Agent Engineering Curriculum

[繁體中文](README_zh.md)

This curriculum converts broad Agent Engineering topics into an original, structured learning program.

It is designed to help learners move from basic agent concepts to production-ready multi-agent systems.

---

## Curriculum Structure

| Module | Topic | Goal |
|---|---|---|
| 00 | Agent Foundations | Understand what agents are and how they differ from chatbots |
| 01 | Agent Architecture | Learn the core components of an agent system |
| 02 | Tool Calling | Teach agents how to call external tools safely |
| 03 | Memory Systems | Design short-term, long-term, user, and shared memory |
| 04 | RAG and Embeddings | Connect agents to knowledge bases and retrieval pipelines |
| 05 | Workflow Orchestration | Build controllable planning, execution, and review flows |
| 06 | Graph-based Agents | Model agent workflows as graphs and state machines |
| 07 | Multi-Agent Systems | Coordinate specialized agents through structured collaboration |
| 08 | Human-in-the-loop | Add approval, feedback, and escalation mechanisms |
| 09 | Production Agent Systems | Add evaluation, observability, safety, and deployment patterns |
| 10 | Domain Agent: Healthcare | Build healthcare-oriented agent workflows with safety boundaries |
| 11 | Domain Agent: Finance | Build finance research and analysis agents with risk controls |
| 12 | Agent Frameworks Comparison | Compare common agent frameworks and when to use each |
| 13 | Agent Observability | Trace, replay, and debug production agent runs |
| 14 | Agent Security | Defend against prompt injection, unsafe tools, and memory leakage |
| 15 | Agent Cost And Latency Engineering | Route tasks by budget, latency, and quality needs |
| 16 | Durable Agent Runtime | Checkpoint, resume, and recover long-running workflows |
| 17 | MCP Modernization | Use tools, resources, prompts, authorization, and elicitation |
| 18 | Agent Memory Governance | Govern memory writes, redaction, merge, decay, and deletion |
| 19 | Agent Identity And Permission | Treat agents as scoped identities with owners and access reviews |
| 21 | Agent Incident Response | Respond to unsafe or unexpected agent behavior with traces and evals |
| 22 | Advanced Agent Evaluation | Build regression, safety, adversarial, and golden trace release gates |
| 24 | Agent Product UX | Design approval, visibility, evidence, recovery, and trust patterns |
| 25 | Enterprise Agent Operating Model | Register, review, monitor, and retire agents safely |

---

## Learning Philosophy

This curriculum follows three principles:

1. Start with simple agents before adding tools.
2. Add memory and workflow before adding multiple agents.
3. Treat production safety as part of the system design, not a final step.

---

## Suggested Learning Path

```text
Foundations
   ↓
Architecture
   ↓
Tool Calling
   ↓
Memory
   ↓
RAG
   ↓
Workflow
   ↓
Graph-based Agents
   ↓
Multi-Agent Systems
   ↓
Human Feedback
   ↓
Production
   ↓
Domain Applications
```

---

## How to Use This Curriculum

Each module should contain:

- goal
- why it matters
- mental model
- core concepts
- architecture diagram
- hands-on exercise
- checklist
- common mistakes
- outcome

---

## Status

The curriculum now includes concept chapters, runnable examples, guided labs, patterns, templates, assessments, glossary, and a capstone project.

---

## Module-To-Practice Map

| Module | Read | Run | Practice | Assess |
|---|---|---|---|---|
| 00 | `00-agent-foundations.md` | - | `labs/lab-00-agent-spec.md` | `assessments/quiz-bank.md` |
| 01 | `01-agent-architecture.md` | `examples/01-single-agent` | `labs/lab-01-single-agent.md` | `assessments/rubrics.md` |
| 02 | `02-tool-calling.md` | `examples/02-tool-using-agent` | `labs/lab-02-tool-calling.md` | `assessments/quiz-bank.md` |
| 03 | `03-memory-systems.md` | `examples/04-memory-agent` | `labs/lab-03-memory.md` | `templates/memory-policy-template.md` |
| 04 | `04-rag-and-embeddings.md` | `examples/08-mini-rag` | `labs/lab-04-rag.md` | retrieval eval cases |
| 05 | `05-workflow-orchestration.md` | `examples/05-multi-agent-workflow` | `labs/lab-05-workflow.md` | workflow review rubric |
| 06 | `06-graph-based-agents.md` | `examples/09-graph-approval-agent` | `labs/lab-06-graph-agent.md` | graph design review |
| 07 | `07-multi-agent-systems.md` | `examples/06-agent-colony` | `labs/lab-07-multi-agent.md` | routing tests |
| 08 | `08-human-in-the-loop.md` | `examples/09-graph-approval-agent` | `labs/lab-08-human-in-the-loop.md` | approval policy review |
| 09 | `09-production-agent-systems.md` | `examples/07-evaluation-harness`, `examples/09-graph-approval-agent` | `labs/lab-09-evaluation.md` | regression suite |
| 10 | `10-domain-agent-healthcare.md` | `examples/06-agent-colony` | domain safety plan | production rubric |
| 11 | `11-domain-agent-finance.md` | `examples/06-agent-colony` | domain risk plan | production rubric |
| 12 | `12-agent-frameworks-comparison.md` | `capstone-starter` | `labs/lab-10-capstone-prep.md` | architecture review |
| 13 | `13-agent-observability.md` | `examples/10-observable-agent` | trace review | incident replay |
| 14 | `14-agent-security.md` | `examples/11-prompt-injection-defense` | `security/prompt-injection-lab.md` | security eval cases |
| 15 | `15-agent-cost-latency-engineering.md` | `examples/12-cost-aware-agent` | routing budget review | cost and latency checks |
| 16 | `16-durable-agent-runtime.md` | `examples/13-durable-workflow-agent` | checkpoint review | resume test |
| 17 | `17-mcp-modernization.md` | `examples/14-modern-mcp-gateway` | gateway policy review | authorization and elicitation tests |
| 18 | `18-agent-memory-governance.md` | `examples/15-memory-governance-agent` | memory policy review | redaction and deletion tests |
| 19 | `19-agent-identity-permission.md` | `examples/16-agent-permission-system` | access review | permission denial tests |
| 21 | `21-agent-incident-response.md` | `incident-response/agent-incident-playbook.md` | incident drill | hotfix eval |
| 22 | `22-advanced-agent-evaluation.md` | `examples/17-advanced-eval-harness` | release gate review | golden trace and adversarial eval |
| 24 | `24-agent-product-ux.md` | `product-ux/agent-product-ux-checklist.md` | UX review | approval and recovery checklist |
| 25 | `25-enterprise-agent-operating-model.md` | `operating-model/enterprise-agent-operating-checklist.md` | registry review | operating checklist |

---

## Completion Path

```text
Read a module
   ↓
Run the closest example
   ↓
Complete the lab
   ↓
Answer review questions
   ↓
Update your capstone design
```
