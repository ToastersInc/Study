# implement a function called validate that expects an IPv4 address as input as a str and then returns True or False, respectively, if that input is a valid IPv4 address or not.

# Structure numb3rs.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit, but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.

import re


def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    # validate that input is a valid ip address #.#.#.# with each # being 0-255
    if re.search(r"\b(?:(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\.){3}(?:25[0-5]|2[0-4]\d|1\d{2}|[1-9]?\d)\b", ip):
        return True
    else:
        return False

if __name__ == "__main__":
    main()
