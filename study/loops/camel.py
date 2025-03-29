def main():
    answer = input("camelCase: ")
    answer = reformat(answer)    
    print(answer)

def reformat(string):
    new_string = ""
    for char in string:
        if char.isupper():
            new_string += "_"
            new_string += char.lower()
        else:
            new_string += char
    return new_string

main()
