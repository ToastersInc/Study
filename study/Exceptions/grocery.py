# In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). 
# Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. 
# No need to pluralize the items. 
# Treat the user’s input case-insensitively.

def main():
    list = []
    print("list groceries below")
    while True:
        try:
            list.append(input("").upper())
            list.sort()
        except EOFError:
            break
#   print(list)
            
    count = {}
    for item in list:
        if item in count:
            count[item] += 1
        else:
            count[item] = 1
    for item in count:
        print(f"{count[item]}: {item}")

main()



 
