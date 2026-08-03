# Agentic Projects — Learn by Building

**Rule:** one **folder** = one **project**.  
**Method:** build first → learn the concept from the code → short teacher Q&A.

```text
agentic-projects/
  01-hello-agent/      ← you are here
  02-llm-tool-agent/   ← next (Ollama)
  03-notes-rag-agent/
  ...
```

## Project roadmap

| # | Folder | You build | You learn |
|---|--------|-----------|-----------|
| **01** | `01-hello-agent` | Agent loop + calculator + time tools (no LLM) | tools, observe, max steps |
| **02** | `02-llm-tool-agent` | Same loop + Ollama small model | LLM tool calling, prompts |
| **03** | `03-notes-rag-agent` | Search your `notes/` + answer | RAG-lite, retrieval |
| **04** | `04-web-research-agent` | Search + summarize (API or mock) | multi-tool routing |
| **05** | `05-planner-agent` | Plan → execute checklist | planning, ReAct |
| **06** | `06-multi-agent-crew` | Researcher + Writer agents | multi-agent |
| **07** | `07-memory-agent` | Short + long memory | memory types |
| **08** | `08-fastapi-agent` | HTTP API around an agent | FastAPI + agents |
| **09** | `09-durable-agent` | Checkpoint / resume job | durable execution |
| **10** | `10-studyforge-full` | Capstone portfolio agent | everything together |

`studyforge/` (older scaffold) can merge into **10** later.

## How each project works

1. `README.md` — goal + how to run  
2. `app/` — code  
3. `tests/` — small checks  
4. You run demos → teacher asks 1–2 questions → next project  

## Machine (16GB RAM)

- Projects **01** need only Python  
- From **02** on: `ollama pull tinyllama` (optional but recommended)

## Progress

- [x] 01-hello-agent
- [ ] 02-llm-tool-agent
- [ ] 03-notes-rag-agent
- [ ] 04–10 …
