"""Test for Exercise 07--Dictionary."""
__author__ = "730465167"

from exercises.ex07.dictionary import invert
from exercises.ex07.dictionary import favorite_color
from exercises.ex07.dictionary import count


def test_invert_empty() -> None:
    """Test's that passing an empty dictionary returns an empty dictionary."""
    test_dict: dict[str, str] = {}
    assert invert(test_dict) == {}


def test_invert_normal() -> None:
    """Test's that under normal circumstances, a dictionary w/ unique values should return a dictionary with inverted keys and values."""
    test_dict: dict[str, str] = {'a': '1', 'b': '2', 'c': '3'} 
    assert invert(test_dict) == {'1': 'a', '2': 'b', '3': 'c'}


def test_invert_single_pair() -> None:
    """Test's that invert works with only one key-value pair."""
    test_dict: dict[str, str] = {'a': '1'}
    assert invert(test_dict) == {'1': 'a'}


def test_favorite_color_empty() -> None:
    """Test's that passing an empty dictionary should return empty string."""
    test_dict: dict[str, str] = {}
    assert favorite_color(test_dict) == ""


def test_favorite_color_normal() -> None:
    """Test's that under normal circumstances, a dictionary w/ unique values should return a dictionary with inverted keys and values."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue", "Luke": "green"}
    assert favorite_color(test_dict) == "blue"


def test_favorite_color_first_color() -> None:
    """Test's that when there are the same amount of multiple different colors, it returns the first."""
    test_dict: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "green"}
    assert favorite_color(test_dict) == "yellow"


def test_count_empty() -> None:
    """Test's that passing an empty list should return an empty dictionary."""
    test_list: list[str] = {}
    assert count(test_list) == {}


def test_count_normal() -> None:
    """Test's that under normal circumstances, returns a dict with approporaite values and keys."""
    test_list: list[str] = ['a', 'b', 'c', 'e', 'e', 'e']
    assert count(test_list) == {'a': 1, 'b': 1, 'c': 1, 'e': 3}


def test_count_onevalue() -> None:
    """Test's that with one value, it returns one value."""
    test_list: list[str] = {"a"}
    assert count(test_list) == {"a": 1}