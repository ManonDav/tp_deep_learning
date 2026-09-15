import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import roman_to_int


def test_repeated():
    assert roman_to_int("III") == 3


def test_subtractive_four():
    assert roman_to_int("IV") == 4


def test_subtractive_nine():
    assert roman_to_int("IX") == 9


def test_composed():
    assert roman_to_int("LVIII") == 58


def test_classic_1994():
    assert roman_to_int("MCMXCIV") == 1994


def test_single_char():
    assert roman_to_int("M") == 1000


def test_subtractive_hundreds():
    assert roman_to_int("CD") == 400


def test_subtractive_tens():
    assert roman_to_int("XC") == 90
