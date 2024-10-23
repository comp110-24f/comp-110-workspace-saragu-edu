"""Practice writing unit tests for functions"""

__author__ = "7307585554"
from exercises.ex05.utils import only_evens, sub, add_at_index
import pytest


def test_only_evens_use_case_1() -> None:
    assert only_evens([1, 4, 10]) == [4, 10]


def test_only_evens_use_case_2() -> None:
    assert only_evens([1, 10, 90]) == [10, 90]


def test_only_evens_edge_case() -> None:
    assert only_evens([-10, 0, 10]) == [-10, 0, 10]


def test_sub_use_case_1() -> None:
    assert sub([1, 2, 3, 4], 0, 2) == [1, 2]


def test_sub_use_case_2() -> None:
    assert sub([0, 1, 2, 3, 4], 0, 3) == [0, 1, 2]


def test_sub_edge_case() -> None:
    assert sub([-10, 0, -10], -10, 10) == [-10, 0, -10]


def test_add_at_index_use_case_1() -> None:
    my_list: list[int] = [10, 20, 30]
    add_at_index(my_list, 40, 3)
    assert my_list == [10, 20, 30, 40]


def test_add_at_index_use_case_2() -> None:
    my_list: list[int] = [39, 40, 41, 42]
    add_at_index(my_list, 43, 4)
    assert my_list == [39, 40, 41, 42, 43]


def test_add_at_index_edge_case() -> None:
    with pytest.raises(IndexError):
        add_at_index([1, 2, 3, 4], 10, 90)
