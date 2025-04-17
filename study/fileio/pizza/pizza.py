from tabulate import tabulate
import sys
import os
import csv

def main():
    # check for appropriate amount of arguements
    if len(sys.argv) != 2:
        sys.exit("program takes two arguments, lines.py filename.py")
    # check if the file exists
    if not os.path.exists(sys.argv[1]):
        sys.exit("file does not exist")
    # check if the argv[1] ends in .py
    if sys.argv[1][-4:] != ".csv":
        sys.exit("Not a python file")

    rows = []

    with open(sys.argv[1]) as file:
        reader = csv.reader(file)
        for row in reader:
            rows.append(row)

    print(tabulate(rows, headers="firstrow", tablefmt="grid"))


if __name__ == "__main__":
    main()


