
#   Prompts the user for a level, n
#   . If the user does not input 1, 2, or 3, the program should prompt again.

#   Randomly generates ten (10) math problems formatted as X + Y = , wherein each of X and Y is a non-negative integer with 
#    digits. No need to support operations other than addition (+).

#   Prompts the user to solve each of those problems. If an answer is not correct (or not even a number), the program should output EEE and prompt the user again, allowing the user up to three tries in total for that problem. If the user has still not answered correctly after three tries, the program should output the correct answer.

#   The program should ultimately output the user’s score: the number of correct answers out of 10.

#   Structure your program as follows, wherein get_level prompts (and, if need be, re-prompts) the user for a level and returns 1, 2, or 3, and generate_integer returns a randomly generated non-negative integer with level digits or raises a ValueError if level is not 1, 2, or 3:

import random
import sys

def main():
    numbers =[]

    selected_level = get_level()
    

    for _ in range(10):
        numbers.append(generate_integer(selected_level))
    
    answers_correct = 0
    questions = 10
    incorrect = 3
    while True:
        try:
            x = random.choice(numbers)
            y = random.choice(numbers)
            for i in range(3):
                answer = int(input(f"{x} + {y} = "))
                if answer == x + y:
                    answers_correct += 1
                    break
                else:
                    incorrect -= 1
                    print("EEE")
                
            questions -= 1

            if incorrect == 0:
                print(f"{x} + {y} = ", x + y)
                incorrect = 3

            if questions == 0:
                print(f"Correct answers = {answers_correct}")
                sys.exit()
                


        except ValueError:
            print("answer must be not negative numbers only")



"""prompts user for a level and returns 1, 2 or 3"""
def get_level():
    while True:
        try:
            n = int(input("level 1, 2, or 3? "))
            if n != 1 and n != 2 and n != 3:
                raise ValueError
            break
        except ValueError:
            print("acceptable answers: 1, 2 or 3")
    return n

"""generate a positive integer with level digits"""
def generate_integer(level):
    if level == 1:
        int = random.randint(1, 10)
        return int
    elif level == 2:
        int = random.randint(11, 99)
        return int
    else:
        int = random.randint(100, 999)
        return int


if __name__ == "__main__":
    main()











