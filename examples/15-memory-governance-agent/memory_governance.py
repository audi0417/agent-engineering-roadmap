"""Memory governance example for production agents."""

from __future__ import annotations

from dataclasses import asdict, dataclass
import json
import re
from pathlib import Path
from typing import Any


EMAIL_RE = re.compile(r"[\w.+-]+@[\w-]+\.[\w.-]+")
PHONE_RE = re.compile(r"\b\d{3}[- ]?\d{3}[- ]?\d{4}\b")


@dataclass
class MemoryRecord:
    key: str
    value: str
    category: str
    confidence: float
    retention: str
    source: str


class GovernedMemoryStore:
    def __init__(self) -> None:
        self.records: dict[str, MemoryRecord] = {}
        self.audit_log: list[dict[str, Any]] = []

    def redact(self, text: str) -> str:
        text = EMAIL_RE.sub("[redacted-email]", text)
        return PHONE_RE.sub("[redacted-phone]", text)

    def classify(self, text: str) -> tuple[str, str]:
        lowered = text.lower()
        if any(term in lowered for term in ["email", "@", "phone", "address"]):
            return "pii", "session"
        if any(term in lowered for term in ["prefer", "likes", "language"]):
            return "preference", "long_term"
        return "task_context", "short_term"

    def write(self, key: str, value: str, source: str) -> MemoryRecord:
        category, retention = self.classify(value)
        safe_value = self.redact(value)
        existing = self.records.get(key)

        if existing:
            merged_value = safe_value if safe_value in existing.value else f"{existing.value}; {safe_value}"
            confidence = min(1.0, existing.confidence + 0.1)
            record = MemoryRecord(key, merged_value, category, confidence, retention, source)
            action = "merge"
        else:
            record = MemoryRecord(key, safe_value, category, 0.8, retention, source)
            action = "write"

        self.records[key] = record
        self.audit_log.append({"action": action, "key": key, "category": category})
        return record

    def decay(self, key: str, amount: float = 0.2) -> MemoryRecord:
        record = self.records[key]
        record.confidence = max(0.0, round(record.confidence - amount, 2))
        self.audit_log.append({"action": "decay", "key": key, "confidence": record.confidence})
        return record

    def delete(self, key: str, reason: str) -> None:
        self.records.pop(key, None)
        self.audit_log.append({"action": "delete", "key": key, "reason": reason})

    def export(self) -> dict[str, Any]:
        return {
            "records": {key: asdict(record) for key, record in self.records.items()},
            "audit_log": self.audit_log,
        }


def run_demo() -> dict[str, Any]:
    store = GovernedMemoryStore()
    store.write("language_preference", "User prefers Traditional Chinese examples.", "chat")
    store.write("contact", "User email is learner@example.com and phone is 555-123-4567.", "chat")
    store.write("language_preference", "User prefers Traditional Chinese examples.", "followup")
    store.decay("language_preference")
    store.delete("contact", "PII should not be retained beyond session.")
    return store.export()


def run_eval(eval_path: Path) -> dict[str, Any]:
    cases = json.loads(eval_path.read_text(encoding="utf-8"))
    results = []
    for case in cases:
        store = GovernedMemoryStore()
        for item in case["writes"]:
            store.write(item["key"], item["value"], item["source"])
        for key in case.get("delete", []):
            store.delete(key, "eval deletion")
        output = store.export()
        serialized = json.dumps(output)
        passed = all(term in serialized for term in case["must_include"]) and all(
            term not in serialized for term in case["must_not_include"]
        )
        results.append({"name": case["name"], "passed": passed, "output": output})
    return {
        "passed": sum(1 for result in results if result["passed"]),
        "total": len(results),
        "results": results,
    }

