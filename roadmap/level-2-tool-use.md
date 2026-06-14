# Level 2 — Tool Use

## Goal

Teach agents how to interact with external tools and APIs.

Tool use is the point where an LLM application becomes an agentic system. Instead of only generating text, the agent can take actions, retrieve fresh information, query data, calculate results, and interact with real software.

---

## Basic Tool-Using Agent Flow

```text
User Request
   ↓
Agent decides whether a tool is needed
   ↓
Agent selects a tool
   ↓
Agent generates tool arguments
   ↓
Tool executes
   ↓
Agent reads tool result
   ↓
Agent returns final answer
```

---

## Core Topics

### Function Calling

Function calling allows the model to produce structured arguments for a predefined function.

Example tool:

```json
{
  "name": "search_documents",
  "description": "Search internal documents by query",
  "parameters": {
    "query": "string",
    "top_k": "integer"
  }
}
```

### Tool Schema Design

A tool schema should clearly define:

- tool name
- purpose
- input parameters
- required fields
- output format
- permission level
- failure behavior

Good tools are narrow and explicit.

Bad tool:

```text
do_anything(input)
```

Better tools:

```text
read_file(path)
search_documents(query, top_k)
create_follow_up_task(patient_id, due_date, note)
```

### Tool Selection

The agent must decide whether a tool is needed.

Tool use is appropriate when the task requires:

- fresh information
- private data
- exact calculation
- database access
- file reading
- external system actions

Tool use is unnecessary when the task only requires rewriting, brainstorming, or explaining known context.

### Tool Chaining

Some tasks require multiple tool calls.

Example:

```text
Search customer record
   ↓
Read recent tickets
   ↓
Summarize issue
   ↓
Create follow-up task
```

### Tool Result Validation

Tool results should be checked before being used.

Validate:

- empty results
- malformed results
- permission errors
- stale data
- conflicting records
- unexpected response format

### Safe Tool Execution

Tools can change real systems. Safety matters.

Actions that may require approval:

- sending emails
- deleting files
- updating records
- placing orders
- making financial trades
- changing user permissions
- writing sensitive memory

---

## Tool Design Principles

1. Make tools narrow and specific.
2. Prefer read-only tools at first.
3. Add write actions only with clear approval gates.
4. Return structured results.
5. Make errors explicit.
6. Log tool calls.
7. Never expose secrets directly to the model.
8. Separate user-facing answers from raw tool outputs.

---

## Hands-on Projects

### Project 1 — Calculator Tool Agent

Build an agent that uses a calculator tool for arithmetic instead of relying on the LLM.

Learning points:

- exact computation
- tool selection
- result formatting

### Project 2 — File Reader Agent

Build an agent that can read files from a controlled directory and summarize them.

Learning points:

- file access boundaries
- path validation
- summarization with source context

### Project 3 — Database Query Agent

Build an agent that can query a database using predefined safe operations.

Learning points:

- read-only queries
- schema-aware retrieval
- SQL safety
- structured result interpretation

### Project 4 — Browser/Search Agent

Build an agent that can search for fresh information and cite sources.

Learning points:

- freshness
- source quality
- citation discipline
- conflict handling

---

## Tool Safety Checklist

Before exposing a tool to an agent, ask:

- Can this tool modify real-world state?
- Can this tool access private or sensitive data?
- Can this tool cause financial, legal, or medical harm?
- Does this tool need user confirmation?
- Are inputs validated?
- Are outputs structured?
- Are calls logged?
- Is there a rollback or recovery path?

---

## Common Mistakes

- Giving agents broad tools with too much power
- Not validating tool arguments
- Returning raw API responses directly to users
- Allowing destructive actions without approval
- Using tools when simple reasoning is enough
- Forgetting to handle failed tool calls
- Letting the model invent tool results

---

## Outcome

You should be able to design tools that agents can call reliably and safely.

This level prepares you for MCP, where tools and resources are exposed through a standardized protocol.
