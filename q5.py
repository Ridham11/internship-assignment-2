# Name: Ridham Mishra
# Question 5 – Bill Splitter

try:
    # Taking inputs from user
    total_bill = float(input("Enter total bill amount: "))
    number_of_people = int(input("Enter number of people: "))
    tax_percentage = float(input("Enter tax percentage: "))
    tip_percentage = float(input("Enter tip percentage: "))

    # Basic validations
    if number_of_people <= 0:
        print("Number of people must be greater than 0.")
    elif total_bill < 0:
        print("Bill amount cannot be negative.")
    else:
        print("\n--- BILL BREAKDOWN ---")

        # Subtotal
        subtotal = total_bill
        print("Subtotal: ₹", subtotal)

        # Tax calculation
        tax_amount = (subtotal * tax_percentage) / 100
        print("Tax Amount:", tax_amount)

        # After tax
        after_tax = subtotal + tax_amount
        print("After Tax:", after_tax)

        # Tip calculation
        tip_amount = (after_tax * tip_percentage) / 100
        print("Tip Amount:", tip_amount)

        # Final total
        final_total = after_tax + tip_amount
        print("Total Bill:", final_total)

        # Amount per person
        amount_per_person = final_total / number_of_people
        print("Amount Per Person:", amount_per_person)

except ValueError:
    print("Invalid input! Please enter numeric values only.")