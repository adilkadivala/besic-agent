"""Tools the agent can call. Each tool is a plain function → string result."""

from __future__ import annotations

import ast
import operator
from datetime import datetime

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.USub: operator.neg,
}


def _eval_node(node):
    if isinstance(node, ast.Expression):
        return _eval_node(node.body)
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)):
        return node.value
    if isinstance(node, ast.Num):  # pragma: no cover
        return node.n
    if isinstance(node, ast.BinOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.left), _eval_node(node.right))
    if isinstance(node, ast.UnaryOp) and type(node.op) in _OPS:
        return _OPS[type(node.op)](_eval_node(node.operand))
    raise ValueError("Only simple math is allowed")


def calculator(expression: str) -> str:
    """Evaluate a simple math expression like '17 * 24'."""
    expression = (expression or "").strip()
    if not expression:
        return "Error: empty expression"
    try:
        tree = ast.parse(expression, mode="eval")
        return str(_eval_node(tree))
    except Exception as e:
        return f"Error: {e}"


def get_time(_: str = "") -> str:
    """Return current local time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def echo(text: str) -> str:
    """Repeat the text back (debug tool)."""
    return f"You said: {(text or '').strip()}"


# Registry: name → function
TOOLS = {
    "calculator": calculator,
    "get_time": get_time,
    "echo": echo,
}
