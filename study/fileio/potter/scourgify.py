# Expects the user to provide two command-line arguments:

     # the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
     #the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

#Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.


#If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

import csv
import os
import sys


def main():
    # check for appropriate amount of arguements
    if len(sys.argv) != 3:
        sys.exit("program takes three arguments, scourgify.py name.csv new.csv")
    # check if the file exists
    if not os.path.exists(sys.argv[1]):
        sys.exit("file does not exist")


    """open before.csv to read"""

    registry = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            registry.append(row)

    students = []

    for student in registry:
        students.append(student["name"])

    print(students)




if __name__ == "__main__":
    main()
