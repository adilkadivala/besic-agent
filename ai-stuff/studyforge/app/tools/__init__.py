from .calculator import calculator
from .search_notes import search_notes

TOOLS = {
    "calculator": calculator,
    "search_notes": search_notes,
}

__all__ = ["TOOLS", "calculator", "search_notes"]
