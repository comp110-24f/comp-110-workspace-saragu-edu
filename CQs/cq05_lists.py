"""Mutating functions."""

__author__ = "730758554"


def manual_append(the_list: list[int], p2: int) -> None:
    """To add to the end of the list"""
    a: list[int] = the_list
    the_list.append(p2)


def double(the_list: list[int]) -> None:
    """To double every item in the list"""
    i: int = 0
    a: list[int] = the_list
    while i < len(the_list):
        # doubles every item by going through i
        a[i] = 2 * a[i]
        i = i + 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1
# makes the lists linked
double(list_2)
print(list_1)
print(list_2)
