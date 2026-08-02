# Your AI Learning Roadmap (from your PDFs)

Built for **starting from zero or near-zero**, using only the documents in this folder.

**Goal:** become a practical **AI / Agentic AI Engineer** — not only theory, but systems you can build and explain in interviews.

**Total time:** ~12–16 weeks at ~8–12 hours/week  
**Primary stack you’ll practice:** Python → FastAPI → LLMs/RAG → Agents → production patterns

---

## How to use this roadmap

1. **Open PDFs in order** — Phase → Step → PDF number.
2. **Don’t read every page cover-to-cover.** Skim for concepts, then do the mini-project.
3. **Keep a notes folder:**
   ```bash
   mkdir -p notes ai-playground
   ```
4. **Weekly rhythm:**
   - 40% reading PDFs  
   - 50% building something small  
   - 10% reviewing notes / flashcards  

**Open a PDF (Linux):**
```bash
xdg-open "./learn/deep-learning.pdf"
```

**Extract text to study with an LLM:**
```bash
pdftotext "./learn/deep-learning.pdf" - | head -n 200
```

---

## Duplicates to ignore

These are copies — use the `learn/` versions only:

| Skip | Use instead |
|------|-------------|
| `ai-related/ai-harness-engineering.pdf` | `learn/ai-harness-engineering.pdf` |
| `ai-related/loop-engineering.pdf` | `learn/loopengineering.pdf` |
| `ai-related/Reinforcement-Learning-System-Design-Interview.pdf` | `learn/Reinforcement-Learning-System-Design-Interview.pdf` |
| `in-complete/Reinforcement Learning System Design Interview-1-26.pdf` | full version in `learn/` |

---

# Phase 0 — Orientation (Week 1)

**Goal:** Learn the language of modern AI so the big books don’t feel random.

| Order | Open this PDF | Pages | Why first |
|------:|---------------|------:|-----------|
| **1** | `go through/terms-in-ai-world.pdf` | ~163 | Glossary of production AI terms. Read as a **dictionary**, not a novel. Skim 20–30 terms/day. |
| **2** | `Complete Roadmap to Become an Agentic AI Engineer.pdf` | ~23 | Big-picture map of the field + interview-style Q&A. Sets expectations for the whole journey. |
| **3** | `go through/The AI Engineer Job Market Has Moved Past Prompting.pdf` | ~9 | Why “prompting only” isn’t enough — motivates the deeper path. |

**Mini-project (Week 1):**
- Create `notes/00-glossary.md`
- Write 15 terms in your own words: *LLM, token, embedding, context window, RAG, agent, tool calling, fine-tuning, hallucination, latency, evaluation, vector DB, prompt, system prompt, MCP*
- Install Python tooling:
  ```bash
  python3 -m venv .venv && source .venv/bin/activate
  pip install fastapi uvicorn openai anthropic  # or whatever API you’ll use
  ```

**Checkpoint:** Can you explain RAG vs fine-tuning vs agents in 2–3 sentences each?

---

# Phase 1 — Foundations (Weeks 2–4)

**Goal:** Neural nets, transformers, and serving a model over HTTP.

| Order | Open this PDF | Pages | How to read |
|------:|---------------|------:|-------------|
| **4** | `learn/deep-learning.pdf` | ~249 | **Main textbook.** Do chapters on neurons → training → transformers. Skip super-mathy digressions on first pass. Aim for *intuition + runnable code*, not every proof. |
| **5** | `go through/Transformer Architecture.pdf` | ~25 | Short, focused recap of attention, multi-head, BERT vs GPT. Read **after** the transformer chapter in #4. |
| **6** | `learn/FAST API.pdf` | ~89 | How AI engineers actually ship models as APIs. REST, validation, async, LLM endpoints. |

**Mini-projects:**
1. Train a tiny classifier (MNIST or similar) with PyTorch.
2. Wrap it (or a mock LLM call) in **FastAPI**.
3. Call it from a script or `curl`.

**Checkpoint:** You can train something simple *and* expose it as an HTTP API.

---

# Phase 2 — AI System Design (Weeks 5–7)

**Goal:** Think in systems (data → model → serve → monitor), not only notebooks.

