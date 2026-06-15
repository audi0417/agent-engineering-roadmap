# Agent Engineering Patterns

Patterns are reusable solutions to recurring agent design problems.

Use this catalog when you know the symptom but are not sure which architecture to choose.

## Pattern Index

| Pattern | Use When | Avoid When |
|---|---|---|
| Single-Purpose Agent | One narrow task is enough | The task requires external actions |
| Tool-Using Agent | The model needs external capabilities | The tool has high-risk side effects and no approval gate |
| RAG Agent | The answer depends on external knowledge | Retrieval quality cannot be evaluated |
| Memory Agent | Stable context should persist across turns | The information is sensitive or unstable |
| Planner-Executor | The task has multiple steps | The task is simple enough for one call |
| Reviewer-Evaluator | Quality must be checked before delivery | The rubric is vague |
| Router-Specialist | Different task types need different handlers | Routing is ambiguous and untested |
| Supervisor Multi-Agent | Several specialists must collaborate | No one owns the final answer |
| Human Approval Gate | Actions are high-impact or irreversible | The action is low-risk and frequent |
| Evaluation Harness | You need regression protection | You have no expected behavior defined |

## 1. Single-Purpose Agent

### Problem

You want an agent that reliably performs one task.

### Structure

```text
Input -> Prompt + Rules -> Model -> Structured Output -> Validation
```

### Use For

- summarization
- classification
- extraction
- rewriting
- planning drafts

### Failure Mode

The scope gets too broad and the agent starts pretending to be a general assistant.

## 2. Tool-Using Agent

### Problem

The model cannot complete the task with text alone.

### Structure

```text
Input -> Decide Tool -> Validate Arguments -> Execute Tool -> Interpret Result -> Answer
```

### Use For

- calculation
- search
- database lookup
- document operations
- external API calls

### Failure Mode

The agent calls tools when it should ask a clarification question.

## 3. RAG Agent

### Problem

The answer depends on knowledge outside the model's context.

### Structure

```text
Question -> Retrieve Documents -> Rank Context -> Generate Answer -> Cite Sources -> Evaluate Faithfulness
```

### Use For

- internal knowledge assistants
- policy lookup
- product documentation
- research support

### Failure Mode

The model answers confidently even when retrieval found the wrong documents.

## 4. Memory Agent

### Problem

The agent needs stable context across tasks or sessions.

### Structure

```text
User Event -> Memory Write Policy -> Memory Store -> Retrieval Policy -> Current Context
```

### Use For

- user preferences
- project facts
- long-running workflows
- shared team context

### Failure Mode

The memory store becomes a pile of stale, sensitive, or irrelevant text.

## 5. Planner-Executor

### Problem

The task has multiple steps and needs explicit control.

### Structure

```text
Task -> Plan -> Execute Step -> Observe -> Continue Or Stop -> Final Output
```

### Use For

- research workflows
- report generation
- data analysis
- multi-step tool use

### Failure Mode

The plan is generated but never checked against reality.

## 6. Reviewer-Evaluator

### Problem

You need to catch errors before users see the final output.

### Structure

```text
Draft -> Rubric -> Review -> Pass Or Revise -> Final
```

### Use For

- content generation
- code review support
- high-stakes summaries
- structured reports

### Failure Mode

The evaluator rewards style instead of correctness.

## 7. Router-Specialist

### Problem

Different task types require different prompts, tools, or policies.

### Structure

```text
Input -> Router -> Specialist Agent -> Specialist Output -> Final Formatter
```

### Use For

- customer support categories
- domain workflows
- mixed internal tools
- enterprise automation

### Failure Mode

The router is not evaluated, so requests go to the wrong specialist.

## 8. Supervisor Multi-Agent

### Problem

Several specialist agents must collaborate under one owner.

### Structure

```text
User Task -> Supervisor -> Specialists -> Shared State -> Evaluator -> Final Answer
```

### Use For

- agent colonies
- domain teams
- research teams
- operations workflows

### Failure Mode

Agents debate forever or produce conflicting answers without resolution.

## 9. Human Approval Gate

### Problem

Some actions are too risky to automate fully.

### Structure

```text
Proposed Action -> Risk Classifier -> Approval Request -> Execute Or Refuse -> Audit Log
```

### Use For

- sending emails
- deleting data
- financial actions
- medical workflows
- production system changes

### Failure Mode

The approval prompt is vague, so the human cannot make an informed decision.

## 10. Evaluation Harness

### Problem

You need to know whether a change made the agent better or worse.

### Structure

```text
Eval Cases -> Agent Run -> Scoring -> Report -> Release Decision
```

### Use For

- prompt changes
- tool changes
- memory changes
- model upgrades
- production regression testing

### Failure Mode

The eval set only contains happy paths and misses the cases users actually care about.
