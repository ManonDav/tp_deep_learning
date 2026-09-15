import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import int_to_roman


def test_repeated():
    assert int_to_roman(3) == "III"


def test_four():
    assert int_to_roman(4) == "IV"


def test_nine():
    assert int_to_roman(9) == "IX"


def test_composed():
    assert int_to_roman(58) == "LVIII"


def test_classic_1994():
    assert int_to_roman(1994) == "MCMXCIV"


def test_one():
    assert int_to_roman(1) == "I"


def test_40_90():
    assert int_to_roman(40) == "XL"
    assert int_to_roman(90) == "XC"


def test_400_900():
    assert int_to_roman(400) == "CD"
    assert int_to_roman(900) == "CM"


def test_big_value():
    assert int_to_roman(3999) == "MMMCMXCIX"
