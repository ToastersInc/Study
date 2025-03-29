#!/usr/bin/env python3

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest
# integer, how much fuel is in the tank.
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again.
# (It is not necessary for Y to be 4.)
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def get_valid_fraction():
    """Prompts the user for a fraction and returns it as a tuple (x, y)
    or None if the input is invalid after several attempts."""
    while True:
        try:
            user_input = input("Fraction: ")
            numerator, denominator = user_input.split('/')
            x = int(numerator)  # Ensure integers
            y = int(denominator)
            if x > y:
                raise ValueError("x cannot be greater than y")
            if y == 0:
                raise ZeroDivisionError("y cannot be zero")
            return x, y
        except ValueError as e:
            print(e)  # Print the specific error message
        except ZeroDivisionError as e:
            print(e)
        except Exception:
            print("Invalid input. Please use the format integer/integer.")


def main():
    # ask user for a fraction
    while True:
        fraction = get_valid_fraction()
        if fraction:
            x, y = fraction
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break


if __name__ == "__main__":
    main()
