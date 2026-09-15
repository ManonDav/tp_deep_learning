import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import merge_intervals


def test_overlapping():
    assert merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]) == [[1, 6], [8, 10], [15, 18]]


def test_adjacent():
    assert merge_intervals([[1, 4], [4, 5]]) == [[1, 5]]


def test_unsorted_input():
    assert merge_intervals([[6, 8], [1, 2], [3, 5]]) == [[1, 2], [3, 5], [6, 8]]


def test_empty():
    assert merge_intervals([]) == []


def test_contained_interval():
    assert merge_intervals([[1, 4], [2, 3]]) == [[1, 4]]


def test_already_merged_sorted():
    assert merge_intervals([[1, 2], [3, 4]]) == [[1, 2], [3, 4]]


def test_single_interval():
    assert merge_intervals([[5, 7]]) == [[5, 7]]
