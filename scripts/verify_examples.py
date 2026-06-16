"""Run all dependency-free examples and showcases.

This script is intentionally boring. It gives contributors one command that
checks whether the course examples still run after a change.
"""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


COMMANDS = [
    ["python", "-m", "compileall", "examples", "showcases", "templates"],
    ["python", "examples/01-single-agent/main.py"],
    ["python", "examples/02-tool-using-agent/main.py"],
    ["python", "examples/03-mcp-agent/main.py"],
    ["python", "examples/04-memory-agent/main.py"],
    ["python", "examples/05-multi-agent-workflow/main.py"],
    ["python", "examples/06-agent-colony/main.py"],
    ["python", "examples/07-evaluation-harness/main.py"],
    ["python", "examples/08-mini-rag/main.py"],
    ["python", "showcases/enterprise-support-agent/main.py"],
    ["python", "showcases/finance-research-agent/main.py"],
    ["python", "showcases/healthcare-agent-colony/main.py"],
]

GENERATED_FILES = [
    ROOT / "examples/04-memory-agent/memory.json",
]


def clean_runtime_files() -> None:
    for path in GENERATED_FILES:
        if path.exists():
            path.unlink()


def run(command: list[str]) -> None:
    print(f"\n$ {' '.join(command)}")
    subprocess.run(
        command,
        cwd=ROOT,
        input="\n",
        text=True,
        check=True,
    )


def main() -> int:
    clean_runtime_files()
    for command in COMMANDS:
        run(command)
    clean_runtime_files()
    print("\nAll runnable examples passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
