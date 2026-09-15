import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import run_length_encode


def test_repeated_groups():
    assert run_length_encode("aaabbbccd") == "3a3b2c1d"


def test_all_isolated_chars():
    assert run_length_encode("abcd") == "1a1b1c1d"


def test_empty_string():
    assert run_length_encode("") == ""


def test_case_sensitive():
    assert run_length_encode("aAaa") == "1a1A2a"


def test_single_char():
    assert run_length_encode("z") == "1z"


def test_long_run():
    assert run_length_encode("aaaaa") == "5a"


def test_mixed_runs_and_isolated():
    assert run_length_encode("aab") == "2a1b"
