#   convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
#   gauge expects an int and returns a str that is:
#   "E" if that int is less than or equal to 1,
#   "F" if that int is greater than or equal to 99,
#   and "Z%" otherwise, wherein Z is that same int.

#   def main():
#       # ask user for a fraction
#       while True:
#           try:
#               user_input = input("Fraction: ")
#               # turn fraction into x and y
#               numerator, denominator = user_input.split('/')
#               x = float(numerator)
#               y = float(denominator)
#               if x > y:
#                   raise ValueError
#               if y == 0:
#                   raise ZeroDivisionError
#               percentage = round((x / y) * 100)
#               if percentage <= 1:
#                   print("E")
#               elif percentage >= 99:
#                   print("F")
#               else:
#                   print(f"{percentage}%")
#               return
#           except ValueError:
#               print("fraction format must be integer/integer, and x must not be larger than y.")
#               user_input = input("Fraction: ")
#           except ZeroDivisionError:
#               print("y cannot be zero")
#               user_input = input("Fraction: ")

#   if __name__ == "__main__":    
#       main()




def main():
    while True:
        try:
            user_input = input("Fraction: ")
            percentage = convert(user_input)
            break
        except ValueError:
            print("fraction format must be integer/integer, and x must not be larger than y.")
        except ZeroDivisionError:
            print("y cannot be zero")

    gauge_value = gauge(percentage)
    if isinstance(gauge_value, int):
        print(f"{gauge_value}%")
    else:
        print(f"{gauge_value}")


def convert(fraction):
    numerator, denominator = fraction.split('/')
    x = float(numerator)
    y = float(denominator)
    if x > y:
        raise ValueError
    if y == 0:
        raise ZeroDivisionError
    percentage = round((x / y) * 100)
    return percentage



def gauge(n):
    if n <= 1:
        return "E"
    elif n >= 99:
        return "F"
    else:
        return n

if __name__ == "__main__":
    main()