| Order | Open this PDF | Pages | How to read |
|------:|---------------|------:|-------------|
| **7** | `learn/ai-sys-design.pdf` | ~315 | **Core system-design book.** RAG, LLM ops, ML systems, big-tech case studies. Read for *architecture patterns*, not memorizing every case study. |
| **8** | `go through/Here’s the Secret to GenAI System Design Interviews.pdf` | ~21 | Interview framing for GenAI design problems. |
| **9** | `full-pdf/building-testing-and-operatingllm-in-production.pdf` | ~107 | How real LLM apps are tested and run in production. |
| **10** | `full-pdf/Context Window Management.pdf` | ~40 | Context limits, packing, truncation, cost — practical production skill. |

**Optional depth (pick 1 if time allows):**
- `learn/sys-des-nlp.pdf` — NLP system design
- `full-pdf/Designing a Unified Feature Store and Model Serving Platform.pdf`
- `full-pdf/Designing an AI Coding Copilot System_ A System Design Interview Guide.pdf`
- `full-pdf/Designing AI Typing Assistance Systems.pdf`

**Mini-project:**
- Draw a system diagram (draw.io / Excalidraw) for an “AI product”:  
  **User → API → retrieval/model → response → logs/metrics**
- Write a 1-page design doc for a simple app (e.g. “company FAQ chatbot”).

**Checkpoint:** You can sketch an end-to-end AI system and name the failure modes (latency, cost, hallucinations, data freshness).

---

# Phase 3 — RAG (Weeks 8–9)

**Goal:** Build the most common production AI pattern: **Retrieval-Augmented Generation**.

| Order | Open this PDF | Pages | How to read |
|------:|---------------|------:|-------------|
| **11** | `go through/RAG Interview Q&A_ How Retrieval-Augmented Generation Actually Works.pdf` | ~18 | Start here — clean conceptual + interview Q&A. |
| **12** | `learn/multi-tenant-rag-with-sys-architechure.pdf` | ~86 | Production architecture: tenants, vector namespaces, gateways, pipelines. |
| **13** | `learn/RAG Evaluation & Testing in Production (Offline + Online).pdf` | ~93 | How to know if RAG is actually good (metrics, offline/online tests). |
| **14** | `go through/Designing Intelligent Document Processing Pipelines.pdf` | ~13 | Ingestion / document pipelines that feed RAG. |

**Mini-project:**
1. Index a small folder of PDFs/notes into ChromaDB or FAISS.
2. Query → retrieve chunks → send to an LLM → answer with citations.
3. Write 10 test questions and score answer quality.

**Checkpoint:** You can explain chunking, embeddings, retrieval, reranking, and evaluation.

---

# Phase 4 — Agentic AI (Weeks 10–12)

**Goal:** Agents that use tools, keep state, and run longer than a single chat turn.

| Order | Open this PDF | Pages | How to read |
|------:|---------------|------:|-------------|
| **15** | `learn/agentic-ai.pdf` | ~247 | **Main agent book.** Roadmap + interview prep for agentic systems. |
| **16** | `go through/Agent Systems.pdf` | ~25 | Compact systems view of agents. |
| **17** | `go through/Stop Confusing the Stack_ LangChain, LangGraph, Langfuse, LangSmith, & Langflow Explained.pdf` | ~15 | Which tool is for what (orchestration vs observability vs UI). |
| **18** | `learn/loopengineering.pdf` | ~190 | Engineering reliable agent *loops* (plan → act → observe). |
| **19** | `learn/ai-harness-engineering.pdf` | ~214 | Harness / runtime patterns around models (adapters, SDKs, safety). |
| **20** | `learn/mcp-interview.pdf` | ~141 | Model Context Protocol — tools, secure integrations, agent I/O. |
| **21** | `full-pdf/AutoGen, CrewAI & Multi-Agent Orchestration.pdf` | ~23 | Multi-agent frameworks and patterns. |
| **22** | `learn/Multi-Agent-AI-sys-des-interview.pdf` | ~152 | Multi-agent system design for interviews. |
| **23** | `go through/Stateful Workflows in AI Engineering_ The Missing Skill Behind Reliable AI Agents.pdf` | ~23 | Workflows that don’t fall over. |
| **24** | `go through/Long-Running Background Agents and Durable Execution.pdf` | ~24 | Durability, checkpoints, background agents. |

