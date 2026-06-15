# Agent Engineering Glossary

## Agent

A goal-directed system that uses context, model calls, tools, memory, workflow, and evaluation to complete tasks.

## Agentic Workflow

A controlled sequence of steps where an agent plans, acts, observes, reviews, and produces an output.

## Context Window

The maximum amount of text or tokens a model can consider in one call.

## Context Engineering

The practice of selecting, structuring, compressing, retrieving, and updating the information given to a model or agent.

## Tool Calling

The ability for a model or agent to request external functions, APIs, databases, or services.

## MCP

Model Context Protocol. A protocol for connecting models and agents to external tools, resources, and prompts in a standardized way.

## Memory

Persisted context that can be reused across turns, tasks, users, or agents.

## Short-Term Memory

Temporary task state used during a single session or workflow.

## Long-Term Memory

Persistent information that may be reused in future sessions.

## Semantic Memory

Stored knowledge such as facts, concepts, and preferences.

## Episodic Memory

Stored event history such as actions taken, decisions made, or user interactions.

## Shared Memory

Memory accessible by multiple agents in a workflow or colony.

## RAG

Retrieval-Augmented Generation. A method that retrieves external information and gives it to the model before generating an answer.

## Embedding

A vector representation of text, images, or other data that makes similarity search possible.

## Vector Database

A database optimized for storing embeddings and retrieving similar items.

## Planner

A component or agent that decomposes a task into steps.

## Executor

A component or agent that performs planned steps or tool calls.

## Reviewer

A component or agent that checks a draft or intermediate result against a rubric.

## Evaluator

A component, model, script, or human process that scores behavior against expected criteria.

## Human-in-the-loop

A design where humans review, approve, correct, or escalate agent actions.

## Approval Gate

A checkpoint that blocks high-risk actions until a human approves them.

## Prompt Injection

An attack or accidental instruction conflict where untrusted content tries to override the system's intended behavior.

## Guardrail

A rule, validator, policy, or runtime check that keeps the agent inside allowed behavior.

## Evaluation Suite

A set of test cases used to measure agent quality, safety, formatting, tool use, and regression behavior.

## Regression

A change that makes previously working behavior fail.

## Observability

The ability to inspect model calls, tool calls, memory operations, errors, cost, latency, and decisions.

## Agent Colony

A group of specialized agents coordinated through shared goals, memory, workflow, evaluation, and governance.
