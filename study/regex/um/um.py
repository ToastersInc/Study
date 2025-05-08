# make function that takes a string and returns how many times "um" is in it. the return value should be a int.


def main():
    print(count(input("Text: ")))


def count(s):
    w = []
    s = s.lower()
    string = s.split(" ")
    for word in string:
        if word.startswith("um"):
            w.append(word)

    print(w)
    return len(w)


if __name__ == "__main__":
    main()


