# Name: Ridham Mishra
# Question 14 – Factorial Calculator

# This program calculates the factorial of a number
# using a loop and displays step-by-step calculation.


# Taking input from user
number = int(input("Enter a number: "))

# Handling negative numbers
if number < 0:
    print("Factorial is not defined for negative numbers.")

# Handling 0
elif number == 0:
    print("0! = 1")

# For positive numbers
else:
    factorial = 1
    expression = ""

    # Loop from number down to 1
    for i in range(number, 0, -1):

        factorial = factorial * i

        # Creating step-by-step expression
        expression = expression + str(i)

        if i != 1:
            expression = expression + " x "

    # Printing final result
    print(str(number) + "! =", expression, "=", factorial)