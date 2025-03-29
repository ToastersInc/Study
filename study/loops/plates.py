# vanity plate must start with 2 letters - DONE
# min 2 chars max 6 chars - DONE
# no periods, spaces, or punctuation - DONE
# numbers come at the end only
import string

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    forbidden_fruit = [".", " "]

    if len(s) < 2: 
        return False 
    if len(s) > 6:
        return False
    if s[0].isnumeric() and s[1].isnumeric():
        return False

    for char in s:
        if char in string.punctuation:
            return False
        if char in forbidden_fruit:
            return False

        i = len(s) - 1
        while i >= 0 and s[i].isdigit():
            i -= 1

        if i < len(s) - 1 and s[i + 1] == '0':
            return False

        for j in range(i + 1):
            if s[j].isdigit():
                return False

    return True


main()
