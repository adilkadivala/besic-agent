# 01 — Hello Agent

**Goal:** Build your first **agentic loop** without an LLM.

```text
User goal
  → Agent decides a TOOL
  → Run tool → OBSERVE result
  → Maybe another tool
  → FINAL answer
```

## Concepts you learn

| Concept | In this project |
|---------|-----------------|
| **Tool** | A function the agent can call (`calculator`, `get_time`, `echo`) |
| **Agent loop** | plan → act → observe → repeat |
| **Max steps** | stop so it can’t loop forever |
| **Router** | simple rules (keywords) choose the tool — later an LLM will |

## Run

```bash
cd ai-playground/agentic-projects/01-hello-agent
python3 -m app.main
python3 -m app.main -q "What is 17 * 24?"
python3 -m app.main -q "What time is it?"
python3 tests/test_tools.py
```

## Try these

- `What is 12 + 30?`
- `What time is it?`
- `Echo hello agent`

## Next project

`02-llm-tool-agent` — replace the keyword router with a small local LLM (Ollama).
