import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import flatten


def test_empty_list():
    assert flatten([]) == []


def test_flat_list():
    assert flatten([1, 2, 3]) == [1, 2, 3]


def test_deeply_nested():
    assert flatten([1, [2, [3, [4]], 5]]) == [1, 2, 3, 4, 5]


def test_with_empty_nested():
    assert flatten([[1, 2], [], [3]]) == [1, 2, 3]


def test_single_element():
    assert flatten([42]) == [42]


def test_nested_empty_only():
    assert flatten([[], []]) == []


def test_mixed_types():
    assert flatten(["a", ["b", ["c"]]]) == ["a", "b", "c"]


def test_raises_on_non_list():
    try:
        flatten(3)
    except TypeError:
        return
    raise AssertionError("flatten(3) should raise TypeError")
