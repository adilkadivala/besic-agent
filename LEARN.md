# 01 — What you should understand after this build

## The agent loop

```text
THINK   → decide tool or final answer
ACT     → call tool
OBSERVE → read result
(repeat)
FINAL   → answer the user
```

This is the same shape as **ReAct**-style agents (Reason + Act).  
In Project 02, **THINK** will be done by an LLM instead of keywords.

## Tool

A **tool** is a function with a clear input/output the agent is allowed to use  
(e.g. calculator, search, HTTP API).

## Why max_steps?

Without a limit, a buggy agent can call tools forever.

## Map to PDFs (later reading)

| Concept | PDF (when you want theory) |
|---------|----------------------------|
| Agents | `learn/agentic-ai.pdf` |
| Loops | `learn/loopengineering.pdf` |
| Tools | `learn/mcp-interview.pdf` |
