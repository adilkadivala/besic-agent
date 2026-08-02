# StudyForge

**Side-by-side project** while learning AI: a **tiny/local LLM + agentic** study assistant.

- **Tools:** `calculator`, `search_notes` (searches your `notes/` folder)
- **Agent loop:** thought → tool → result → final answer
- **LLM:** Ollama small model when available, else **mock** mode (works offline)

## Your laptop (16GB RAM)

Good models for 16GB:

| Model | Command | Notes |
|-------|---------|--------|
| **tinyllama** (recommended start) | `ollama pull tinyllama` | Small & fast |
| qwen2.5:0.5b | `ollama pull qwen2.5:0.5b` | Very small |
| phi3:mini | `ollama pull phi3:mini` | Smarter, heavier |

Avoid 7B+ models if you want headroom for browser + IDE.

## Setup

```bash
cd ai-playground/studyforge
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Optional: real small LLM

```bash
# terminal 1
ollama serve

# terminal 2
ollama pull tinyllama
```

## Run

```bash
cd ai-playground/studyforge
source .venv/bin/activate   # if you created venv

# Mock or Ollama auto-detect
python -m app.main

# One-shot
python -m app.main -q "What is 17 * 24?"
python -m app.main -q "Search notes for ReLU"

# Force modes
python -m app.main --mode mock
python -m app.main --mode ollama --model tinyllama
```

## Tests

```bash
python tests/test_tools.py
```

## Side-by-side learning plan

| Learn (theory) | Build (StudyForge) |
|----------------|--------------------|
| Neuron, loss, GD | Keep `tiny_train_loop.py` |
| Tools & agents | This repo — agent loop |
| RAG | Add PDF/notes retrieval v2 |
| FastAPI | Wrap `run_agent` in API |
| Tiny LM from scratch | `scripts/train_tiny_lm.py` later |

## Project status

- [x] P0: scaffold + calculator + search_notes + agent loop + mock LLM
- [ ] P1: polished Ollama tool-calling prompts
- [ ] P2: real RAG embeddings
- [ ] P3: FastAPI
- [ ] P4: from-scratch tiny LM script
