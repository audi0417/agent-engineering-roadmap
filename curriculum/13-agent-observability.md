# 13 Agent Observability

## Goal

Learn how to make an agent system inspectable after it leaves demo mode.

An agent is observable when you can answer:

- What did the agent see?
- What did it decide?
- Which tool did it call?
- Which guardrail fired?
- Why did the final answer look this way?
- How much did the run cost?

## Why It Matters

A chatbot demo can be debugged by reading the final answer. A production agent cannot.

Once an agent has tools, memory, retrieval, approval gates, and handoffs, the final answer is only the last page of the story. The real system is the sequence of decisions before the answer.

Without observability, teams cannot reliably debug:

- bad tool selection
- missing retrieval context
- unsafe approvals
- prompt injection
- repeated retries
- expensive model calls
- failed handoffs
- hidden policy violations

## Mental Model

Think of an agent trace like a flight recorder.

The trace does not fly the plane. It records enough evidence so that after a surprising event, the team can reconstruct what happened.

For agents, the minimum flight recorder contains:

- `run_id`: one user request or background job
- `span_id`: one operation inside the run
- `event_type`: model decision, tool call, tool result, guardrail, handoff, memory read
- `payload`: the structured details needed for debugging
- `parent_span_id`: how events are connected

## Black Box View

```text
user request
   ↓
agent run
   ↓
decisions + tool calls + guardrails + handoffs
   ↓
final answer
```

If you only store the final answer, the middle is invisible.

## Mechanism View

```text
Run
├── LLM decision span
├── retrieval span
├── tool call span
├── tool result span
├── guardrail span
├── handoff span
└── final response span
```

Each span should answer one question:

> What happened here, and what evidence did the system use?

## What To Trace

Trace these events first:

| Event | Why it matters |
|---|---|
| run start/end | Groups all work for one request |
| model request/response metadata | Debugs model choice, latency, token cost |
| tool call/result | Shows what the agent actually did |
| retrieval query/result ids | Explains grounded or ungrounded answers |
| guardrail trigger | Explains refusal, approval, or escalation |
| memory read/write | Reveals stale or unsafe context |
| handoff | Shows responsibility transfer |
| final answer | Connects the visible output to the hidden run |

## What Not To Log Blindly

Observability can become a privacy leak.

Do not blindly log:

- API keys
- access tokens
- full medical records
- personal financial data
- private user memory
- raw documents with sensitive content
- credentials returned by tools

Production traces need redaction and retention policies.

## Common Failure Modes

### Failure 1: Final-Answer-Only Debugging

The team stores only the answer and user input.

Problem: when the answer is wrong, nobody knows whether the issue came from retrieval, policy, tool use, or model reasoning.

Fix: log the intermediate events.

### Failure 2: Unstructured Logs

The team logs long text strings.

Problem: logs cannot be filtered by tool name, run id, risk level, or guardrail type.

Fix: use structured JSON events.

### Failure 3: Logging Everything Forever

The team stores every prompt, document, and tool result forever.

Problem: observability becomes a security and compliance problem.

Fix: redact sensitive content and define retention windows.

## Practical Exercise

Run:

```bash
python examples/10-observable-agent/main.py
```

Then inspect:

```bash
cat examples/10-observable-agent/trace.jsonl
```

Answer:

- Which event required human approval?
- Which event would you show a reviewer?
- Which payload field should be redacted in a real production system?

## Production Checklist

- [ ] Every run has a `run_id`
- [ ] Tool calls and tool results are recorded separately
- [ ] Guardrail triggers are visible
- [ ] Retrieval traces store document ids, not only raw text
- [ ] Sensitive fields are redacted
- [ ] Trace retention has a policy
- [ ] Incidents can be replayed from traces
- [ ] Cost, latency, and error rate can be measured

## References

- [OpenAI Agents SDK Tracing](https://openai.github.io/openai-agents-python/tracing/)
- [OpenTelemetry Generative AI Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/)
- [OpenTelemetry MCP Semantic Conventions](https://opentelemetry.io/docs/specs/semconv/gen-ai/mcp/)

