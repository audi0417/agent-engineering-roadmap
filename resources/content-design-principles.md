# Content Design Principles

[繁體中文](content-design-principles_zh.md)

## Purpose

This document defines how to create original teaching content for the Agent Engineering Roadmap.

The repository should provide original explanations, diagrams, exercises, and code examples. It should not expose, copy, translate, or depend on any specific external teaching source.

---

## Core Principle

Do not reveal source materials.

Use external learning materials only as private inspiration for understanding common learner questions, confusing concepts, and useful teaching patterns. The final repository content must be original.

---

## Content Transformation Flow

```text
Private learning input
   ↓
Extract abstract concepts and learner pain points
   ↓
Remove source-specific wording, examples, and structure
   ↓
Create original English lesson
   ↓
Add original diagrams, checklists, and exercises
   ↓
Add original runnable code when useful
```

---

## What Can Be Used

Allowed:

- high-level concepts
- common learning questions
- common implementation challenges
- original explanations
- original diagrams
- original code examples
- original exercises
- original checklists

Not allowed:

- naming private source materials
- listing source platforms
- copying article structure
- translating full paragraphs
- copying screenshots
- copying code without license verification
- exposing private research notes

---

## Lesson Template

Each lesson should contain:

```text
Title
Goal
Why it matters
Mental model
Core concepts
Architecture diagram
Hands-on project
Checklist
Common mistakes
Outcome
```

---

## Writing Style

Good teaching content should be:

- practical
- concise
- implementation-oriented
- beginner-friendly but not shallow
- architecture-aware
- safety-aware
- production-aware

## Teaching Pattern

Each original lesson should make the learner feel the problem before naming the method.

Use this pattern:

```text
Problem
   ↓
Intuition
   ↓
Black-box input/output
   ↓
Internal mechanism
   ↓
Minimal runnable example
   ↓
Common failure mode
   ↓
Checklist
```

For example, do not introduce "memory architecture" as a definition first. Start with the failure: the agent forgets a stable user preference. Then ask what should be remembered, what should be retrieved, and what should never be stored. Only after that should the lesson name short-term memory, semantic memory, episodic memory, and shared memory.

Every major concept should include:

- one plain-language sentence
- one concrete example
- one architecture or flow diagram when useful
- one common mistake
- one practical next step

---

## Repository Policy

Public files should only include finished educational content.

Do not commit:

- raw research notes
- source lists
- private references
- copied text
- platform-specific scraping notes
- unverified third-party code
