# Name: Ridham Mishra
# Question 11 – Number Pattern Printer

# This program prints different number patterns based on user choice

pattern_choice = int(input("Choose pattern (1-4): "))
pattern_height = int(input("Enter height: "))

# Pattern 1
if pattern_choice == 1:
    for i in range(1, pattern_height + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

# Pattern 2
elif pattern_choice == 2:
    for i in range(1, pattern_height + 1):
        for j in range(i):
            print(i, end=" ")
        print()

# Pattern 3
elif pattern_choice == 3:
    for i in range(pattern_height, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()

# Pattern 4
elif pattern_choice == 4:
    for i in range(1, pattern_height + 1):
        for j in range(1, i + 1):
            print(j, end="")
        for j in range(i - 1, 0, -1):
            print(j, end="")
        print()

else:
    print("Invalid pattern choice.")