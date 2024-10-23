"""Writing the function to find then remove the max"""

__author__ = "730758554"


def find_and_remove_max(my_list: list[int]) -> int:
    """Function to find the max of the list and remove it"""
    if my_list == []:
        return -1
        quit()
    else:
        i: int = 0
        x: int = 0
        while i < len(my_list):
            # to find the max and set it equal to x
            if my_list[i] > x:
                x = my_list[i]
                i = i + 1
            else:
                i = i + 1
        i = 0
        while i < len(my_list):
            if my_list[i] == x:
                my_list.pop(i)
                # to remove x from the list
            else:
                i = i + 1
        return x
    # to return the max
