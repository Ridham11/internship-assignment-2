# Name: Ridham Mishra
# Question 6 – Grade Calculator

try:
    print("Enter marks for 5 subjects (out of 100):")

    subject1 = int(input("Subject 1: "))
    subject2 = int(input("Subject 2: "))
    subject3 = int(input("Subject 3: "))
    subject4 = int(input("Subject 4: "))
    subject5 = int(input("Subject 5: "))

    # Validate marks range
    if (subject1 < 0 or subject1 > 100 or
        subject2 < 0 or subject2 > 100 or
        subject3 < 0 or subject3 > 100 or
        subject4 < 0 or subject4 > 100 or
        subject5 < 0 or subject5 > 100):

        print("Marks should be between 0 and 100.")

    else:
        # Calculate total
        total_marks = subject1 + subject2 + subject3 + subject4 + subject5
        print("\nTotal Marks:", total_marks)

        # Calculate percentage
        percentage = total_marks / 5
        print("Percentage:", percentage)

        # Determine grade
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 50:
            grade = "D"
        else:
            grade = "F"

        print("Grade:", grade)

        # Check pass/fail (all subjects must be >= 40)
        if (subject1 >= 40 and
            subject2 >= 40 and
            subject3 >= 40 and
            subject4 >= 40 and
            subject5 >= 40):
            print("Result: PASS")
        else:
            print("Result: FAIL")

except ValueError:
    print("Invalid input! Please enter numeric marks only.")