**Optional / advanced agents:**
- `learn/autonomus-ai.pdf` — autonomy depth
- `learn/agentic-voice-ai.pdf` — voice agents
- `go through/RecursiveMAS_ What Happens When AI Agents Stop Talking and Start Sharing Latent Thoughts_.pdf`
- `go through/Anthropic Launches Claude Fable 5 and Mythos 5_ The Next Step Toward Long-Horizon AI Agents.pdf` (trend reading)

**Mini-project:**
1. Build an agent with **tools**: web search or local file read + a calculator (or your FastAPI service).
2. Add a simple loop: *plan → tool call → observe → answer*.
3. Stretch: two agents (researcher + writer) with a shared task list.

**Checkpoint:** You can build a tool-using agent and explain tool calling, memory, and failure recovery.

---

# Phase 5 — Fine-tuning, RL & specialization (Weeks 13–14)

**Goal:** When RAG/agents aren’t enough — adapt models and reason about learning loops.

| Order | Open this PDF | Pages | How to read |
|------:|---------------|------:|-------------|
| **25** | `go through/Fine-Tuning & PEFT LoRA, QLoRA, RLHF, DPO, ORPO, Adapter Layers.pdf` | ~20 | Modern fine-tuning + preference tuning overview. |
| **26** | `go through/Reinforcement Learning for Agents.pdf` | ~27 | RL concepts applied to agents. |
| **27** | `learn/Reinforcement-Learning-System-Design-Interview.pdf` | ~142 | Full RL system design for interviews. |
| **28** | `in-complete/Memory.pdf` | ~30 | Agent/memory architectures (draft — still useful). |

**Optional specialization:**
- `learn/Production-Recommendation.pdf` — recommendation systems
- `go through/Cosmos 3_ NVIDIA’s Omnimodal World Model for Physical AI.pdf` — physical / multimodal AI (curiosity read)

**Mini-project (pick one):**
- Fine-tune a small open model with LoRA on a tiny dataset **or**
- Run a simple RL env (CartPole) and log rewards **or**
- Design (on paper) a memory layer for your agent (short-term chat + long-term vector store).

**Checkpoint:** You know *when* to use RAG vs fine-tune vs RLHF/DPO-style training.

---

# Phase 6 — Interview & career polish (Weeks 15–16+)

**Goal:** Package what you learned for jobs and interviews.

| Order | Open this PDF | Pages | How to use |
|------:|---------------|------:|------------|
| **29** | `full-pdf/Machine-Learning-Pocket-Notes-Interview.pdf` | ~54 | Quick ML interview refresh. |
| **30** | `full-pdf/100 Top AI Engineer Interview Questions Based on Real Big Tech Patterns .pdf` | ~8 | Drill coding + AI screen patterns. |
| **31** | `go through/Forward Deployed Engineer (FDE) Mock Interview Q&A.pdf` | ~14 | Customer-facing AI engineer interviews. |
| **32** | Revisit: `Complete Roadmap to Become an Agentic AI Engineer.pdf` | ~23 | Full-circle self-assessment against the original roadmap. |

**Also useful:**
- `X_Monetization_Content_Plan.md` — only if you want to *create content* about what you’re learning (optional, not core engineering).

**Portfolio checklist (aim for 3 demos):**
1. **API:** FastAPI service wrapping a model or LLM call  
2. **RAG app:** docs in → answers with sources  
3. **Agent:** multi-step tool use with basic persistence  

Deploy one of them (Railway / Fly.io / Render free tier) + write a README that shows system design diagrams.

---

## Master reading order (print this)

