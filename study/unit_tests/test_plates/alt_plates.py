#   In a file called plates.py, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein is_valid still expects a str as input and returns True if that str meets all requirements and False if it does not, but main is only called if the value of __name__ is "__main__":

#   def main():
#       ...


#   def is_valid(s):
#       ...


#   if __name__ == "__main__":
#       main()

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
    if s[0].isnumeric() or s[1].isnumeric():
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

if __name__ == "__main__":
    main()



