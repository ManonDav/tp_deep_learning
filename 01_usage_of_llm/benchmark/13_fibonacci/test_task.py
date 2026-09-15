import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import fibonacci


def test_zero():
    assert fibonacci(0) == 0


def test_one():
    assert fibonacci(1) == 1


def test_two():
    assert fibonacci(2) == 1


def test_ten():
    assert fibonacci(10) == 55


def test_one_hundred():
    assert fibonacci(100) == 354224848179261915075
