"""Small auditable memory store for Example 04."""

from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


WORD_RE = re.compile(r"[A-Za-z0-9_]+")


@dataclass
class Memory:
    user_id: str
    text: str
    reason: str
    created_at: str


class JsonMemoryStore:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.path.parent.mkdir(parents=True, exist_ok=True)

    def load(self) -> list[Memory]:
        if not self.path.exists():
            return []
        data = json.loads(self.path.read_text(encoding="utf-8"))
        return [Memory(**item) for item in data]

    def save(self, memories: list[Memory]) -> None:
        data = [asdict(memory) for memory in memories]
        self.path.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    def add(self, user_id: str, text: str, reason: str) -> Memory:
        memory = Memory(
            user_id=user_id,
            text=text.strip(),
            reason=reason,
            created_at=datetime.now(timezone.utc).isoformat(),
        )
        memories = self.load()
        memories.append(memory)
        self.save(memories)
        return memory

    def search(self, user_id: str, query: str, limit: int = 3) -> list[Memory]:
        query_words = set(tokenize(query))
        scored: list[tuple[int, Memory]] = []
        for memory in self.load():
            if memory.user_id != user_id:
                continue
            score = len(query_words.intersection(tokenize(memory.text)))
            if score > 0:
                scored.append((score, memory))
        scored.sort(key=lambda item: (item[0], item[1].created_at), reverse=True)
        return [memory for _, memory in scored[:limit]]


def tokenize(text: str) -> list[str]:
    return [match.group(0).lower() for match in WORD_RE.finditer(text)]
