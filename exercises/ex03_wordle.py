"""Creating a wordle"""

__author__ = "730758554"


def input_guess(secret_word_len: int) -> str:
    """To take input for guess which must be same length as secret_word"""
    guess: str = str(input(f"Enter a {secret_word_len} character word: "))
    # guess is the input entered by user
    while len(guess) != secret_word_len:
        guess = str(input(f"That wasn't {secret_word_len} chars! Try again: "))
        # guess must have the same length of secret word
    return str(guess)


def contains_char(secret_word: str, char_guess: str) -> bool:
    """To print where the character is found"""
    assert len(char_guess) == 1
    i: int = 0
    while i < len(secret_word):
        if char_guess != secret_word[i]:
            # checking if character is included in secret_word
            # if not go to next character of secret_word
            i = i + 1
        elif char_guess == secret_word[i]:
            return True
            # if character exists then return True
    return False


def emojified(guess: str, secret: str) -> str:
    """Create docstring"""
    assert len(guess) == len(secret)
    x: str = ""
    i: int = 0
    while i < len(secret):
        if guess[i] == secret[i]:
            x = x + "\U0001F7E9"
            # prints green box
            i = i + 1
        elif contains_char(secret, guess[i]):
            x = x + "\U0001F7E8"
            # prints yellow box
            i = i + 1
        else:
            x = x + "\U00002B1C"
            # prints white box
            i = i + 1
    print(x)
    return x
    # prints all the boxes


def main(secret: str) -> None:
    """The entrypoint of the main game loop"""
    turn: int = 1
    # counts the turns
    print(f"=== Turn {turn}/6 ===")
    guess = input_guess(len(secret))
    if guess == secret:
        # if guessed correctly immediately
        emojified(guess, secret)
        print(f"=== Turn {turn}/6 ===")
        print(f"You won in {turn}/6 turns!")
    else:
        while (guess != secret) and (turn < 6):
            emojified(guess, secret)
            turn = turn + 1
            print(f"=== Turn {turn}/6 ===")
            guess = input_guess(len(secret))
            # run emojitified until guess==secret or turn is greater than or equal to 6
            if guess == secret:
                emojified(guess, secret)
                print(f"You won in {turn}/6 turns!")
            elif turn >= 6:
                print("X/6 - Sorry, try again tomorrow!")


if __name__ == "__main__":
    main(secret="codes")
# combines the functions
