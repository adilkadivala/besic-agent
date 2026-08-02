# Day 1 — Orientation (Vocabulary)

**Date:** 2026-07-16  
**PDFs:** `go through/terms-in-ai-world.pdf` · `Complete Roadmap to Become an Agentic AI Engineer.pdf`  
**Teacher:** Grok · **Student:** k-adi  
**Status:** Complete ✓

## Goal
Build a working vocabulary so every later PDF makes sense.

## Q&A log

### Q1 — What is an LLM?
**Student answer:**
LLM is a large-language-model performs on the user query, it takes input from the user, and converts into chunks, and then thinks which token will fit to the next, then send response to the end user

**Teacher feedback:** 7/10 — next-token idea correct; use "tokens" not "chunks"; predict not "think"

---

### Q2 — What is a token?
**Student answer:**
token is a piece of text... cat/set/on/mat example

**Teacher feedback:** 5.5/10 — good example; wrong "why" (tokens are units of computation, not "more meaningful than sentences")

---

### Q3 — What is a prompt?
**Student answer:**
input query by end user; good prompt clarifies intent → clearer answer

**Teacher feedback:** 8/10 — solid; also developers write prompts; spelling "prompt"

---

### Q4 — What is a hallucination?
**Student answer:**
unclear prompt / intent; danger of exposing sensitive data (Taj Hotel docs)

**Teacher feedback:** 4/10 — mixed with data leak; hallucination = inventing false confident facts

---

### Q5 — Chatbot vs agent?
**Student answer:**
Chatbot waits for prompt, text-to-text (also docs/images). Agents take steps, call tools (search, APIs, write files). Chatbot answers; agent takes actions.

**Teacher feedback:** 9/10 — excellent core distinction. Spelling: tools not "tolls". Note: reading docs can still be a chatbot+RAG; "agent" = plan + tools + multi-step actions toward a goal.

---

## My 15 core terms (own words) — Day 1 pack

1. **LLM** — Large Language Model; neural net trained on lots of text; predicts next token; generates replies token by token
2. **Token** — small piece of text (word/subword); model’s unit of input/output; text → token IDs → predict next
3. **Prompt** — text input to the LLM (question + instructions + context); good prompts clarify intent
4. **Hallucination** — model invents false but confident facts (not the same as a privacy leak)
5. **Agent** — AI that can take multi-step actions and use tools to complete a goal (not only chat)
6. **Chatbot** — mostly conversational: text (or multimodal) in → answer out; limited or no tool actions
7. **Tool calling** — agent/API lets the model request external actions (search, APIs, files)
8. **Inference** — running a trained model to generate outputs (using the model, not training it)
9. **Context window** — max tokens the model can see at once (prompt + history + reply budget)
10. **Embedding** — number vector representing meaning of text (used for search/similarity)
11. **RAG** — retrieve relevant docs, then generate answer grounded in them
12. **Fine-tuning** — further train a model on your data so behavior/style/domain improves
13. **System prompt** — developer-set rules/role for the model (separate from the user message)
14. **Latency** — how long the user waits for a response
15. **Evaluation** — measuring if answers/actions are actually good (tests, metrics, human review)

*(Items 8–15 introduced for homework — student should rewrite 8–15 in their own words tomorrow if not solid yet.)*

## End-of-day checkpoint
- [x] Can explain LLM, token, prompt in my own words
- [x] Can explain the difference between a chatbot and an agent (basic)
- [ ] Skimmed the Agentic AI roadmap contents (homework if not done)

## Day 1 scores
| Q | Topic | Score |
|---|--------|------:|
| 1 | LLM | 7/10 |
| 2 | Token | 5.5/10 |
| 3 | Prompt | 8/10 |
| 4 | Hallucination | 4/10 |
| 5 | Agent vs chatbot | 9/10 |
| **Avg** | | **~6.7/10** |
