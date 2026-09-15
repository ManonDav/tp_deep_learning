import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from solution import parse_csv_line


def test_simple():
    assert parse_csv_line("a,b,c") == ["a", "b", "c"]


def test_quoted_with_comma():
    assert parse_csv_line('a,"b,c",d') == ["a", "b,c", "d"]


def test_escaped_quotes():
    assert parse_csv_line('"hello ""world"""') == ['hello "world"']


def test_numbers_as_strings():
    assert parse_csv_line("1,2,3") == ["1", "2", "3"]


def test_trailing_empty():
    assert parse_csv_line("a,") == ["a", ""]


def test_leading_empty():
    assert parse_csv_line(",b") == ["", "b"]


def test_quoted_empty():
    assert parse_csv_line('""') == [""]


def test_quoted_spaces():
    assert parse_csv_line('"  x  "') == ["  x  "]
