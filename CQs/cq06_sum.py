"""Summing the elements of a list using different loops"""

__author__ = "730758554"


def w_sum(vals: list[float]) -> float:
    """Creates sum using while loop"""
    i: int = 0
    sum: float = 0.0
    # to return 0.0 set the sum equal to 0.0 at the start
    while i < len(vals):
        sum = sum + vals[i]
        i = i + 1
    return sum


def f_sum(vals: list[float]) -> float:
    """Creates sum using for loop"""
    sum: float = 0.0
    for number in vals:
        sum = sum + number
        # the number gives the output of vals at that index
    return sum


def f_range_sum(vals: list[float]) -> float:
    """Creates sum using range with for loop"""
    sum: float = 0.0
    for number in range(0, len(vals), 1):
        sum = sum + vals[number]
        # because number gives the index of the list
    return sum
