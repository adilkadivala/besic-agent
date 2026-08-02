# Article: I built my first agent — without an LLM

**Scope:** Agents phase after DL complete (project 01 + StudyForge P0)  
**Publish:** X Article or long post  
**Length:** ~750–900 words  

**Title options:**
1. I built my first agent without an LLM (on purpose)  
2. THINK → ACT → OBSERVE: the loop before frameworks  
3. From DL capstone to hello-agent in plain English  

**Linking post:**
```
Deep learning: done.
Agents: started.

Project 01 has tools + a loop.
No LLM yet — on purpose.

Notes below.
```

---

## BODY

---

# I built my first agent — without an LLM

I finished a compressed deep learning core (~93% capstone).

Next phase was supposed to be “agents.”

Most timelines online start with:

- pick a framework  
- spin three agents  
- call it orchestration  

I did the opposite.

**Project 01: Hello Agent** — a real agentic loop, real tools, **no LLM**.

On purpose.

---

## Why no model first?

Because the hard idea isn’t “call GPT.”

The hard idea is the **loop**:

```text
THINK   → decide tool or final answer
ACT     → call tool
OBSERVE → read result
(repeat)
FINAL   → answer the user
```

That’s the same shape as **ReAct**-style agents (Reason + Act).

If THINK is a keyword router today and an LLM tomorrow, the skeleton stays.

I wanted the skeleton in my own code before frameworks hide it.

---

## What I shipped

Folder: `agentic-projects/01-hello-agent`

| Piece | What it is |
|--------|------------|
| **Tools** | `calculator`, `get_time`, `echo` — plain functions → string results |
| **Router (THINK)** | keyword rules (math / time / echo) |
| **Loop** | think → act → observe, up to `max_steps` |
| **CLI** | ask a question, watch steps print |
| **Tests** | tiny checks on tools |

Example:

- User: `What is 17 * 24?`  
- THINK → calculator  
- ACT → run expression  
- OBSERVE → `408`  
- FINAL → `The answer is 408`

No API key. No cloud. Just Python.

---

## Concepts that finally felt real

### 1) Tool
A **tool** is a function with clear input/output the agent is allowed to use.

Not “magic skills.” Functions with a registry.

### 2) Agent loop
Not a chatbot. A process that can **act**, then **look**, then **decide again**.

### 3) Max steps
Without a limit, a buggy agent calls tools forever.

Reliability starts with a **stop condition** — long before multi-agent drama.

### 4) Router vs brain
Today THINK is rules.  
**Project 02** replaces THINK with a **small local LLM (Ollama / tinyllama)** on the **same loop**.

That’s how I’m learning: change one layer at a time.

---

## Chatbot vs agent (from code)

| | Chatbot | Agent (project 01) |
|--|---------|---------------------|
| Job | Answer in text | Reach a goal with steps |
| Tools | optional / none | required for real work |
| Loop | usually one shot | think–act–observe |

I already “knew” this from Day 1 vocabulary.  
Shipping it removed the fog.

---

## StudyForge (side project)

In parallel I have **StudyForge** — a study assistant agent aimed at **my notes**.

Current P0:

- agent loop  
- tools: `calculator`, `search_notes`  
- mock LLM offline; Ollama when available  
- 16GB-friendly models only (`tinyllama`, not 7B+ while coding)

Later: better tool-calling prompts, real RAG, FastAPI, portfolio merge.

The point of StudyForge isn’t “another chatbot.”  
It’s **an agent that can use my learning notes as a tool**.

---

## Roadmap (learn by building)

| # | Build | Learn |
|---|--------|--------|
| 01 | Hello loop + tools | tools, observe, max steps ✅ |
| 02 | + Ollama | LLM tool calling |
| 03 | Notes RAG agent | retrieval |
| 04 | Web research | multi-tool routing |
| 05 | Planner | plan → execute |
| 06 | Multi-agent | roles / handoff |
| 07 | Memory | short + long |
| 08 | FastAPI agent | ship over HTTP |
| 09 | Durable agent | checkpoint / resume |
| 10 | StudyForge full | portfolio capstone |

Method: **one folder = one project.**  
Build → learn from code → short Q&A → next folder.

PDFs (`agentic-ai`, `loopengineering`, MCP, etc.) come **after** the skeleton exists so the words attach to something real.

---

## What I refuse to do (for now)

- Start at multi-agent crew demos  
- Wrap a heavy framework before I can write the loop  
- Pretend mock agents are production systems  
- Run huge local models on 16GB while IDE + browser are open  

Order is part of the skill.

---

## Status

- ✅ Deep learning compressed core  
- ✅ `01-hello-agent`  
- ✅ StudyForge P0 scaffold  
- ➡️ Next: `02-llm-tool-agent` (same loop, LLM THINK)

If you’re learning agents too: write THINK / ACT / OBSERVE yourself once.

Then the frameworks will make sense — instead of feeling like magic.

Follow for the Ollama episode when 02 ships.  
Reply **loop** if you want a single-diagram version of the four steps.

---

## Captions

### A
```
First agent: shipped.
LLM: not required (yet).

THINK → ACT → OBSERVE → FINAL

Build log in the article.
```

### B
```
I learned agents by removing the model first.

Tools + loop + max_steps.

Then I'll add Ollama.
```

### C
```
DL done.
Hello-agent done.
StudyForge scaffolded.

Next: LLM tool calling on the same loop.
```

---

*Source: `agentic-projects/01-hello-agent/*`, `agentic-projects/README.md`, `studyforge/README.md`, `notes/side-by-side-plan.md`*
