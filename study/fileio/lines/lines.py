# Even so, in a file called lines.py, implement a program that expects exactly one command-line argument,
# the name (or path) of a Python file, and outputs the number of lines of code in that file, excluding comments and blank lines.
# If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.

# Assume that any line that starts with #, optionally preceded by whitespace, is a comment.
# (A docstring should not be considered a comment.)
# Assume that any line that only contains whitespace is blank.
import sys
import os


def main():
    # check for appropriate amount of arguements
    if len(sys.argv) != 2:
        sys.exit("program takes two arguments, lines.py filename.py")
    # check if the file exists
    if os.path.exists(sys.argv[1]):
        print("file exists")
    else:
        sys.exit("file does not exist")
    # check if the argv[1] ends in .py
    if sys.argv[1][-3:] != ".py":
        sys.exit("Not a python file")

    lines = []
    line_count = 0
    # open file
    with open(sys.argv[1]) as file:
        # read each line
        for line in file:
            lines.append(line.rstrip().lstrip())

    for line in lines:
        if not line.strip():
            continue
        elif line.startswith("#"):
            continue
        else:
            line_count += 1
        # if valid line then add 1 to lines variable

    # print lines
    print(lines)
    print(line_count)


if __name__ == "__main__":
    main()
