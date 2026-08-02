"""
LLM client for StudyForge.

Modes:
  - mock: no server (always available) — for learning the agent loop offline
  - ollama: local small model (16GB RAM friendly: tinyllama, qwen2.5:0.5b, etc.)
"""

from __future__ import annotations

import json
import os
from typing import Any

import httpx

DEFAULT_OLLAMA_URL = os.environ.get("OLLAMA_HOST", "http://127.0.0.1:11434")
DEFAULT_MODEL = os.environ.get("STUDYFORGE_MODEL", "tinyllama")


class LLMClient:
    def __init__(
        self,
        mode: str = "auto",
        model: str = DEFAULT_MODEL,
        base_url: str = DEFAULT_OLLAMA_URL,
    ):
        """
        mode:
          - auto: use ollama if reachable, else mock
          - ollama: require Ollama
          - mock: never call network
        """
        self.model = model
        self.base_url = base_url.rstrip("/")
        if mode == "auto":
            self.mode = "ollama" if self._ollama_up() else "mock"
        else:
            self.mode = mode

    def _ollama_up(self) -> bool:
        try:
            r = httpx.get(f"{self.base_url}/api/tags", timeout=1.5)
            return r.status_code == 200
        except Exception:
            return False

    def chat(self, messages: list[dict[str, str]], temperature: float = 0.2) -> str:
        if self.mode == "mock":
            return self._mock_chat(messages)
        return self._ollama_chat(messages, temperature)

    def _ollama_chat(self, messages: list[dict[str, str]], temperature: float) -> str:
        payload: dict[str, Any] = {
            "model": self.model,
            "messages": messages,
            "stream": False,
            "options": {"temperature": temperature},
        }
        try:
            r = httpx.post(
                f"{self.base_url}/api/chat",
                json=payload,
                timeout=120.0,
            )
            r.raise_for_status()
            data = r.json()
            return data.get("message", {}).get("content", "") or ""
        except Exception as e:
            return f"[ollama error: {e}] Fall back tip: start ollama serve && ollama pull {self.model}"

    def _mock_chat(self, messages: list[dict[str, str]]) -> str:
        """
        Rule-based stand-in so the agent loop works without a model.
        Looks at the latest user message (and tool results in history).
        """
        user_texts = [m["content"] for m in messages if m.get("role") == "user"]
        last = user_texts[-1] if user_texts else ""
        low = last.lower()

        # If we already injected a tool result, produce a final answer.
        if "tool result" in low or last.startswith("TOOL_RESULT"):
            return (
                "FINAL: Based on the tool output above, here is the answer. "
                "(Mock LLM — start Ollama for real answers.)"
            )

        # Math-looking → calculator
        if any(op in last for op in ["*", "+", "-", "/", "="]) and any(c.isdigit() for c in last):
            # Extract a simple expression if possible
            expr = last
            for prefix in ["what is", "calculate", "compute", "how much is"]:
                if prefix in low:
                    expr = last[low.index(prefix) + len(prefix) :].strip(" ?")
                    break
            return json.dumps({"tool": "calculator", "args": {"expression": expr}})

        # Note search keywords
        if any(k in low for k in ["note", "relu", "backprop", "loss", "vector", "neuron", "what did i", "search"]):
            # pick a query word
            query = last
            for key in ["relu", "backprop", "loss", "vector", "neuron", "gradient", "token", "agent"]:
                if key in low:
                    query = key
                    break
            return json.dumps({"tool": "search_notes", "args": {"query": query}})

        return (
            "FINAL: I'm the mock LLM (Ollama not running). "
            "Try: 'What is 17 * 24?' or 'Search notes for ReLU'. "
            "Or run: ollama serve && ollama pull tinyllama"
        )
