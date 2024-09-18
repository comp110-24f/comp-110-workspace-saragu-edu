"""This is for challenge question 3."""

__author__ = 730758554


def num_instances(phrase: str, search_char: str) -> int:
    count: int = 0
    # count is the number of times the computer finds search_char.
    x: int = 0
    # This moves throughout the phrase
    while x < len(phrase):
        # This means if you have looked through the whole phrase
        if phrase[x] == search_char:
            # if the character is the character you are searching for
            count = count + 1
            # This moves to the next character
            x = x + 1
        else:
            x = x + 1

    return count


# Returns the number of times they found the search_char.
