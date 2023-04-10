"""Exercise 07--Dictionary."""
__author__ = "730465167"


def invert(input: dict[str, str]) -> dict[str, str]:
    """Docstring."""
    inv_dict: dict[str, str] = {}

    for key in input:
        if input[key] in inv_dict:
            raise KeyError("Error: Duplicate Keys")
        inv_dict[input[key]] = key
    return inv_dict


def favorite_color(color_dict: dict[str, str]) -> str:
    """Docstring."""
    counter: int = 0
    favorite_color: str = ""
    color_count = {}
    for key in color_dict:
        color = color_dict[key]
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1

    for key in color_count:
        if color_count[key] > counter:
            counter = color_count[key]
            favorite_color = key
    return favorite_color


print(favorite_color({"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}))


def count(the_list: list[str]) -> dict[str, int]:
    """Docstring."""
    the_dict: dict[str, int] = {}
    for idx in the_list:
        if idx in the_dict:
            the_dict[idx] += 1
        else:
            the_dict[idx] = 1
    return the_dict
