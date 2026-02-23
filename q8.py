# Name: Ridham Mishra
# Question 8 – Leap Year Checker

# This program checks whether a given year is a leap year

try:
    year_input = int(input("Enter a year: "))

    # Check divisibility conditions for leap year
    if year_input % 4 == 0:
        if year_input % 100 == 0:
            if year_input % 400 == 0:
                print(year_input, "is a Leap Year.")
            else:
                print(year_input, "is NOT a Leap Year.")
        else:
            print(year_input, "is a Leap Year.")
    else:
        print(year_input, "is NOT a Leap Year.")

except ValueError:
    print("Invalid input! Please enter a valid year.")