"""
Agent loop (no LLM yet).

Learning target:
  THINK  → choose tool or final answer
  ACT    → run tool
  OBSERVE → read tool result
  repeat until FINAL or max_steps
"""

from __future__ import annotations

import re
from dataclasses import dataclass, field

from .tools import TOOLS, calculator


@dataclass
class Step:
    kind: str  # THINK | ACT | OBSERVE | FINAL
    content: str


@dataclass
class AgentResult:
    answer: str
    steps: list[Step] = field(default_factory=list)


def _extract_math(text: str) -> str | None:
    """Pull a simple expression like 17 * 24 from a sentence."""
    m = re.search(r"(\d+\s*[\+\-\*/]\s*\d+(?:\s*[\+\-\*/]\s*\d+)*)", text)
    return m.group(1).replace(" ", "") if m else None


def think(user_message: str, last_observe: str | None) -> tuple[str, dict | None]:
    """
    Keyword router (fake 'brain').
    Returns:
      ("FINAL", {"text": "..."}) or
      ("TOOL", {"name": "...", "arg": "..."})
    """
    low = user_message.lower().strip()

    # After we already ran a tool, produce a final answer from observation
    if last_observe is not None:
        if last_observe.startswith("Error"):
            return "FINAL", {"text": f"Tool failed: {last_observe}"}
        # If observation looks like a number from calculator
        if re.fullmatch(r"-?\d+(\.\d+)?", last_observe.strip()):
            return "FINAL", {"text": f"The answer is {last_observe}"}
        if "You said:" in last_observe:
            return "FINAL", {"text": last_observe}
        return "FINAL", {"text": f"Result: {last_observe}"}

    # Time
    if any(k in low for k in ["time", "clock", "date", "today"]):
        return "TOOL", {"name": "get_time", "arg": ""}

    # Echo
    if low.startswith("echo ") or "echo " in low:
        text = user_message.split("echo", 1)[-1].strip(" :")
        return "TOOL", {"name": "echo", "arg": text or user_message}

    # Math
    expr = _extract_math(user_message)
    if expr or any(k in low for k in ["calculate", "what is", "compute", "math"]):
        if not expr:
            # try after 'is'
            if "is" in low:
                tail = user_message.lower().split("is", 1)[-1]
                expr = _extract_math(tail) or tail.strip(" ?")
            else:
                expr = user_message
        return "TOOL", {"name": "calculator", "arg": expr or "0"}

    # Default: no tool
    return "FINAL", {
        "text": (
            "I am a simple rule-based agent (no LLM yet). "
            "Try: 'What is 17 * 24?' or 'What time is it?' or 'Echo hello'"
        )
    }


def run_agent(user_message: str, max_steps: int = 4, verbose: bool = True) -> AgentResult:
    steps: list[Step] = []
    last_observe: str | None = None

    for i in range(max_steps):
        decision, payload = think(user_message, last_observe)
        steps.append(Step("THINK", f"{decision}: {payload}"))
        if verbose:
            print(f"\n--- step {i + 1} THINK ---\n{decision}: {payload}")

        if decision == "FINAL":
            answer = payload["text"]
            steps.append(Step("FINAL", answer))
            if verbose:
                print(f"\n--- FINAL ---\n{answer}")
            return AgentResult(answer=answer, steps=steps)

        # ACT
        name = payload["name"]
        arg = payload.get("arg", "")
        steps.append(Step("ACT", f"{name}({arg!r})"))
        if verbose:
            print(f"\n--- ACT ---\n{name}({arg!r})")

        if name not in TOOLS:
            result = f"Error: unknown tool {name}"
        else:
            result = TOOLS[name](arg)

        # OBSERVE
        last_observe = str(result)
        steps.append(Step("OBSERVE", last_observe))
        if verbose:
            print(f"\n--- OBSERVE ---\n{last_observe}")

    answer = "Stopped: max steps reached."
    steps.append(Step("FINAL", answer))
    if verbose:
        print(f"\n--- FINAL ---\n{answer}")
    return AgentResult(answer=answer, steps=steps)
