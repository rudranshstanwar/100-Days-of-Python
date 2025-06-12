logo = r"""
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|

"""
print(logo)
# Creating the required functions
def add(n1, n2):
    """To add n1 with n2"""
    return n1 + n2
def sub(n1, n2):
    """To subtract n2 from n1"""
    return n1 - n2
def mul(n1, n2):
    """To multiply n1 with n2"""
    return n1 * n2
def div(n1,n2):
    """To divide n2 by n1"""
    return n1 / n2
# Storing the functions in a dictionary to call them later
operations = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
continue_operations = True
while continue_operations:
    print(logo)
    number1 = float(input("What's the first number?: "))
    print("+" + "\n" + "\n" + "-" + "\n" + "*" + "\n" +"/")
    operation = input("Pick an operation: ")
    number2 = float(input("What's the next number?: "))
    number = operations[operation](number1, number2)
    print(f"{number1} {operation} {number2} = {number}")
    continue_or_not = input(f"Type 'y' to continue calculating with {number}, or type 'n' to start a new calculation:\n")
    if continue_or_not == "y":
        number1 = number
        print("+" + "\n" + "\n" + "-" + "\n" + "*" + "\n" + "/")
        operation = input("Pick an operation: ")
        number2 = float(input("What's the next number?: "))
        number = operations[operation](number1, number2)
        print(f"{number1} {operation} {number2} = {number}")
        continue_or_not = input(f"Type 'y' to continue calculating with {number}, or type 'n' to start a new calculation:\n")
    elif continue_or_not == "n":
        print("\n"*20)
