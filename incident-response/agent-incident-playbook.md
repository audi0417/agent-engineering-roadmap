# Agent Incident Response Playbook

Use this playbook when an agent produces unsafe output, calls the wrong tool, leaks sensitive context, ignores approval policy, or behaves unexpectedly.

## 1. Declare

Record:

- incident title
- time detected
- detecting person or system
- affected agent
- affected tool or workflow
- suspected severity

## 2. Contain

Immediate containment options:

- disable the affected agent
- disable a specific tool
- revoke a token or scope
- pause memory writes
- pause external side effects
- route high-risk tasks to human review

Containment should happen before root-cause analysis when user harm or data exposure is possible.

## 3. Preserve Evidence

Collect:

- run id
- trace events
- user request
- retrieved document ids
- tool calls and tool results
- guardrail events
- memory reads and writes
- permission decisions
- final output

Redact sensitive data before sharing incident notes.

## 4. Triage

Ask:

- Did the model make a bad decision?
- Did retrieval introduce unsafe context?
- Did a tool return malicious or confusing data?
- Did memory contain stale or sensitive information?
- Did permissions allow too much access?
- Did an approval gate fail?
- Did a handoff lose policy context?

## 5. Hotfix

A good hotfix includes:

- a targeted code or policy change
- a new regression eval
- a trace or benchmark check
- a rollback plan
- an owner

Do not close the incident with only a prompt edit unless the eval proves the behavior changed.

## 6. Verify

Run:

```bash
python scripts/verify_examples.py
python benchmarks/benchmark_runner.py
```

For production systems, also replay the original trace or create a synthetic case with the same failure shape.

## 7. Postmortem

Use this template:

```text
Title:
Date:
Owner:
Severity:

What happened:
User impact:
Detection:
Timeline:
Root cause:
Contributing factors:
What worked:
What failed:
Fix:
New eval:
Follow-up owners:
```

## 8. Prevention

Add at least one of:

- new benchmark case
- new security eval
- stricter permission scope
- memory retention change
- approval gate
- tool schema validation
- observability event
- owner review cadence

