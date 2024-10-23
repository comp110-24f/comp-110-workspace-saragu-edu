"""Building list utility functions"""

__author__ = "730758554"


def only_evens(input: list[int]) -> list[int]:
    """Using the input list, return a list with only evens"""
    i: int = 0
    x: list[int] = []
    while i < len(input):
        if input[i] % 2 == 0:
            # Checking if it's even
            x.append(input[i])
            i = i + 1
        else:
            i = i + 1
    return x


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Using the input list, only return a list from the start to end inputs"""
    i: int = 0
    x: list[int] = []
    if start < 0:
        # for example if given starts less than zero
        i = 0
    else:
        i = start
    if end > len(input):
        # for example if given the end greater than the length of the list
        end = len(input)
    while i < end:
        x.append(input[i])
        i = i + 1
    return x


def add_at_index(input: list[int], element: int, index: int) -> None:
    """Using the list input, add the element at the given index"""
    if index < 0:
        raise IndexError("Index is out of bounds for the input list")
    elif index > len(input):
        raise IndexError("Index is out of bounds for the input list")
    else:
        input.append(element)
        i: int = index
        o: int = 0
        new_element: int = 0
        while o < len(input):
            # take the items off the list if they are before the index
            # then but add them to the end of the list
            new_element = input[i]
            input.pop(i)
            input.append(new_element)
            o = o + 1
