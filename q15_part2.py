# Part 2 – Find all prime numbers in a given range

start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Prime numbers in the range are:")

for num in range(start, end + 1):

    if num > 1:

        is_prime = True

        for i in range(2, num):

            if num % i == 0:
                is_prime = False
                break

        if is_prime:
            print(num, end=" ")