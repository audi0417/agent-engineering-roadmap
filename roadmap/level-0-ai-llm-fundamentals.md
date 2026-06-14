# Level 0 — AI & LLM Fundamentals

## Goal

Understand the foundations required to build AI agent systems.

Before building agents, you need to understand how LLM applications work: how prompts shape behavior, how context is managed, how embeddings enable retrieval, how structured outputs make systems reliable, and how evaluation prevents silent failure.

---

## Mental Model

A basic LLM application usually looks like this:

```text
User Input
   ↓
Prompt Template
   ↓
LLM
   ↓
Output Parser
   ↓
Application Response
```

An agent system extends this by adding tools, memory, planning, and workflow control.

---

## Core Topics

### Large Language Models

Learn what LLMs are good at and where they fail.

LLMs are strong at:

- summarization
- classification
- reasoning over text
- code generation
- transformation tasks
- natural language interfaces

LLMs are weak at:

- guaranteed factual correctness
- long-horizon planning without structure
- precise numerical computation
- remembering information across sessions by default
- safely using tools without boundaries

### Prompt Engineering

Prompt engineering is not just writing clever instructions. It is the interface design between humans, models, tools, and tasks.

Learn:

- system prompts
- user prompts
- few-shot examples
- role prompting
- task decomposition
- output constraints
- refusal and safety instructions

### Context Window

The context window is the working memory of an LLM call.

Learn:

- what belongs in context
- what should be retrieved dynamically
- how context length affects cost and quality
- how to reduce irrelevant context
- how to structure context for tool-using agents

### Embeddings

Embeddings convert text into vectors so that similar meanings can be searched.

They are useful for:

- semantic search
- RAG
- memory retrieval
- document clustering
- recommendation
- duplicate detection

### Vector Databases

Vector databases store embeddings and allow similarity search.

Common options:

- Chroma
- Qdrant
- LanceDB
- Weaviate
- Pinecone
- PostgreSQL with pgvector

### Retrieval-Augmented Generation

RAG allows an LLM to answer using external knowledge.

Basic RAG flow:

```text
User Question
   ↓
Query Embedding
   ↓
Vector Search
   ↓
Retrieve Documents
   ↓
LLM Answer with Context
```

### Structured Outputs

Agents need reliable outputs, not just natural language.

Learn:

- JSON output
- schema validation
- Pydantic models
- tool call arguments
- function call schemas
- retry on invalid output

### Evaluation Basics

Evaluation is how you know whether your LLM app works.

Start with:

- exact match for deterministic tasks
- human review for qualitative tasks
- rubric-based evaluation
- retrieval precision and recall
- hallucination checks
- regression test sets

---

## Hands-on Projects

### Project 1 — Basic LLM Chat Interface

Build a simple chat app that sends user messages to an LLM and returns responses.

Learning points:

- API calls
- prompt formatting
- environment variables
- streaming output
- error handling

### Project 2 — Embedding Search Demo

Create a small document search system using embeddings.

Learning points:

- chunking
- embedding generation
- vector storage
- similarity search
- top-k retrieval

### Project 3 — Simple RAG Assistant

Build an assistant that answers questions using retrieved documents.

Learning points:

- retrieval pipeline
- context injection
- citation-aware answers
- hallucination reduction
- fallback behavior

### Project 4 — Structured Output Extractor

Build an extractor that converts unstructured text into JSON.

Learning points:

- schema design
- validation
- retries
- error messages
- downstream integration

---

## Checklist

You are ready for Level 1 when you can:

- explain what an LLM can and cannot do
- write a clear system prompt
- build a basic LLM call
- generate embeddings
- retrieve relevant documents
- build a simple RAG pipeline
- validate JSON output against a schema
- create a small evaluation dataset

---

## Common Mistakes

- Treating prompts as magic instead of interface design
- Putting too much irrelevant text into context
- Using RAG without evaluating retrieval quality
- Assuming the model remembers past sessions automatically
- Accepting free-form text when structured output is needed
- Skipping evaluation until production

---

## Outcome

You should understand how LLM applications work before adding tools, memory, and multi-agent orchestration.

This level gives you the foundation for building agents that are reliable instead of impressive only in demos.
