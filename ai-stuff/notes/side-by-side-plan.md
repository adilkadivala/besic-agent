# Side-by-side plan: Learn + StudyForge

**Machine:** 16GB RAM → use `tinyllama` / `qwen2.5:0.5b` (not big 7B+ while coding).  
**Project:** `ai-playground/studyforge/`

## Weekly rhythm

| Day | Theory (class) | Build (project) |
|-----|----------------|-----------------|
| 1 | New PDF/chapter concepts | Wire concept into StudyForge or notes search |
| 2 | Q&A / quiz | Improve agent or tools |
| 3 | Light review | Demo script + README update |

## 16GB tips

```bash
ollama serve
ollama pull tinyllama          # start here
# later if smooth:
# ollama pull qwen2.5:0.5b
```

Close heavy apps when running a model + browser + IDE.

## Progress

- [x] P0 StudyForge scaffold + mock agent
- [ ] Ollama live with tinyllama
- [ ] Better prompts for tool JSON
- [ ] RAG v2
- [ ] FastAPI
- [ ] Tiny LM from scratch
