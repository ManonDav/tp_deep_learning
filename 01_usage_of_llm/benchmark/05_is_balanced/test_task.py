import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import is_balanced


def test_simple_parentheses():
    assert is_balanced("()") is True


def test_all_bracket_types():
    assert is_balanced("()[]{}") is True


def test_nested():
    assert is_balanced("({[]})") is True


def test_wrong_closing():
    assert is_balanced("(]") is False


def test_interleaved():
    assert is_balanced("([)]") is False


def test_unbalanced_count():
    assert is_balanced("((())") is False


def test_empty():
    assert is_balanced("") is True


def test_no_delimiters():
    assert is_balanced("abc") is True


def test_unclosed():
    assert is_balanced("(") is False


def test_extra_closing():
    assert is_balanced("())") is False
