# Name: Ridham Mishra
# Question 16 – Number Guessing Game (Bonus Version)

# This program creates a number guessing game.
# Features:
# 1. 7 attempts
# 2. Hint if guess is close (difference within 5)
# 3. Tracks best score (minimum attempts used)

import random

best_score = 0   # To store minimum attempts used

while True:

    secret_number = random.randint(1, 100)
    guessed_correctly = False

    print("\n--- NUMBER GUESSING GAME ---")
    print("Guess the number between 1 and 100.")
    print("You have 7 attempts.")

    for attempt in range(1, 8):

        guess = int(input("Enter your guess: "))
        attempts_left = 7 - attempt

        # Check correct guess
        if guess == secret_number:
            print("Congratulations! You guessed correctly.")
            print("Attempts used:", attempt)

            guessed_correctly = True

            # Updating best score
            if best_score == 0 or attempt < best_score:
                best_score = attempt

            break

        # Check if guess is close (difference within 5)
        elif guess > secret_number:

            if guess - secret_number <= 5:
                print("Too high, but very close!")
            else:
                print("Too high!")

            print("Attempts remaining:", attempts_left)

        else:

            if secret_number - guess <= 5:
                print("Too low, but very close!")
            else:
                print("Too low!")

            print("Attempts remaining:", attempts_left)

    # If user failed
    if not guessed_correctly:
        print("You failed to guess the number.")
        print("Correct number was:", secret_number)

    # Show best score if exists
    if best_score != 0:
        print("Best score (minimum attempts):", best_score)

    # Ask to play again
    choice = input("Play again? (yes/no): ")

    if choice != "yes":
        print("Game Over.")
        break