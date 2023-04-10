"""EX05, 'list' Utility Functions!"""
__author__ = "730465167"


def only_evens(the_list: list[int]) -> int:
    """Checks the list and returns the even numbers only."""
    even_number = []
    for number in the_list:
        if number % 2 == 0:
            even_number.append(number)
    return (even_number)


def concat(list_1: list[int], list_2: list[int]) -> list:
    """Combines all of the elements of the first list with all the elements of the second list into a new list."""
    master_list = []
    for number in list_1:
        master_list.append(number)
    for number in list_2:
        master_list.append(number)
    return (master_list)


def sub(a_list: list[int], start_idx: int, end_idx: int) -> list:
    """Given a list, user will input a range that will output only the elements of the list within that range."""
    end_list = []
    if start_idx < 0:
        start_idx = 0 
    if end_idx > len(a_list):
        end_idx = len(a_list)
    if len(a_list) == 0 and start_idx >= len(a_list) and end_idx <= 0: 
        return end_list
    for number in range(start_idx, end_idx):
        end_list.append(a_list[number])
    return end_list