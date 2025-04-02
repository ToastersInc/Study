# implement a program that prompts the user for names,
# one per line, until the user inputs control-d.
# Assume that the user will input at least one name. Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and, and names with commas and one and, as in the below:

#   Adieu, adieu, to Liesl
#   Adieu, adieu, to Liesl and Friedrich
#   Adieu, adieu, to Liesl, Friedrich, and Louisa
#   Adieu, adieu, to Liesl, Friedrich, Louisa, and Kurt
#   Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, and Brigitta
#   Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, and Marta
#   Adieu, adieu, to Liesl, Friedrich, Louisa, Kurt, Brigitta, Marta, and Gretl


def main(): 
    names = []
    """ask for a name from user and continue to ask until they type 'Ctrl - d'"""
    while True:
        try:
            user_input = input("Name: ").title()
            names.append(user_input)
        except EOFError:
            break

    """check for the length of the names list and print the names with proper grammer"""
    print("")
    if len(names) < 1:
        print("you didnt enter any names")
    elif len(names) == 1:
        print(f"Adieu, adieu, to {names[0]}")
    elif len(names) == 2:
        print(f"Adieu, adieu, to {names[0]} and {names[1]}")
    elif len(names) > 2:
        for name in names:
            if name == names[0]:
                print(f"Adieu, adieu, to {name}, ", end="")
            elif names.index(name) > 0 and names.index(name) < len(names) - 1:
                print(f"{name}, ", end="")
            else:
                print(f"and {name}")


if __name__ == "__main__":
    main()
