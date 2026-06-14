# Agent Colony Architecture

## Overview

An Agent Colony is a coordinated system of specialized agents connected through shared memory, MCP tools, workflow orchestration, and evaluation loops.

## Core Components

- Supervisor Agent
- Specialist Agents
- Memory Agent
- Tool Agent
- MCP Router
- Evaluator Agent
- Shared Memory
- Human-in-the-loop approval

## Reference Flow

```text
User Request
  ↓
Supervisor Agent
  ↓
Task Decomposition
  ↓
Specialist Agents + MCP Tools
  ↓
Evaluator Agent
  ↓
Final Response
  ↓
Memory Update
```
