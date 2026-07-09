"""Task 1: Simple Calculator:
Description: Develop a basic calculator that can
perform four primary arithmetic operations: addition,
subtraction, multiplication, and division.

Objectives:
Create functions for each operation.
Take two inputs from the user and allow them to select
the desired operation.
Handle division by zero with appropriate error
messages."""

def add(num1, num2):
    """Function to add two numbers."""
    return num1 + num2
def subtract(num1, num2):
    """Function to subtract two numbers."""
    return num1 - num2
def multiply(num1, num2):
    """Function to multiply two numbers."""
    return num1 * num2
def divide(num1, num2):
    """Function to divide two numbers."""
    if num2 == 0:
        return "Error! Division by zero is not allowed."
    else:
        return num1 / num2
def calculator():
    """Main function to run the calculator."""
    print("Welcome to the Simple Calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                print(f"{num1} / {num2} = {divide(num1, num2)}")
        else:
            print("Invalid Input")

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            break
    print("Thank you for using the Simple Calculator!")
if __name__ == "__main__":
    calculator()

