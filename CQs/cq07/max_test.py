"""Creating the unit test to test the function created"""

__author__ = "730758554"
from find_max import find_and_remove_max


def test_find_and_remove_max() -> None:
    assert find_and_remove_max(my_list=[-1, -4, -10]) == -1
    # edge case if the list has negative numbers


def test_find_max() -> None:
    assert find_and_remove_max(my_list=[1, 2, 3, 4]) == 4
    # use case to return the expected max


def test_remove_max() -> None:
    my_list: list[int] = [3, 4, 4, 4]
    find_and_remove_max([3, 4, 4, 4])
    assert my_list == [3]
    # use case to see the correct mutation of the list
