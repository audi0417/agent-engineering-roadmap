# Module 06 — Graph-based Agents

[繁體中文](06-graph-based-agents_zh.md)

## Goal

Learn how to model agent workflows as graphs and state machines.

Graph-based design helps developers build controllable, inspectable, and reusable agent workflows.

---

## Mental Model

```text
Node = step
Edge = transition
State = shared workflow data
```

---

## Core Concepts

### Node

A node represents one step in the workflow, such as planning, retrieval, tool use, or review.

### Edge

An edge defines how the workflow moves between nodes.

### State

State stores shared workflow data such as user input, intermediate outputs, tool results, and review status.

### Conditional Routing

The graph can choose different paths based on state.

### Checkpointing

Checkpointing allows the workflow to pause, resume, or recover.

---

## Architecture Diagram

```mermaid
flowchart TD
    Start[Start] --> Planner[Planner Node]
    Planner --> Router{Route}
    Router -->|Need Data| Retrieval[Retrieval Node]
    Router -->|Need Tool| Tool[Tool Node]
    Retrieval --> Review[Review Node]
    Tool --> Review
    Review -->|Pass| End[End]
    Review -->|Revise| Planner
```

---

## Hands-on Exercise

Design a graph workflow:

```text
Workflow goal:
Nodes:
Edges:
State fields:
Conditional routes:
Checkpoint strategy:
Failure behavior:
```

---

## Checklist

You understand this module if you can:

- explain nodes, edges, and state
- design conditional routing
- separate workflow state from model output
- explain why checkpointing matters
- convert a linear workflow into a graph

---

## Common Mistakes

- Making the graph too complex too early
- Storing unclear state
- No failure path
- No checkpoint strategy
- Treating graph design as visual decoration instead of control logic

---

## Outcome

After this module, you should be able to design graph-based agent workflows.

Next module: [Module 07 — Multi-Agent Systems](07-multi-agent-systems.md)
