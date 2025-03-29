
def main():
    # prompt the user for an Expression
    answer = input("Expression: ")
    num1, op, num2 = answer.split()
    num1 = float(num1)
    num2 = float(num2)
    new_answer = calculate(num1, op, num2)
    print(new_answer)

   
def calculate(num1, op, num2):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "/":
        return num1 / num2
    elif op == "*":
        return num1 * num2
    else:
        print("invalid operator")







main()

