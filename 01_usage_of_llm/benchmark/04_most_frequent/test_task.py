import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import most_frequent


def test_single_mode():
    assert most_frequent([1, 3, 1, 2, 3, 1]) == 1


def test_tie_returns_first():
    assert most_frequent([3, 1, 3, 1]) == 3


def test_strings():
    assert most_frequent(["a", "b", "a"]) == "a"


def test_single_element():
    assert most_frequent([7]) == 7


def test_tie_with_more_than_two():
    assert most_frequent([1, 2, 1, 2, 3, 3]) == 1


def test_all_distinct():
    assert most_frequent([5, 2, 8]) == 5
