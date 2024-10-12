"""Exercise 04: modifications/for loops with lists"""

__author__ = "730758554"


def all(my_list: list[int], specific_number) -> bool:
    """To determine whether every number in the list is equal to a specific number"""
    if my_list == []:
        # if the list is empty
        return False
    else:
        for number in range(0, len(my_list)):
            if my_list[number] != specific_number:
                # if the number doesn't equal the specific number
                return False
                quit()
            else:
                return True
    return True


def max(input: list[int]) -> int:
    """To determine the max in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
        # if the list is empty
    x: int = input[0]
    for number in range(0, len(input)):
        if input[number] > x:
            # if the number is greater, make the number x, would repeat until finds
            # the max by going through the whole list
            x = input[number]
    return x


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """To determine whether at every index the lists are the same"""
    if first_list == [] and second_list == []:
        # if both lists are empty
        return True
    elif len(first_list) == len(second_list):
        for number in range(0, len(first_list)):
            if first_list[number] != second_list[number]:
                # if some number for the first list doesn't equal the number at the
                # same index for the second list
                return False
                quit()
        return True
    else:
        return False


def extend(first_list: list[int], list_to_add: list[int]) -> None:
    """To combine the lists by adding the second list to the first"""
    i: int = 0
    while i < len(list_to_add):
        first_list.append(int(list_to_add[i]))
        # use the append feature to add to the end of the list
        i = i + 1
