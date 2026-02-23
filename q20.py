# Name: Ridham Mishra
# Question 20 – Number System Functions


# 1. Factorial
def factorial(n):

    if n < 0:
        return "Factorial not defined for negative numbers"

    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


# 2. Prime Check
def is_prime(n):

    if n <= 1:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 3. Fibonacci
def fibonacci(n):

    if n <= 0:
        return "Invalid input"

    if n == 1:
        return 0
    if n == 2:
        return 1

    a = 0
    b = 1

    for i in range(3, n + 1):
        c = a + b
        a = b
        b = c

    return b


# 4. Sum of Digits
def sum_of_digits(n):

    n = abs(n)
    total = 0

    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10

    return total


# 5. Reverse Number
def reverse_number(n):

    sign = 1
    if n < 0:
        sign = -1
        n = -n

    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n = n // 10

    return sign * reversed_num


# 6. Armstrong Number
def is_armstrong(n):

    original = n
    total = 0

    while n > 0:
        digit = n % 10
        total = total + (digit * digit * digit)
        n = n // 10

    if total == original:
        return True
    else:
        return False


# 7. GCD
def gcd(a, b):

    while b != 0:
        temp = b
        b = a % b
        a = temp

    return a


# 8. LCM
def lcm(a, b):

    return abs(a * b) // gcd(a, b)


# 9. Perfect Number
def is_perfect_number(n):

    if n <= 0:
        return False

    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n:
        return True
    else:
        return False


# 10. Menu Function
def math_menu():

    while True:

        print("\n--- MATH MENU ---")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci")
        print("4. Sum of Digits")
        print("5. Reverse Number")
        print("6. Armstrong Check")
        print("7. GCD")
        print("8. LCM")
        print("9. Perfect Number")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "10":
            print("Exiting...")
            break

        try:

            if choice == "1":
                n = int(input("Enter number: "))
                print("Factorial:", factorial(n))

            elif choice == "2":
                n = int(input("Enter number: "))
                if is_prime(n):
                    print("Prime Number")
                else:
                    print("Not Prime")

            elif choice == "3":
                n = int(input("Enter position: "))
                print("Fibonacci:", fibonacci(n))

            elif choice == "4":
                n = int(input("Enter number: "))
                print("Sum of digits:", sum_of_digits(n))

            elif choice == "5":
                n = int(input("Enter number: "))
                print("Reversed number:", reverse_number(n))

            elif choice == "6":
                n = int(input("Enter number: "))
                if is_armstrong(n):
                    print("Armstrong Number")
                else:
                    print("Not Armstrong")

            elif choice == "7":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("GCD:", gcd(a, b))

            elif choice == "8":
                a = int(input("Enter first number: "))
                b = int(input("Enter second number: "))
                print("LCM:", lcm(a, b))

            elif choice == "9":
                n = int(input("Enter number: "))
                if is_perfect_number(n):
                    print("Perfect Number")
                else:
                    print("Not Perfect")

            else:
                print("Invalid choice")

        except ValueError:
            print("Please enter valid integer input")


math_menu()