"""Prompts the user for a level, n.
    If the user does not input a positive integer, the program should prompt again.
Randomly generates an integer between 1 and n,
    inclusive, using the random module.
Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
    If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
    If the guess is larger than that integer, the program should output Too large! and prompt the user again.
    If the guess is the same as that integer, the program should output Just right! and exit.
"""

import sys
import random


def main():
    """prompt the user for a positive integer"""
    try:
        user_input = int(input("Level: "))
        if user_input < 1:
            raise ValueError
    except ValueError:
        print("integer needs to be positive")
        sys.exit()
    """generate a random number from 1 to user_input"""
    random_number = random.randint(1, user_input)

    """prompt the user to guess the random number"""
    while True:
        try:
            guess = int(input("Guess: "))
            if guess < 1:
                raise ValueError
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too Large!")
            else:
                print("Just right!")
                sys.exit()
        except ValueError:
            print("Guess must be a positive integer")


if __name__ == "__main__":
    main()
