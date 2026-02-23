# Name: Ridham Mishra
# Question 18 – Calculator Functions


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
        return "Division by zero is not allowed."
    else:
        return a / b


# Function for modulus
def modulus(a, b):
    return a % b


# Function for power
def power(a, b):
    return a ** b


# Main calculator function with menu
def calculator():

    while True:

        print("\n--- CALCULATOR MENU ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Modulus")
        print("6. Power")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "7":
            print("Calculator Closed.")
            break

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

        elif choice == "5":
            print("Result:", modulus(num1, num2))

        elif choice == "6":
            print("Result:", power(num1, num2))

        else:
            print("Invalid choice.")


# Calling main function
calculator()