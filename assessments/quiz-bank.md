# Agent Engineering Quiz Bank

Use these questions to check whether you understand the course concepts.

## Module 00 - Foundations

1. What is the difference between a chatbot and an agent?
2. Why should an agent have a narrow goal?
3. What are the five parts of the minimal agent loop?
4. Give one example of an action that should require human approval.
5. Why is "help the user" not a good agent goal?

## Module 01 - Architecture

1. What are the main components of an agent system?
2. Why should output format be defined before implementation?
3. What belongs in system instructions?
4. What belongs in workflow state?
5. What is one failure mode of an overly broad architecture?

## Module 02 - Tool Calling

1. When should an agent call a tool?
2. What should a tool schema validate?
3. Why are tool outputs untrusted?
4. What makes a tool high risk?
5. How can you log tool calls for debugging?

## Module 03 - Memory

1. What is the difference between memory and context?
2. What should never be stored by default?
3. Why does memory need an audit log?
4. What is the difference between semantic and episodic memory?
5. How can stale memory harm an agent?

## Module 04 - RAG

1. What problem does RAG solve?
2. What are retrieval precision and recall?
3. Why should no-answer questions be in a RAG eval set?
4. What is answer faithfulness?
5. Why does more context sometimes make answers worse?

## Module 05 - Workflow

1. Why is workflow useful for agent reliability?
2. What is a planner-executor pattern?
3. What should a reviewer check?
4. Why should workflows have a maximum step count?
5. What is a good retry policy?

## Module 06 - Graph-based Agents

1. Why model an agent as a graph?
2. What is a state?
3. What is a conditional edge?
4. Where should error handling appear in the graph?
5. When is a graph overkill?

## Module 07 - Multi-Agent Systems

1. When is multi-agent useful?
2. Why can multi-agent systems become harder to debug?
3. What is a supervisor agent?
4. What is shared memory?
5. How should conflicts between agents be resolved?

## Module 08 - Human-in-the-loop

1. What actions should require approval?
2. What information should an approval request include?
3. What is the difference between review and approval?
4. Why should approval decisions be logged?
5. When should the agent refuse instead of asking for approval?

## Module 09 - Production

1. What should be logged for observability?
2. What is a regression eval?
3. Why is cost control part of agent design?
4. What is prompt injection?
5. How can a deployment be rolled back?

## Practical Review Questions

1. Design a memory policy for a tutoring agent.
2. Design a tool policy for a finance research agent.
3. Design a RAG eval set for an internal documentation assistant.
4. Design a workflow for a support ticket triage agent.
5. Design a human approval gate for an email-sending agent.

## Practical Coding Checks

1. Run `python scripts/verify_examples.py`. Which examples are deterministic and why is that useful for teaching?
2. In Example 08, what is the difference between `retrieval_passed` and `answer_passed`?
3. Add a no-answer RAG case. What should the agent say when the knowledge base lacks evidence?
4. Break one tool schema in Example 02. What kind of failure should the evaluation catch before release?
5. Add one high-risk domain request to a showcase. Which safety boundary should block or escalate it?
