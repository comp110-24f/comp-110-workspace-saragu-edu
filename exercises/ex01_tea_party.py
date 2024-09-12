"""This is for the exercise 1 to calculate the number of tea bags needed."""

__author__ = "730758554"


def main_planner(guests: int) -> None:
    """To connect the tea bags, treats, and costs function"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    # This does not need return statement, since the return value is None.
    # The number must be changed to string to be added to the other strings.


def tea_bags(people: int) -> int:
    """To get the number of people at the party"""
    return people * 2


def treats(people: int) -> int:
    """To get the number of people to find the number of treats required."""
    return int(tea_bags(people=people) * 1.5)


# Because the return value is float,
# the expression (tea_bags(people) * 1.5) must be changed from float to int.


def cost(tea_count: int, treat_count: int) -> float:
    """To calculate the cost of the tea bags and the treats"""
    return tea_count * 0.5 + treat_count * 0.75


# The return value is float,
# so type can be left as calculated.

if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party?")))
    # This is used to ask
    # the person the question "How many guests are attending your tea party?"
