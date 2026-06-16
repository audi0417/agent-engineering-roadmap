from __future__ import annotations

from pathlib import Path

from durable_agent import load_checkpoint, run_until_checkpoint, summarize


DEFAULT_TASK = "Investigate a billing access ticket without changing production data."


def main() -> int:
    print("Durable Workflow Agent")
    print("======================")
    try:
        task = input("Task > ").strip() or DEFAULT_TASK
    except EOFError:
        task = DEFAULT_TASK
    checkpoint_path = Path(__file__).with_name("checkpoint.json")

    if checkpoint_path.exists():
        checkpoint_path.unlink()

    paused = run_until_checkpoint(task, checkpoint_path, stop_after_steps=2)
    print("\n=== Before Resume ===")
    print(summarize(paused))

    resumed = run_until_checkpoint(task, checkpoint_path)
    print("\n=== After Resume ===")
    print(summarize(resumed))
    print(f"checkpoint: {checkpoint_path}")

    loaded = load_checkpoint(checkpoint_path)
    passed = loaded.completed and "review" in loaded.artifacts
    print("\n=== Eval Report ===")
    print("[PASS] resume_from_checkpoint" if passed else "[FAIL] resume_from_checkpoint")
    return 0 if passed else 1


if __name__ == "__main__":
    raise SystemExit(main())
