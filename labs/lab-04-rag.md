# Lab 04 - RAG

## Objective

Build a retrieval test set before trusting RAG answers.

## Estimated Time

60-90 minutes

## Read First

- `curriculum/04-rag-and-embeddings.md`
- `roadmap/level-0-ai-llm-fundamentals.md`

## Task

Create a small knowledge base with 5-10 documents and 10 questions.

For each question, record:

- expected relevant document
- expected answer facts
- acceptable uncertainty
- citation requirement

## Acceptance Criteria

Your RAG eval set must include:

- at least three direct lookup questions
- at least three synthesis questions
- at least two no-answer questions
- at least two adversarial or ambiguous questions

## Common Mistake

RAG does not automatically make answers true. It only gives the model more context. You still need to evaluate retrieval and generation separately.

## Extension

Track retrieval precision and answer faithfulness separately.
