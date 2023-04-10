"""EX04, list Utility Functions!"""
__author__ = "730465167"


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks to see if every element at every index is true."""
    if (len(list_1) == 0 and len(list_2) != 0):
        return False
    if (len(list_1) != 0 and len(list_2) == 0):
        return False
    count = 0
    length_1 = len(list_1)
    while (len(list_1) == len(list_2) and len(list_1) > 0 and len(list_2) > 0):
        if list_1.pop() == list_2.pop():
            count += 1
    if (count == length_1):
        return True
    else: 
        return False


def all(list: list[int], number: int) -> bool:
    """Checks if all the numbers in the list match the indicated number."""
    if len(list) == 0:
        return False
    count = 0
    length = len(list)
    while len(list) > 0:
        if list.pop() == number:
            count += 1
    if (count == length):
        return True
    else: 
        return False


def max(list: list[int]) -> int:
    """Checks the list and returns the largest value."""
    if len(list) == 0: 
        raise ValueError("max() arg is an empty List")
    largest = list[0]
    idx = 0
    while idx < len(list):
        if list[idx] > largest:
            largest = list[idx]
        idx += 1
    return largest