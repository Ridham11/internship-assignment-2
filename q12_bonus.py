# Name: Ridham Mishra
# Question 12 – Bonus
# Full Multiplication Table (1 to 10)

# This program prints multiplication tables
# from 1 to 10 in a grid format

print("Full Multiplication Table (1 to 10)\n")

# Outer loop controls the rows (numbers 1 to 10)
for i in range(1, 11):

    # Inner loop controls the columns (1 to 10)
    for j in range(1, 11):

        # Multiply current row number with column number
        result = i * j

        # Print result with space
        print(result, end=" ")

    # Move to next line after one row is completed
    print()