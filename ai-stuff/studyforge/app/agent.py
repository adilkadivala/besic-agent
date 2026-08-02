"""
Agentic loop: plan → tool → observe → (repeat) → final answer.

The LLM is asked to reply with either:
  {"tool": "name", "args": {...}}
or
  FINAL: ... plain answer ...
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass, field

from .llm import LLMClient
from .tools import TOOLS

SYSTEM_PROMPT = """You are StudyForge, a study agent for an AI student.
You can use tools by replying with ONLY a JSON object on one line:
{"tool": "TOOL_NAME", "args": {...}}

Available tools:
- calculator: args = {"expression": "17 * 24"}
- search_notes: args = {"query": "ReLU"}

When you can answer without tools, or after seeing tool results, reply with:
FINAL: your answer here

Keep answers short and clear for a beginner learner.
"""


@dataclass
class StepLog:
    kind: str  # THOUGHT / TOOL / RESULT / ANSWER
    content: str


@dataclass
class AgentResult:
    answer: str
    steps: list[StepLog] = field(default_factory=list)


def _parse_tool_call(text: str) -> dict | None:
    text = text.strip()
    # raw JSON
    try:
        data = json.loads(text)
        if isinstance(data, dict) and "tool" in data:
            return data
    except json.JSONDecodeError:
        pass
    # JSON embedded in text
    m = re.search(r"\{[^{}]*\"tool\"[^{}]*\}", text, re.DOTALL)
    if m:
        try:
            data = json.loads(m.group(0))
            if isinstance(data, dict) and "tool" in data:
                return data
        except json.JSONDecodeError:
            pass
    return None


def run_agent(
    user_message: str,
    llm: LLMClient | None = None,
    max_steps: int = 5,
    verbose: bool = True,
) -> AgentResult:
    llm = llm or LLMClient(mode="auto")
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message},
    ]
    steps: list[StepLog] = []

    if verbose:
        print(f"[mode={llm.mode} model={llm.model}]")

    for i in range(max_steps):
        raw = llm.chat(messages)
        steps.append(StepLog("THOUGHT", raw))
        if verbose:
            print(f"\n--- step {i + 1} THOUGHT ---\n{raw}")

        if raw.strip().upper().startswith("FINAL:") or raw.strip().lower().startswith("final:"):
            answer = raw.split(":", 1)[1].strip() if ":" in raw else raw
            steps.append(StepLog("ANSWER", answer))
            if verbose:
                print(f"\n--- ANSWER ---\n{answer}")
            return AgentResult(answer=answer, steps=steps)

        call = _parse_tool_call(raw)
        if not call:
            # treat as final if no tool
            steps.append(StepLog("ANSWER", raw))
            if verbose:
                print(f"\n--- ANSWER (no tool) ---\n{raw}")
            return AgentResult(answer=raw, steps=steps)

        name = call.get("tool", "")
        args = call.get("args") or {}
        steps.append(StepLog("TOOL", f"{name}({args})"))
        if verbose:
            print(f"\n--- TOOL ---\n{name}({args})")

        if name not in TOOLS:
            result = f"Error: unknown tool '{name}'. Use calculator or search_notes."
        else:
            try:
                result = TOOLS[name](**args) if args else TOOLS[name]()
            except TypeError as e:
                result = f"Error calling {name}: {e}"

        steps.append(StepLog("RESULT", str(result)))
        if verbose:
            print(f"\n--- RESULT ---\n{result}")

        # Feed tool result back into the conversation
        messages.append({"role": "assistant", "content": raw})
        messages.append(
            {
                "role": "user",
                "content": f"TOOL_RESULT from {name}:\n{result}\n\nNow give FINAL: answer for the user.",
            }
        )

    answer = "Stopped: max agent steps reached."
    steps.append(StepLog("ANSWER", answer))
    return AgentResult(answer=answer, steps=steps)
