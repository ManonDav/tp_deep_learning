import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import is_palindrome


def test_sentence_with_punctuation():
    assert is_palindrome("Was it a car or a cat I saw?") is True


def test_sentence_with_commas_and_colon():
    assert is_palindrome("A man, a plan, a canal: Panama") is True


def test_not_palindrome():
    assert is_palindrome("Hello") is False


def test_empty_string():
    assert is_palindrome("") is True


def test_only_spaces():
    assert is_palindrome("   ") is True


def test_numeric_palindrome():
    assert is_palindrome("12321") is True


def test_numeric_not_palindrome():
    assert is_palindrome("12345") is False


def test_mixed_case_single_word():
    assert is_palindrome("Racecar") is True
