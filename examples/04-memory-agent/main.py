"""Example 04 - Memory Agent.

Run:
    python main.py
"""

from __future__ import annotations

import json
from pathlib import Path

from memory_store import JsonMemoryStore


BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = BASE_DIR / "agent_config.json"
MEMORY_PATH = BASE_DIR / "memory.json"


def load_config() -> dict:
    with CONFIG_PATH.open("r", encoding="utf-8") as file:
        return json.load(file)


def should_store(message: str, policy: dict) -> tuple[bool, str]:
    lowered = message.lower()
    for blocked in policy.get("never_store", []):
        if blocked in lowered:
            return False, f"Blocked by sensitive-data rule: {blocked}"
    for trigger in policy.get("write_when_message_contains", []):
        if trigger in lowered:
            return True, f"Matched write trigger: {trigger}"
    return False, "No memory trigger matched"


def build_response(message: str, memories: list) -> str:
    if memories:
        memory_lines = "\n".join(f"- {memory.text}" for memory in memories)
    else:
        memory_lines = "- No relevant memory found."

    return f"""Memory-aware response

Current request:
{message}

Retrieved memory:
{memory_lines}

Answer:
I will answer using the current request first, then use memory only when it is relevant and safe.
"""


def main() -> None:
    config = load_config()
    policy = config["memory_policy"]
    user_id = config["demo"]["default_user_id"]
    store = JsonMemoryStore(MEMORY_PATH)

    print("Memory Teaching Agent")
    print("=" * 22)
    print("Type a message. Use 'Remember ...' to write memory.\n")

    message = input("> ").strip()
    if not message:
        message = "Remember that I prefer Traditional Chinese explanations with examples."

    should_write, reason = should_store(message, policy)
    if should_write:
        memory = store.add(user_id=user_id, text=message, reason=reason)
        print(f"\nSaved memory: {memory.text}")
        print(f"Reason: {memory.reason}\n")

    memories = store.search(
        user_id=user_id,
        query=message,
        limit=int(policy.get("max_retrieved_memories", 3)),
    )
    print(build_response(message, memories))


if __name__ == "__main__":
    main()
