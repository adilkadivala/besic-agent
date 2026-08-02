# Thread — First agent (no LLM) + StudyForge start

**Phase:** After DL complete → Agents project 01  

---

### T1
```
DL foundations: done.

I didn't start with multi-agent frameworks.

I shipped 01-hello-agent:
a real agent loop with tools — and no LLM.

Here's what I learned 🧵
```

### T2
```
The loop (tattoo this):

THINK  → pick tool or final answer
ACT    → run the tool
OBSERVE → read the result
repeat
FINAL  → answer the user

Same shape as ReAct-style agents.
```

### T3
```
What is a tool?

A function with clear input/output
the agent is allowed to call.

Mine today:
• calculator
• get_time
• echo
```

### T4
```
Why no LLM in project 01?

So I learn the skeleton first.

THINK is just a keyword router for now.
Project 02 replaces THINK with Ollama.
Same loop. Smarter brain.
```

### T5
```
Why max_steps?

Without a stop condition,
a buggy agent loops forever.

Reliability = exit ramps, not only smart models.
```

### T6
```
Chatbot vs agent (from code, not Twitter):

Chatbot: text in → text out
Agent: goal → tools → observations → final

I can demo it:
"What is 17 * 24?"
→ calculator → observe → "The answer is …"
```

### T7
```
Side project: StudyForge

Study agent that can:
• calculator
• search_notes (my notes/ folder)
• mock LLM offline / Ollama when up

16GB laptop → tinyllama, not 7B while coding.
```

### T8
```
Roadmap I'm building next:

02 LLM tool agent (Ollama)
03 notes RAG agent
04 web research
05 planner
06 multi-agent
07 memory
08 FastAPI
09 durable / checkpoint
10 StudyForge full
```

### T9
```
Method:

One folder = one project.
Build first → learn from code → short Q&A.
PDFs after the skeleton exists.

agentic-ai / loop engineering will hit harder now.
```

### T10
```
Status:

✅ DL compressed core (~93%)
✅ 01-hello-agent
✅ StudyForge P0 scaffold
➡️ 02-llm-tool-agent next

Follow for build logs.
Reply "agents" if you want the Ollama episode when I ship 02.
```
