# Contributing Guide

Thank you for your interest in contributing to Agent Engineering Roadmap.

This project is an educational repository for learning how to build AI agents, MCP-style integrations, memory systems, workflows, multi-agent systems, and production-ready agent applications.

---

## What you can contribute

You can contribute:

- curriculum improvements
- runnable examples
- architecture diagrams
- paper notes
- documentation fixes
- bilingual translations
- evaluation templates
- safety checklists

---

## Content Rules

All contributions must be original.

Do not submit:

- copied articles
- direct translations of external tutorials
- copied video transcripts
- unlicensed screenshots
- unverified third-party code
- private source notes
- platform-specific source lists

You may contribute original explanations inspired by general learning needs, but public repository content should not expose private source materials.

---

## File Structure

Follow the existing structure:

```text
curriculum/     Structured course modules
examples/       Runnable code examples
roadmap/        Learning roadmap
architecture/   System design notes
papers/         Paper reading notes
healthcare/     Healthcare domain track
finance/        Finance domain track
resources/      General resources and policies
```

---

## Bilingual Documentation

For major educational content, provide both English and Traditional Chinese versions when possible.

Use this naming convention:

```text
module-name.md       English
module-name_zh.md    Traditional Chinese
```

Each file should link to the other language version near the top.

---

## Lesson Format

Curriculum modules should follow this structure:

```text
Title
Language switch link
Goal
Why it matters
Mental model
Core concepts
Deep Dive
Black-box view
Naive failure
Mechanism
Architecture diagram
Hands-on exercise
Runnable or design checkpoint
Evaluation cases
Checklist
Common mistakes
Outcome
Next module
```

---

## Example Format

Runnable examples should include:

```text
README.md
README_zh.md
main.py
requirements.txt
.env.example
optional config files
```

Examples should be small, readable, and focused on one concept.

---

## Code Style

- Keep code beginner-friendly.
- Prefer clear names over clever abstractions.
- Add comments only when they improve understanding.
- Avoid unnecessary dependencies.
- Never commit secrets or API keys.

---

## Pull Request Checklist

Before submitting a pull request, check:

- [ ] The content is original.
- [ ] The file is placed in the correct folder.
- [ ] English and Chinese versions are linked when applicable.
- [ ] Code examples can run with the documented steps.
- [ ] `python scripts/verify_examples.py` passes if runnable examples are affected.
- [ ] New lessons include a problem-first explanation, a concrete example, and an eval or safety check.
- [ ] New production patterns include an owner, risk, observability, and release-gate consideration when relevant.
- [ ] No secrets or private notes are included.
- [ ] The contribution improves learning value.

## Pull Requests

Use the PR template in `.github/PULL_REQUEST_TEMPLATE.md`.

For runnable examples, include the command you ran and the expected pass/fail signal.

For curriculum changes, explain the learner outcome and the closest runnable example or checklist.

For production governance content, connect the change to at least one of:

- risk assessment
- permission scope
- memory governance
- observability
- incident response
- release gate

---

## Project Philosophy

This project values:

- practical learning
- clear structure
- safe agent design
- production awareness
- bilingual accessibility
- original educational content
