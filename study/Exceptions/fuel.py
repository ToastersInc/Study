#!/usr/bin/env python3

# In a file called fuel.py, implement a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, and then outputs, as a percentage rounded to the nearest 
# integer, how much fuel is in the tank. 
# If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
# And if 99% or more remains, output F instead to indicate that the tank is essentially full.

# If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
# (It is not necessary for Y to be 4.) 
# Be sure to catch any exceptions like ValueError or ZeroDivisionError.

def main():
    # ask user for a fraction
    while True:
        try:
            user_input = input("Fraction: ")
            # turn fraction into x and y
            numerator, denominator = user_input.split('/')
            x = float(numerator)
            y = float(denominator)
            if x > y:
                raise ValueError
            if y == 0:
                raise ZeroDivisionError
            percentage = round((x / y) * 100)
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            return
        except ValueError:
            print("fraction format must be integer/integer, and x must not be larger than y.")
            user_input = input("Fraction: ")
        except ZeroDivisionError:
            print("y cannot be zero")
            user_input = input("Fraction: ")

    

    
main()
