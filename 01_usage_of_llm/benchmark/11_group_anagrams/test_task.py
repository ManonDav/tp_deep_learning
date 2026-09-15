import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import group_anagrams


def normalize(groups):
    return sorted([sorted(g) for g in groups])


def test_basic():
    result = normalize(group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
    expected = normalize([["eat", "tea", "ate"], ["tan", "nat"], ["bat"]])
    assert result == expected


def test_empty():
    assert group_anagrams([]) == []


def test_single_word():
    assert normalize(group_anagrams(["abc"])) == normalize([["abc"]])


def test_case_insensitive():
    result = normalize(group_anagrams(["Tea", "ate", "EAT"]))
    expected = normalize([["Tea", "ate", "EAT"]])
    assert result == expected


def test_distinct_words():
    assert normalize(group_anagrams(["cat", "dog"])) == normalize([["cat"], ["dog"]])
