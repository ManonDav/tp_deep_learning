import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import two_sum


def test_basic():
    assert sorted(two_sum([2, 7, 11, 15], 9)) == [0, 1]


def test_not_adjacent():
    assert sorted(two_sum([3, 2, 4], 6)) == [1, 2]


def test_duplicate_values():
    assert sorted(two_sum([3, 3], 6)) == [0, 1]


def test_three_elements():
    assert sorted(two_sum([1, 2, 3], 5)) == [1, 2]


def test_negatives():
    assert sorted(two_sum([-1, 0, 1], 0)) == [0, 2]


def test_same_value_middle():
    assert sorted(two_sum([1, 5, 5, 2], 10)) == [1, 2]
