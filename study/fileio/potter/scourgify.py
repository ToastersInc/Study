# Expects the user to provide two command-line arguments:

# the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
# the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

# Converts that input to that output, splitting each name into a first name and last name. Assume that each student will have both a first name and last name.


# If the user does not provide exactly two command-line arguments, or if the first cannot be read, the program should exit via sys.exit with an error message.

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

    """open before.csv to read and put the contents into registry as a list of dictioanries"""

    registry = []
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            registry.append(row)

    """take name key value and split it into first and last name keys with the corresponding values"""
    for row in registry:
        if "name" in row and isinstance(row["name"], str):
            name_parts = row["name"].split(",")
            if len(name_parts) == 2:
                row["first_name"] = name_parts[1]
                row["last_name"] = name_parts[0]
                del row["name"]
            else:
                print("couldnt split names")

    #    print(registry)

    """write new registry to after.csv"""

    with open(sys.argv[2], "w") as file:
        writer = csv.DictWriter(file, fieldnames=["first_name", "last_name", "house"])
        writer.writeheader()
        writer.writerows(registry)


if __name__ == "__main__":
    main()
