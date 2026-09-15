import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import longest_common_prefix


def test_common_prefix():
    assert longest_common_prefix(["flower", "flow", "flight"]) == "fl"


def test_no_common():
    assert longest_common_prefix(["dog", "racecar", "car"]) == ""


def test_longer_common():
    assert longest_common_prefix(["interspecies", "interstellar", "interstate"]) == "inters"


def test_empty_string():
    assert longest_common_prefix(["", "b"]) == ""


def test_single_string():
    assert longest_common_prefix(["single"]) == "single"


def test_one_is_prefix_of_other():
    assert longest_common_prefix(["car", "carpet"]) == "car"


def test_case_sensitive():
    assert longest_common_prefix(["Apple", "apple"]) == ""
