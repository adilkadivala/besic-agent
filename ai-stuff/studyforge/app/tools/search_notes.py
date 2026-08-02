"""Search student notes markdown files for a keyword."""

from __future__ import annotations

import re
from pathlib import Path

# Default: repo notes/ next to ai-playground/
_DEFAULT_NOTES = Path(__file__).resolve().parents[4] / "notes"


def search_notes(query: str, notes_dir: str | Path | None = None, max_hits: int = 5) -> str:
    """
    Search .md files under notes/ for query (case-insensitive).
    Returns matching snippets with file names.
    """
    query = (query or "").strip()
    if not query:
        return "Error: empty query"

    root = Path(notes_dir) if notes_dir else _DEFAULT_NOTES
    if not root.is_dir():
        return f"Error: notes directory not found: {root}"

    pattern = re.compile(re.escape(query), re.IGNORECASE)
    hits: list[str] = []

    for path in sorted(root.rglob("*.md")):
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except OSError:
            continue
        for i, line in enumerate(text.splitlines(), start=1):
            if pattern.search(line):
                snippet = line.strip()
                if len(snippet) > 160:
                    snippet = snippet[:157] + "..."
                hits.append(f"{path.name}:{i}: {snippet}")
                if len(hits) >= max_hits:
                    return "\n".join(hits)

    if not hits:
        return f"No matches for '{query}' in {root}"
    return "\n".join(hits)
