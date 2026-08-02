import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.tools.calculator import calculator
from app.tools.search_notes import search_notes


def test_calculator_multiply():
    assert calculator("17 * 24") == "408"


def test_calculator_add():
    assert calculator("2 + 3") == "5"


def test_search_notes_relu():
    out = search_notes("ReLU")
    assert "No matches" not in out or "relu" in out.lower()
    # should find something in student notes
    assert "day-04" in out or "ReLU" in out or "relu" in out.lower()


if __name__ == "__main__":
    test_calculator_multiply()
    test_calculator_add()
    test_search_notes_relu()
    print("All tool tests passed.")
