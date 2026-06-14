"""Local tools for Example 02 — Tool-Using Agent."""

from __future__ import annotations

import ast
import operator
from typing import Any, Callable


class ToolError(Exception):
    """Raised when a tool receives invalid input or cannot complete safely."""


_ALLOWED_OPERATORS: dict[type[ast.operator], Callable[[Any, Any], Any]] = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
}

_ALLOWED_UNARY: dict[type[ast.unaryop], Callable[[Any], Any]] = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _safe_eval(node: ast.AST) -> float:
    if isinstance(node, ast.Expression):
        return _safe_eval(node.body)

    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value

    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_OPERATORS:
            raise ToolError(f"Operator {op_type.__name__} is not allowed.")
        left = _safe_eval(node.left)
        right = _safe_eval(node.right)
        return _ALLOWED_OPERATORS[op_type](left, right)

    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in _ALLOWED_UNARY:
            raise ToolError(f"Unary operator {op_type.__name__} is not allowed.")
        operand = _safe_eval(node.operand)
        return _ALLOWED_UNARY[op_type](operand)

    raise ToolError(f"Expression type {type(node).__name__} is not allowed.")


def calculator(expression: str) -> dict[str, Any]:
    """Safely evaluate a simple arithmetic expression."""
    if not expression or len(expression) > 120:
        raise ToolError("Expression is empty or too long.")

    tree = ast.parse(expression, mode="eval")
    result = _safe_eval(tree)
    return {"expression": expression, "result": result}


def word_count(text: str) -> dict[str, Any]:
    """Count words and characters in text."""
    if text is None:
        raise ToolError("Text is required.")

    words = [word for word in text.strip().split() if word]
    return {
        "word_count": len(words),
        "character_count": len(text),
        "character_count_no_spaces": len(text.replace(" ", "")),
    }


def todo_builder(notes: str) -> dict[str, Any]:
    """Turn simple comma-separated or line-separated notes into todo items."""
    if not notes or not notes.strip():
        raise ToolError("Notes are required.")

    raw_items = notes.replace("\n", ",").split(",")
    items = [item.strip().rstrip(".") for item in raw_items if item.strip()]

    return {
        "todo_count": len(items),
        "todos": [{"id": index + 1, "task": item} for index, item in enumerate(items)],
    }


TOOL_REGISTRY: dict[str, Callable[..., dict[str, Any]]] = {
    "calculator": calculator,
    "word_count": word_count,
    "todo_builder": todo_builder,
}


TOOL_SCHEMAS: list[dict[str, Any]] = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Safely evaluate a simple arithmetic expression.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "A simple arithmetic expression, such as '(128 * 42) / 7'.",
                    }
                },
                "required": ["expression"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "word_count",
            "description": "Count words and characters in a piece of text.",
            "parameters": {
                "type": "object",
                "properties": {
                    "text": {
                        "type": "string",
                        "description": "The text to analyze.",
                    }
                },
                "required": ["text"],
                "additionalProperties": False,
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "todo_builder",
            "description": "Turn messy notes into a structured todo list.",
            "parameters": {
                "type": "object",
                "properties": {
                    "notes": {
                        "type": "string",
                        "description": "Comma-separated or line-separated notes to convert into todo items.",
                    }
                },
                "required": ["notes"],
                "additionalProperties": False,
            },
        },
    },
]
