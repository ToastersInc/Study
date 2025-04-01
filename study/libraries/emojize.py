import sys
import emoji


def main():
    # prompt the user for the string
    user_input = input("Input: ")
    split_input = user_input.split()
    for word in split_input:
        if word[0] == ":" and word[-1] == ":":
            emojized_string = emoji.emojize(user_input, language="alias")
            print(f"Output: {emojized_string}")
    print("no words found to emojize")
    sys.exit()


if __name__ == "__main__":
    main()
