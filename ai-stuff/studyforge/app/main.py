#!/usr/bin/env python3
"""StudyForge CLI — chat with your study agent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

# Allow: python -m app.main  from studyforge/
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.agent import run_agent
from app.llm import LLMClient


def main():
    parser = argparse.ArgumentParser(description="StudyForge — agentic study assistant")
    parser.add_argument(
        "--mode",
        choices=["auto", "mock", "ollama"],
        default="auto",
        help="auto=Ollama if up else mock (default)",
    )
    parser.add_argument(
        "--model",
        default=None,
        help="Ollama model name (default: tinyllama)",
    )
    parser.add_argument(
        "-q",
        "--query",
        default=None,
        help="Single question then exit (no interactive loop)",
    )
    args = parser.parse_args()

    kwargs = {"mode": args.mode}
    if args.model:
        kwargs["model"] = args.model
    llm = LLMClient(**kwargs)

    print("=" * 50)
    print(" StudyForge — Tiny LLM + Agentic Study Agent")
    print("=" * 50)
    print(f" LLM mode: {llm.mode}  |  model: {llm.model}")
    print(" Tools: calculator, search_notes")
    print(" Type 'quit' or 'exit' to leave.")
    print(" Try: What is 17 * 24?")
    print(" Try: Search notes for ReLU")
    print("=" * 50)

    if args.query:
        run_agent(args.query, llm=llm)
        return

    while True:
        try:
            user = input("\nYou> ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nBye!")
            break
        if not user:
            continue
        if user.lower() in {"quit", "exit", "q"}:
            print("Bye!")
            break
        run_agent(user, llm=llm)


if __name__ == "__main__":
    main()
