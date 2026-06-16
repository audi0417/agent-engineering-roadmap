"""Durable workflow agent with checkpoint and resume."""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
import json
from pathlib import Path


STEPS = ["classify", "plan", "execute", "review", "finalize"]


@dataclass
class WorkflowState:
    task: str
    current_step: int = 0
    artifacts: dict[str, str] = field(default_factory=dict)
    completed: bool = False


def save_checkpoint(path: Path, state: WorkflowState) -> None:
    path.write_text(json.dumps(asdict(state), indent=2), encoding="utf-8")


def load_checkpoint(path: Path) -> WorkflowState:
    data = json.loads(path.read_text(encoding="utf-8"))
    return WorkflowState(**data)


def run_step(state: WorkflowState) -> WorkflowState:
    step = STEPS[state.current_step]
    if step == "classify":
        state.artifacts[step] = "support_workflow"
    elif step == "plan":
        state.artifacts[step] = "check account status, draft reply, review risk"
    elif step == "execute":
        state.artifacts[step] = "read-only investigation completed"
    elif step == "review":
        state.artifacts[step] = "passed: no destructive tool call"
    elif step == "finalize":
        state.artifacts[step] = "final response ready"
        state.completed = True

    state.current_step += 1
    return state


def run_until_checkpoint(
    task: str,
    checkpoint_path: Path,
    stop_after_steps: int | None = None,
) -> WorkflowState:
    if checkpoint_path.exists():
        state = load_checkpoint(checkpoint_path)
    else:
        state = WorkflowState(task=task)

    steps_run = 0
    while not state.completed and state.current_step < len(STEPS):
        state = run_step(state)
        save_checkpoint(checkpoint_path, state)
        steps_run += 1
        if stop_after_steps is not None and steps_run >= stop_after_steps:
            break

    return state


def summarize(state: WorkflowState) -> str:
    status = "completed" if state.completed else "paused"
    return (
        f"Workflow {status}. "
        f"Step index: {state.current_step}/{len(STEPS)}. "
        f"Artifacts: {', '.join(sorted(state.artifacts))}."
    )

