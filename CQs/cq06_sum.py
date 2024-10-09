"""Summing the elements of a list using different loops"""
__author__ = "730758554"
def w_sum(vals: list[float])-> float:
    i: int = 0
    sum: float = 0
    while i< len(vals):
        sum = sum + vals[i]
        i = i + 1
    return sum

