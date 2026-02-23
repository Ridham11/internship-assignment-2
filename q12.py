# Name: Ridham Mishra
# Question 12 – Multiplication Table Generator

# This program asks the user for a number
# and prints its multiplication table up to a given range


# Taking number input from user
number = int(input("Enter a number: "))

# Taking range input from user
end_range = int(input("Enter the range (end value): "))

print("\nMultiplication Table of", number)

# Using for loop to generate table
for i in range(1, end_range + 1):
    
    # Calculating multiplication
    result = number * i
    
    # Printing in proper format
    print(number, "x", i, "=", result)