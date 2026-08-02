# Viral shorts — Agents phase (after DL complete → today)

**Scope only:** post–Day 9 work  
- `agentic-projects/01-hello-agent` ✅  
- `studyforge/` P0 scaffold ✅  
- roadmap 02–10 planned  
**Not included:** DL Day 1–9 rehash  

Mark `[x]` when live.

---

# Milestone / phase shift

### A1 `[ ]`
```
Deep learning core: done (~93%).

I did not jump to multi-agent cosplay.

I built project 01: a real agent loop
with tools — and no LLM yet on purpose.
```

### A2 `[ ]`
```
Phase 2 rule I'm following:

Build first.
Learn the concept from the code.
Then open the PDF.

Agents by shipping, not by vibes.
```

### A3 `[ ]`
```
Locked order paid off:

1) Deep learning foundations ✓
2) Agents theory + builds ← now
3) StudyForge as the portfolio agent

Foundations first was the right call.
```

---

# Agent loop (core teaching)

### L1 `[ ]`
```
The agent loop in 4 words:

THINK → ACT → OBSERVE → (repeat) → FINAL

Same shape as ReAct.
LLM optional at the start.
```

### L2 `[ ]`
```
I built my first agent with NO LLM.

Keyword router chooses the tool.
Tools do the work.
Loop has a max_steps brake.

That's still an agentic loop.
```

### L3 `[ ]`
```
Chatbot: answer text.
Agent: decide tool → run → observe → maybe again → final.

Project 01 made this concrete in code.
```

### L4 `[ ]`
```
Why max_steps?

Without a limit,
a buggy agent calls tools forever.

Reliability starts with a stop condition.
```

### L5 `[ ]`
```
Tool = a function with clear input/output
the agent is allowed to use.

Calculator. Time. Echo.
Later: search, HTTP, files.
```

### L6 `[ ]`
```
My first tools:

calculator
get_time
echo

Boring on purpose.
Clarity over hype.
```

### L7 `[ ]`
```
THINK without an LLM =

simple rules / keywords.

"what is 17*24" → calculator
"what time" → get_time

Project 02 replaces THINK with a small local model.
```

### L8 `[ ]`
```
Observe is underrated.

Act without reading the tool result
is just fire-and-forget.

The loop only works if OBSERVE feeds the next THINK.
```

---

# Build-in-public (hello-agent)

### B1 `[ ]`
```
Shipped: 01-hello-agent

• agent loop
• calculator + time + echo
• max_steps
• CLI + tiny tests

No API keys. No cloud. Just Python.
```

### B2 `[ ]`
```
Try this mental model:

User goal
→ agent picks a TOOL
→ run tool
→ OBSERVE
→ FINAL answer

I can now explain that from code I wrote.
```

### B3 `[ ]`
```
Demo queries that teach the loop:

"What is 17 * 24?"
"What time is it?"
"Echo hello agent"

Each one forces THINK → ACT → OBSERVE → FINAL.
```

### B4 `[ ]`
```
Router today: keywords.
Router next: Ollama tinyllama.

Same loop.
Smarter THINK step.

That's how I'm learning agents.
```

---

# StudyForge

### S1 `[ ]`
```
Side project while learning:

StudyForge — a tiny study agent
that can use calculator + search my notes/

Mock LLM offline.
Ollama when available.
16GB laptop friendly.
```

### S2 `[ ]`
```
16GB RAM tip for local AI:

Start with tinyllama.
Maybe qwen2.5:0.5b.

Avoid 7B+ if you also want browser + IDE alive.
```

### S3 `[ ]`
```
StudyForge status:

✅ scaffold + agent loop + tools + mock LLM
☐ polished Ollama tool JSON
☐ real RAG embeddings
☐ FastAPI wrap
☐ merge into portfolio capstone
```

### S4 `[ ]`
```
search_notes tool >

fancy empty agent demo.

My agent should read MY study notes.
That's the product wedge for me.
```

---

# Roadmap teaser (02–10)

### R1 `[ ]`
```
Agent projects roadmap (learn by building):

01 hello loop ← done
02 LLM + tools (Ollama)
03 notes RAG agent
04 web research
05 planner / ReAct
06 multi-agent
07 memory
08 FastAPI agent
09 durable / checkpoint
10 StudyForge full
```

### R2 `[ ]`
```
Next build: 02-llm-tool-agent

Same loop as 01.
THINK becomes a small local LLM.

That's the jump from rules to models.
```

### R3 `[ ]`
```
I refuse to start at "multi-agent crew."

Sequence:

loop → tools → LLM tools → RAG → plan → multi-agent

Order is the skill.
```

---

# Contrarian / viral

### V1 `[ ]`
```
Unpopular build order:

Don't wrap LangChain on day 1.

Write THINK / ACT / OBSERVE yourself.
Then you'll know what frameworks hide.
```

### V2 `[ ]`
```
"Agent" without max_steps
is a money printer for your API bill.

Always cap the loop.
```

### V3 `[ ]`
```
You don't need GPT-4 to learn agents.

You need:
1) a tool
2) a loop
3) a stop condition

I proved it in project 01.
```

### V4 `[ ]`
```
Theory PDFs later.
Working loop first.

agentic-ai.pdf will make sense
because I already shipped the skeleton.
```

---

# Engagement

### E1 `[ ]`
```
Did you build your first agent
with or without an LLM?

I started without — on purpose.
```

### E2 `[ ]`
```
Reply "loop" if you want the 4-step
THINK → ACT → OBSERVE → FINAL diagram
as a single image-style post next.
```

### E3 `[ ]`
```
What should project 03 search first?

A) my markdown notes
B) PDFs
C) the web

I'm building a notes RAG agent next-next.
```

### E4 `[ ]`
```
Follow for build logs:

01 hello-agent ✓
02 Ollama tools ← next

Learning agents by folders, not threads only.
```

---

## 5-day schedule

| Day | Posts |
|-----|--------|
| 1 | A1, L1 |
| 2 | L2, B1 |
| 3 | L4, V1 |
| 4 | S1, R1 |
| 5 | **Thread** or **Article 05** + E4 |

Space milestone posts (A1 / B1 / R1) across different days.
