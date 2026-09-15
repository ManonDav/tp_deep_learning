import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import caesar_cipher


def test_basic_shift():
    assert caesar_cipher("abc", 3) == "def"


def test_wraparound():
    assert caesar_cipher("xyz", 3) == "abc"


def test_case_preserved_and_symbols():
    assert caesar_cipher("Hello, World!", 1) == "Ifmmp, Xpsme!"


def test_negative_shift():
    assert caesar_cipher("abc", -1) == "zab"


def test_shift_greater_than_25():
    assert caesar_cipher("abc", 29) == "def"


def test_empty_string():
    assert caesar_cipher("", 5) == ""


def test_digits_untouched():
    assert caesar_cipher("abc123", 1) == "bcd123"


def test_lower_and_upper_wraparound():
    assert caesar_cipher("Zz", 1) == "Aa"
