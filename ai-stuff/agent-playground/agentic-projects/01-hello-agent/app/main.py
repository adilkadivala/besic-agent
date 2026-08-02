#!/usr/bin/env python3
"""CLI for 01-hello-agent."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.agent import run_agent


def main():
    parser = argparse.ArgumentParser(description="01-hello-agent — first agentic loop")
    parser.add_argument("-q", "--query", default=None, help="One question then exit")
    args = parser.parse_args()

    print("=" * 50)
    print(" 01-hello-agent  |  learn by building")
    print(" Tools: calculator, get_time, echo")
    print(" No LLM — keyword router (Project 02 adds LLM)")
    print("=" * 50)

    if args.query:
        run_agent(args.query)
        return

    print("Type 'quit' to exit. Try: What is 17 * 24?")
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
        run_agent(user)


if __name__ == "__main__":
    main()
