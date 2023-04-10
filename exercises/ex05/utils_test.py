"""Unit Test."""
__author__ = "730465167"

from exercises.ex05.utils import only_evens, sub, concat


def test_only_evens_edge_case():
    """Unit test for only_even function that tests if no even it returns empty list."""
    assert only_evens([1, 3, 5]) == []


def test_only_evens_use_case_1():
    """Unit test for the only_evens function for one even number if one even number in list."""
    assert only_evens([1, 3, 4]) == [4]


def test_only_evens_use_case_2():
    """Unit test for the only_evens fuction that returns all even if all even list."""
    assert only_evens([2, 4, 6]) == [2, 4, 6]


def test_concat_edge_case():
    """Unit test for concat function that tests if two lists are concatenated together."""
    assert concat([1, 2, 3], [4, 5, 6]) == [1, 2, 3, 4, 5, 6]


def test_concat_use_case_1():
    """Unit test for concat function that tests that two empty lists return an empty list."""
    assert concat([], []) == []


def test_concat_use_case_2():
    """Unit test for concat function that tests that one empty list and one filled list returns filled list."""
    assert concat([], [1, 2, 3]) == [1, 2, 3]


def test_sub_edge_case():
    """Unit test for sub function that tests that an empty list returns an empty list."""
    assert sub([], 0, 10) == []


def test_sub_use_case_1():
    """Test that when start_idx is less than 0, start idx begins at 0."""
    assert sub([1, 2, 3, 4, 5, 6], -1, 3) == [1, 2, 3]


def test_sub_use_case_2():
    """Tests that correct range returns valid result."""
    assert sub([1, 2, 3, 4, 5, 6], 0, 3) == [1, 2, 3]