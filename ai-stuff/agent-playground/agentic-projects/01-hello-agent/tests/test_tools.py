import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app.tools import calculator, echo, get_time
from app.agent import run_agent


def test_calculator():
    assert calculator("17 * 24") == "408"
    assert calculator("10 + 5") == "15"


def test_echo():
    assert "hello" in echo("hello")


def test_get_time():
    t = get_time()
    assert len(t) >= 10


def test_agent_math():
    r = run_agent("What is 17 * 24?", verbose=False)
    assert "408" in r.answer


def test_agent_time():
    r = run_agent("What time is it?", verbose=False)
    assert r.answer.startswith("Result:") or "-" in r.answer


if __name__ == "__main__":
    test_calculator()
    test_echo()
    test_get_time()
    test_agent_math()
    test_agent_time()
    print("All tests passed.")
