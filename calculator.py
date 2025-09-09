#  Simple Calculator Project

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error! Division by zero is not allowed."
    return a / b


# Main program
def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    choice = input("Enter choice (1/2/3/4): ")

    # Taking inputs
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == '1':
        print(f"The result is: {add(a, b)}")
    elif choice == '2':
        print(f"The result is: {subtract(a, b)}")
    elif choice == '3':
        print(f"The result is: {multiply(a, b)}")
    elif choice == '4':
        print(f"The result is: {divide(a, b)}")
    else:
        print("Invalid choice!")


# Run the calculator
calculator()