# Name: Ridham Mishra
# Question 13 – Sum and Average Calculator

# This program asks the user how many numbers they want to enter.
# Then it calculates:
# 1. Sum
# 2. Average
# 3. Maximum number
# 4. Minimum number


# Asking how many numbers the user wants to enter
count = int(input("How many numbers do you want to enter? "))

# Initializing variables
total_sum = 0

# Taking first number separately to initialize max and min
first_number = int(input("Enter number 1: "))
total_sum = total_sum + first_number

maximum = first_number
minimum = first_number


# Loop for remaining numbers
for i in range(2, count + 1):

    number = int(input("Enter number " + str(i) + ": "))

    # Adding to total sum
    total_sum = total_sum + number

    # Checking maximum
    if number > maximum:
        maximum = number

    # Checking minimum
    if number < minimum:
        minimum = number


# Calculating average
average = total_sum / count


# Displaying results
print("\nResults:")
print("Sum:", total_sum)
print("Average:", average)
print("Maximum:", maximum)
print("Minimum:", minimum)