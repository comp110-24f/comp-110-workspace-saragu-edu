"""For cq04, concatenation file"""

__author__ = "730758554"


def concat(p1: str, p2: str) -> str:
    # To add p1 to p2, connects words with spaces
    return p1 + p2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))