```
1.  terms-in-ai-world.pdf
2.  Complete Roadmap to Become an Agentic AI Engineer.pdf
3.  The AI Engineer Job Market Has Moved Past Prompting.pdf
4.  deep-learning.pdf
5.  Transformer Architecture.pdf
6.  FAST API.pdf
7.  ai-sys-design.pdf
8.  Here’s the Secret to GenAI System Design Interviews.pdf
9.  building-testing-and-operatingllm-in-production.pdf
10. Context Window Management.pdf
11. RAG Interview Q&A...
12. multi-tenant-rag-with-sys-architechure.pdf
13. RAG Evaluation & Testing in Production...
14. Designing Intelligent Document Processing Pipelines.pdf
15. agentic-ai.pdf
16. Agent Systems.pdf
17. LangChain / LangGraph / Langfuse stack PDF
18. loopengineering.pdf
19. ai-harness-engineering.pdf
20. mcp-interview.pdf
21. AutoGen, CrewAI & Multi-Agent Orchestration.pdf
22. Multi-Agent-AI-sys-des-interview.pdf
23. Stateful Workflows...
24. Long-Running Background Agents...
25. Fine-Tuning & PEFT...
26. Reinforcement Learning for Agents.pdf
27. Reinforcement-Learning-System-Design-Interview.pdf
28. Memory.pdf
29. Machine-Learning-Pocket-Notes-Interview.pdf
30. 100 Top AI Engineer Interview Questions...
31. FDE Mock Interview Q&A.pdf
32. Revisit Complete Roadmap...
```

---

## What to open **today** (Day 1)

| Step | Action |
|------|--------|
| 1 | Open `go through/terms-in-ai-world.pdf` — pick 15 terms, write them in `notes/00-glossary.md` |
| 2 | Skim `Complete Roadmap to Become an Agentic AI Engineer.pdf` (23 pages — doable in one sitting) |
| 3 | Create folders: `notes/` and `ai-playground/` |
| 4 | Tomorrow: start `learn/deep-learning.pdf` Chapter 1 + a tiny Python neural-net tutorial |

---

## Suggested tool stack (for projects)

| Need | Tool |
|------|------|
| Language | Python 3.11+ |
| Deep learning | PyTorch |
| APIs | FastAPI + Uvicorn |
| Vectors / RAG | ChromaDB or FAISS |
| Agents | Start simple (raw tool loop); then LangGraph / CrewAI |
| LLM APIs | OpenAI / Anthropic / local Ollama |
| Notes | Markdown in `notes/` |

Example starter `ai-playground/requirements.txt`:
```text
torch
fastapi
uvicorn[standard]
chromadb
httpx
pydantic
```

---

## Progress tracker

Copy into `notes/progress.md` and check off as you go:

```markdown
## Phase 0
- [ ] terms glossary (15+ terms)
- [ ] agentic roadmap overview
- [ ] job market short read

## Phase 1
- [ ] deep-learning (core chapters)
- [ ] transformers recap
- [ ] FastAPI service demo

## Phase 2
- [ ] ai-sys-design core chapters
- [ ] production LLM ops notes
- [ ] 1 system design diagram + design doc

## Phase 3
- [ ] RAG concepts
- [ ] multi-tenant RAG architecture
- [ ] RAG evaluation
- [ ] working RAG demo

## Phase 4
- [ ] agentic-ai core
- [ ] loops + harness
- [ ] MCP basics
- [ ] multi-agent overview
- [ ] tool-using agent demo

## Phase 5
- [ ] fine-tuning overview
- [ ] RL for agents / system design
- [ ] one specialization experiment

## Phase 6
- [ ] interview question drills
- [ ] portfolio of 3 demos
```

---

## Study rules that actually work

1. **Build after every phase** — unread theory fades; a small demo sticks.
2. **Explain out loud** — if you can’t teach RAG to a friend, re-read Phase 3.
3. **Interview early, lightly** — from Phase 2 onward, answer 2–3 questions/week from the interview PDFs.
4. **Don’t start with multi-agent frameworks** — master single-agent + tools first.
5. **Skip optional PDFs** until the core path is done; your stack is already large enough.

---

## When you’re stuck

Ask me things like:
- “Summarize the first 50 pages of `deep-learning.pdf`”
- “Quiz me on RAG from my notes”
- “Help me design the Week 8 RAG mini-project”
- “I’m on Phase 4 — what should I build this weekend?”

---

*Start with Phase 0 today. Open PDF #1 (`terms-in-ai-world.pdf`). You’ve got a clear path.*
