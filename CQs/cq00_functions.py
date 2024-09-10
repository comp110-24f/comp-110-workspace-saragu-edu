"""CQ00 Functions"""

__author__ = "730758554"


def mimic(message: str) -> str:
    """Repeats the input back to you"""
    return message


def main() -> None:
    """Prints the result of mimic"""
    print(mimic(message=input("What is your message?")))
    return


if __name__ == "__main__":
    main()
