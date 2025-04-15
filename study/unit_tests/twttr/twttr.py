#   In a file called twttr.py, reimplement Setting up my twttr from Problem Set 2, restructuring your code per the below, wherein shorten expects a str as input and returns that same str but with all vowels (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase.

#   def main():
#       ...


#   def shorten(word):
#       ...


#   if __name__ == "__main__":
#       main()



def main():
    answer = input("Input: ")
    answer = strip_vowel(answer)
    print(f"Output: {answer}")


def strip_vowel(input):
    vowel = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    stripped_answer = ""
    for char in input:
        if char not in vowel:
            stripped_answer += char
    return stripped_answer

if __name__ == "__main__":
    main()

