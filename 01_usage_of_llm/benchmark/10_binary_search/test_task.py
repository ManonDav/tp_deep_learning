import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import binary_search


def test_target_present_middle():
    assert binary_search([-5, 0, 3, 7, 9, 11], 7) == 3


def test_target_at_start():
    assert binary_search([1, 2, 3, 4, 5], 1) == 0


def test_target_at_end():
    assert binary_search([1, 2, 3, 4, 5], 5) == 4


def test_target_absent_low():
    assert binary_search([1, 2, 3, 4, 5], 0) == -1


def test_empty_list():
    assert binary_search([], 3) == -1


def test_target_absent_high():
    assert binary_search([1, 2, 3, 4, 5], 6) == -1


def test_single_element_found():
    assert binary_search([9], 9) == 0


def test_single_element_not_found():
    assert binary_search([9], 3) == -1
