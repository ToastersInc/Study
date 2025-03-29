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


main()
