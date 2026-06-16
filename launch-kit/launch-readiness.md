# Launch Readiness

This file records whether the repository is ready to share publicly.

## Summary

Status: `Launch-ready`

The project now has a complete course path, runnable examples, lab solution guides, domain casebooks, a capstone starter, GitHub Pages, and CI verification for dependency-free examples.

## Readiness Checks

| Area | Status | Evidence |
|---|---|---|
| Course map | Pass | `COURSE.md`, `COURSE_zh.md`, `curriculum/README.md` |
| Bilingual core curriculum | Pass | Modules 00-12 in English and Traditional Chinese |
| Deep-dive chapters | Pass | Modules 03-12 include Deep Dive sections |
| Runnable examples | Pass | Examples 01-09 |
| Dependency-free verification | Pass | `scripts/verify_examples.py` |
| CI | Pass | `.github/workflows/verify-examples.yml` |
| GitHub Pages | Pass | `docs/index.html` deployed from Actions |
| Labs | Pass | Labs 00-10 |
| Lab solution guides | Pass | `lab-solutions/` |
| Capstone | Pass | `projects/capstone-agent-colony.md`, `capstone-starter/` |
| Domain practice | Pass | `domain-casebooks/` and showcases |
| Safety and eval emphasis | Pass | Evaluation harness, Mini RAG, Graph Approval Agent, casebooks |
| Contributor path | Pass | Issue templates and `CONTRIBUTING.md` |

## Verification Command

```bash
python scripts/verify_examples.py
```

Expected result:

```text
All runnable examples passed.
```

## Remaining Non-Blocking Launch Tasks

These are promotion tasks, not course-completion blockers:

- pin the repository on the GitHub profile
- add official GitHub repository topics
- share the launch post
- create 5 curated good-first-issue tasks
- collect early learner feedback

## Launch Positioning

Use this short positioning:

```text
Agent Engineering Roadmap is a bilingual, hands-on course for building production-aware AI agents with MCP-style tools, memory, RAG, workflows, human approval, evaluation, domain casebooks, and agent colonies.
```

## Quality Bar For Future Additions

New content should include:

- problem-first motivation
- one-sentence intuition
- black-box view
- concrete example
- runnable checkpoint or design artifact
- common failure modes
- evaluation or safety check

If an addition only explains a term but does not give a way to practice or evaluate it, it is not ready yet.
