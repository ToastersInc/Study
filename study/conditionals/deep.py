def main():
    # ask the user question 
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")
    answer = answer.lower()
    match answer:
        case "42" | "forty-two" | "forty two":
            print("yes")
        case _:
            print("no")

main()

