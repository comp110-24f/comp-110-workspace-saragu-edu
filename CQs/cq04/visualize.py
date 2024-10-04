"""For cq04, visualize file"""

from cq04.concatenation import concat
from cq04.coordinates import get_coords

__author__ = "730758554"
# imports the functions from the other files

x: str = "123"
y: str = "abc"
# creates global variables for x and y


print(concat(x, y))
get_coords(x, y)
