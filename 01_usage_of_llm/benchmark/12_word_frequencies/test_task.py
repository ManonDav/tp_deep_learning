import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import word_frequencies


def test_basic():
    assert word_frequencies("The cat and the dog.") == {"the": 2, "cat": 1, "and": 1, "dog": 1}


def test_punctuation_separators():
    assert word_frequencies("a-b c! a.") == {"a": 2, "b": 1, "c": 1}


def test_empty():
    assert word_frequencies("") == {}


def test_apostrophe_internal():
    assert word_frequencies("l'eau est l'eau") == {"l'eau": 2, "est": 1}


def test_no_words():
    assert word_frequencies("!!! ...") == {}


def test_single_repeated():
    assert word_frequencies("hello hello hello") == {"hello": 3}
