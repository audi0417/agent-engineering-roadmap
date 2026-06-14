# Level 3 — Model Context Protocol (MCP)

## Goal

Use MCP to standardize how agents connect to tools, data sources, and external systems.

MCP is important because production agents rarely work alone. They need to read files, query databases, call APIs, access domain systems, and operate under clear permission boundaries.

---

## Core Concepts

### MCP Client

The application or agent runtime that connects to one or more MCP servers.

### MCP Server

A service that exposes tools, resources, and prompts to the client through a standard protocol.

### Tools

Executable actions the agent can call, such as reading a database record, creating a task, or searching a document.

### Resources

Readable context exposed by the server, such as files, records, schemas, documents, or logs.

### Prompts

Reusable prompt templates that help standardize domain-specific workflows.

---

## Why MCP Matters for Agent Engineering

Without MCP, every agent integration becomes custom glue code.

With MCP, agent systems can use a more modular architecture:

```text
Agent Runtime
   ↓
MCP Client
   ↓
MCP Servers
   ↓
Tools / Resources / Data Sources
```

This allows developers to separate agent reasoning from system integration.

---

## What to Learn

- How MCP clients discover tools
- How MCP servers expose tools and resources
- How tool schemas are defined
- How agents decide when to call tools
- How to manage authentication and permissions
- How to run local and remote MCP servers
- How to design safe MCP boundaries

---

## Hands-on Projects

### Project 1 — Filesystem MCP Server

Build a server that allows an agent to list, read, and summarize files in a controlled directory.

Learning points:

- tool schema design
- file permission boundaries
- resource exposure
- safe read-only access

### Project 2 — Database MCP Server

Build a server that exposes read-only SQL queries or predefined database operations.

Learning points:

- query validation
- schema discovery
- preventing destructive operations
- structured result formatting

### Project 3 — Memory MCP Server

Build a server that allows agents to write and retrieve long-term memory.

Learning points:

- memory write policy
- semantic retrieval
- metadata filtering
- memory auditing

### Project 4 — Health Record Demo MCP Server

Build a domain MCP server that exposes synthetic patient profile, nutrition logs, vital signs, and care notes.

Learning points:

- domain-specific tool design
- privacy boundary design
- safe healthcare decision support
- integration with healthcare agent workflows

---

## Design Checklist

When designing an MCP server, ask:

- What actions should the agent be allowed to perform?
- What actions should require human approval?
- What data should be exposed as resources?
- What data should never be exposed?
- Should the server be read-only or read-write?
- How will tool calls be logged?
- How will errors be returned to the agent?
- How will prompt injection risks be reduced?

---

## Common Mistakes

- Giving agents unrestricted file or database access
- Exposing raw sensitive data without filtering
- Designing tools that are too broad
- Allowing destructive actions without approval
- Returning unstructured tool results
- Treating MCP as a toy plugin instead of a system boundary

---

## Outcome

After this level, you should be able to design MCP servers as the integration layer of an agentic application.

You should also understand that MCP is not only a technical protocol. It is a system design boundary between reasoning, tools, data, and permissions.
