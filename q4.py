# Name: Ridham Mishra
# Question 4 – Age Calculator

# Assuming current year
current_year = 2026

try:
    # Asking user to enter birth year
    birth_year = int(input("Enter your birth year: "))

    # Checking if birth year is valid
    if birth_year > current_year:
        print("Birth year cannot be in the future.")
    else:
        # Calculating current age
        current_age = current_year - birth_year
        print("\nCurrent Age:", current_age)

        # Age in months
        age_in_months = current_age * 12
        print("Age in Months:", age_in_months)

        # Age in days (approximate)
        age_in_days = current_age * 365
        print("Age in Days (approx):", age_in_days)

        # Age in hours
        age_in_hours = age_in_days * 24
        print("Age in Hours:", age_in_hours)

        # Age in minutes
        age_in_minutes = age_in_hours * 60
        print("Age in Minutes:", age_in_minutes)

        # Years until 100
        years_to_100 = 100 - current_age
        print("Years until age 100:", years_to_100)

except ValueError:
    print("Invalid input! Please enter a valid year.")