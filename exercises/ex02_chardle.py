"""EX02 - Chardle = A cute step toward Wordle."""

__author__ = "730758554"


def input_word() -> str:
    users_word: str = str(input("Enter a 5-character word:"))
    # This gives the input of the user to the variable users_word.
    if len(users_word) == 5:
        return users_word
    else:
        print("Error: Word must contain 5 characters.")
        exit()
        # This prints the error message but exits the code.
        return "Error: Word must contain 5 characters."


def input_letter() -> str:
    users_letter: str = str(input("Enter a single character."))
    # This takes the input to assign to variable users_letter.
    if len(users_letter) == 1:
        return users_letter
    else:
        print("Error: Character must be a single character")
        exit()
        # This prints the error message but exits the code.
        return "Error: Character must be a single character."


def contains_char(word: str, letter: str) -> None:
    print("Searching for " + letter + " in " + word)
    count: int = 0
    # This counts the number of times letter appears in word.
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1

    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1

    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1

    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1

    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1
    # If statements repeat to search word for letter.
    if count == 0:
        print("No instances of " + letter + " found in " + word)
        # prints result if letter doesn't appear in word.
    elif count == 1:
        print("1 instance of " + letter + " found in " + word)
        # prints result if letter appears only once in word.
    elif count > 1:
        print(str(count) + " instances of " + letter + " found in " + word)
        # prints result if letter appears more than once in word.


def main() -> None:
    # This runs the three functions at once.
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
