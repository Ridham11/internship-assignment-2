# Name: Ridham Mishra
# Question 9 – Ticket Pricing System

# This program calculates movie ticket price based on age and day

try:
    # Taking inputs
    person_age = int(input("Enter age: "))
    day_of_week = input("Enter day of week: ")
    number_of_tickets = int(input("Enter number of tickets: "))

    # Determining base price based on age
    if person_age < 3:
        base_ticket_price = 0
    elif person_age <= 12:
        base_ticket_price = 150
    elif person_age <= 59:
        base_ticket_price = 300
    else:
        base_ticket_price = 200

    # Calculating total before discount
    total_before_discount = base_ticket_price * number_of_tickets

    # Applying weekend discount (20%)
    if (day_of_week == "Friday" or 
        day_of_week == "Saturday" or 
        day_of_week == "Sunday"):
        discount_amount = total_before_discount * 0.20
    else:
        discount_amount = 0

    # Final amount after discount
    final_amount = total_before_discount - discount_amount

    print("\nBase Amount:", total_before_discount)
    print("Discount:", discount_amount)
    print("Final Amount:", final_amount)

except ValueError:
    print("Invalid input! Please enter valid numbers.")