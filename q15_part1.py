# Name: Ridham Mishra
# Question 15 – Prime Number Checker
# Part 1 – Check if a single number is prime


# Taking input from user
number = int(input("Enter a number: "))

# Prime numbers are greater than 1
if number <= 1:
    print(number, "is NOT a prime number.")

else:
    is_prime = True

    # Checking divisibility from 2 to number-1
    for i in range(2, number):

        if number % i == 0:
            is_prime = False
            break

    # Printing result
    if is_prime:
        print(number, "is a PRIME number.")
    else:
        print(number, "is NOT a prime number.")