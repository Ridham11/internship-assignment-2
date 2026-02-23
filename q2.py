# Name: Ridham Mishra
# Question 2 – Simple Calculator

# Using try-except to handle invalid input
try:
    # Asking user to enter two numbers
    first_number = int(input("Enter first number: "))
    second_number = int(input("Enter second number: "))

    print("\nResults:")

    # Addition
    addition_result = first_number + second_number
    print(first_number, "+", second_number, "=", addition_result)

    # Subtraction
    subtraction_result = first_number - second_number
    print(first_number, "-", second_number, "=", subtraction_result)

    # Multiplication
    multiplication_result = first_number * second_number
    print(first_number, "*", second_number, "=", multiplication_result)

    # Division
    if second_number != 0:
        division_result = first_number / second_number
        
        print(first_number, "/", second_number, "=", division_result)
    else:
        print("Division by zero is not allowed")



    # Modulus
    if second_number != 0:
        modulus_result = first_number % second_number
        print(first_number, "%", second_number, "=", modulus_result)
    else:
        print("Modulus by zero is not allowed")

    # Exponentiation
    power_result = first_number ** second_number
    print(first_number, "^", second_number, "=", power_result)

except ValueError:
    print("Invalid input! Please enter integer numbers only.")