#Simple Calculator

#Imports
from valid_inputs import accepted_inputs

def main():

    go_again = 'y'

    while go_again != 'n':

        get_operation()

        go_again = input("Another Calculation? [Y/N]\n").strip().lower()

    print("Thanks for using the calculator.\n")

def get_operation():

    print("Please choose an operation.\n")

    while True:

        operation = input("Multiply [*], Divide [/], Add [+], Subtract [-], or Y for a list of valid inputs.\n")
        operation = operation.lower().strip()

        if operation == 'y':
            for k, v in accepted_inputs.items():
                print(f"'{k}' for '{v}'.")
            continue
        
        if operation in accepted_inputs:
            operation = accepted_inputs[operation]
            break

        else:
            operation = input("Invalid Input. Enter Y to see valid options.\n")

    a, b = get_inputs(operation)

    if operation == '*':
        result = multiply(a, b)

    elif operation == '/':
        result = divide(a, b)

    elif operation == '+':
        result = add(a, b)

    elif operation == '-':
        result = subtract(a, b)

    print(f"Result is {result}.")

def get_inputs(operation):

    while True:
        input_1 = input("First number: \n")
        try:
            input_1 = float(input_1)
            break
        except ValueError:
            print("Invalid input, please enter a number.\n")

    while True:
        input_2 = input("Second number: \n")
        try:
            input_2 = float(input_2)
        except ValueError:
            print("Invalid input, please enter a number.\n")
            continue

        if operation == '/' and input_2 == 0:
            print("Cannot divide by 0.")
            continue
        
        break

    return input_1, input_2



def multiply(input_1, input_2):
    return input_1 * input_2

def divide(input_1, input_2):
    return input_1 / input_2

def add(input_1, input_2):
    return input_1 + input_2

def subtract(input_1, input_2):
    return input_1 - input_2

if __name__ == "__main__":
    main()