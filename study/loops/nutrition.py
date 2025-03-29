#!/usr/bin/env python3

fruits = [ {"name": "apple", "calories": "130"},
          {"name": "avocado", "calories": "50"} ]

def main():
    print(len(fruits))
    answer = input("Item: ").lower()
    for fruit in fruits:
        if answer == fruit["name"]:
            print(f"Calories: {fruit["calories"]}")
main()
