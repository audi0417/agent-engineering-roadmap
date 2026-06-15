"""Deterministic multi-agent workflow for Example 05."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Artifact:
    task: str
    plan: list[str] = field(default_factory=list)
    research_notes: list[str] = field(default_factory=list)
    draft: str = ""
    feedback: list[str] = field(default_factory=list)


def planner(task: str) -> list[str]:
    return [
        "Clarify the user goal and expected output.",
        "Identify the minimal implementation steps.",
        "Add a quality check before final delivery.",
        "Document risks and the next action.",
    ]


def researcher(task: str, plan: list[str]) -> list[str]:
    return [
        f"Task focus: {task}",
        "Agent systems need explicit stage contracts.",
        "Review gates catch missing requirements before output reaches users.",
        f"Planned stages: {len(plan)}",
    ]


def writer(artifact: Artifact) -> str:
    plan = "\n".join(f"{index + 1}. {step}" for index, step in enumerate(artifact.plan))
    notes = "\n".join(f"- {note}" for note in artifact.research_notes)
    return f"""Clear goal
Build a reliable workflow for: {artifact.task}

Implementation steps
{plan}

Research notes
{notes}

Risk or limitation
More agents do not automatically improve quality. The workflow needs explicit inputs, outputs, and review rules.

Next action
Run the workflow on one real task, inspect each artifact, then replace deterministic stages with LLM calls one at a time.
"""


def reviewer(draft: str, required_items: list[str]) -> list[str]:
    lowered = draft.lower()
    missing = [item for item in required_items if item.lower() not in lowered]
    return [f"Missing required section or concept: {item}" for item in missing]


def run_workflow(task: str, required_items: list[str], max_rounds: int) -> Artifact:
    artifact = Artifact(task=task)
    artifact.plan = planner(task)
    artifact.research_notes = researcher(task, artifact.plan)

    for _ in range(max_rounds + 1):
        artifact.draft = writer(artifact)
        artifact.feedback = reviewer(artifact.draft, required_items)
        if not artifact.feedback:
            break

    return artifact
