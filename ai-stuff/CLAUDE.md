# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

The *ai‑stuff* repository is a curated collection of learning resources for artificial intelligence.  It does **not** contain source code, build scripts, tests, or any executable artifacts.  All content is stored as PDF documents, grouped by topic.

## Directory Layout

| Directory | Description |
|-----------|-------------|
| `learn/` | Core learning PDFs covering agentic AI, system design, RAG, reinforcement‑learning, and related interview material. |
| `full-pdf/` | Larger, more comprehensive PDFs – interview question sets, system‑design guides, and deep‑dive papers on AI engineering. |
| `go through/` | Supplemental PDFs that dive into niche topics such as multi‑agent orchestration, context‑window management, and AI‑agent durability. |
| `in‑complete/` | Draft or partially‑complete PDFs (e.g., notes on memory architectures and RL system‑design interview prep). |

No other source files (e.g., `.py`, `.js`, `.sh`, `.md`) are present in the repository.

## Common Commands (PDF‑focused workflow)

Because the repo is documentation‑only, typical development commands (build, lint, test) are **not applicable**.  The useful commands revolve around viewing, searching, and extracting text from PDFs:

- **Open a PDF (Linux/macOS)**
  ```bash
  xdg-open ./learn/ai-harness-engineering.pdf   # Linux (uses default PDF viewer)
  # or on macOS:
  open ./learn/ai-harness-engineering.pdf
  ```
- **Search across PDFs** (requires `pdfgrep`)
  ```bash
  pdfgrep -i "retrieval" ./learn/*.pdf ./full-pdf/*.pdf
  ```
- **Convert a PDF to plain‑text** (requires `poppler-utils` – `pdftotext`)
  ```bash
  pdftotext ./go\ through/Long-Running\ Background\ Agents\ and\ Durable\ Execution.pdf -
  ```
  The dash (`-`) streams the text to stdout, which can be piped into other tools or fed to Claude for summarisation.
- **Batch convert a directory of PDFs to text**
  ```bash
  for f in ./learn/*.pdf; do pdftotext "$f" "${f%.pdf}.txt"; done
  ```

These commands are useful for any downstream automation (e.g., generating summary outlines or feeding content into a language model).

## High‑Level “Architecture”

Since the repository contains no runnable code, the “architecture” consists solely of its **document hierarchy**.  When building a learning plan, treat each top‑level directory as a thematic bucket:

1. **Foundations** – PDFs in `learn/` such as `deep-learning.pdf`, `FAST API.pdf`, and `ai‑sys‑design.pdf` provide baseline concepts and system‑design fundamentals.
2. **Advanced Topics** – PDFs in `go through/` explore cutting‑edge subjects (e.g., multi‑agent orchestration, context‑window management, durable agents).
3. **Interview & Career Prep** – Files under `full-pdf/` and `in‑complete/` contain interview question collections and high‑level design interview guides useful for job‑search preparation.

When a future Claude instance needs to locate information, start by selecting the appropriate bucket, then drill down to the most relevant PDF based on its title.

## Suggested Workflow for Building a Learning Plan

1. **Identify Goals** – Define the learning objectives (e.g., *understand agentic AI*, *build a retrieval‑augmented generation system*, *prepare for system‑design interviews*).
2. **Map PDFs to Goals** – Use the directory layout above to associate each goal with one or more PDFs.
3. **Prioritise** – Order the PDFs from foundational to advanced; start with the `deep‑learning.pdf` and `ai‑sys‑design.pdf` files before tackling the more specialized documents in `go through/`.
4. **Summarise** – Use Claude’s PDF reading capability (`Read` tool) or the `pdftotext` workflow to extract key points, then synthesize a concise study schedule (e.g., weekly topics, hands‑on mini‑projects).
5. **Iterate** – After completing a section, revisit the remaining PDFs, refine the schedule, and add practical coding exercises (e.g., building a small RAG prototype) that complement the theory.

## Presence of Configuration Files

- No `.cursor/` rules, `.github/copilot‑instructions.md`, or project‑specific `README.md` files were found.
- Consequently there are no special linting, CI, or Copilot guidance to document.

---

*End of CLAUDE.md*