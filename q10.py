# Name: Ridham Mishra
# Question 10 – Simple ATM Simulator
# Description:
# This program simulates a simple ATM system.
# It allows the user to:
# 1. Check account balance
# 2. Deposit money
# 3. Withdraw money (while maintaining minimum balance of 500)
# 4. View transaction history
# 5. Exit the program


def atm_simulator():

    # Initial account balance is set to 10,000
    account_balance = 10000

    # This list will store all deposit and withdrawal transactions
    transaction_history = []

    # Infinite loop to keep ATM running until user chooses Exit
    while True:

        # Display ATM menu options
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. View Transaction History")
        print("5. Exit")

        # Take user input for menu choice
        user_choice = input("Enter your choice: ")

        # Option 1: Check current balance
        if user_choice == "1":
            print("Current Balance:", account_balance)

        # Option 2: Deposit money into account
        elif user_choice == "2":

            # Take deposit amount from user
            deposit_amount = int(input("Enter deposit amount: "))

            # Add deposit amount to current balance
            account_balance = account_balance + deposit_amount

            # Store deposit transaction in history list
            transaction_history.append("Deposited: " + str(deposit_amount))

            print("Deposit successful.")

        # Option 3: Withdraw money from account
        elif user_choice == "3":

            # Take withdrawal amount from user
            withdraw_amount = int(input("Enter withdraw amount: "))

            # Check if balance after withdrawal will remain >= 500
            # Minimum balance rule must be maintained
            if account_balance - withdraw_amount >= 500:

                # Subtract withdrawal amount from balance
                account_balance = account_balance - withdraw_amount

                # Store withdrawal transaction in history
                transaction_history.append("Withdrawn: " + str(withdraw_amount))

                print("Withdrawal successful.")

            else:
                # If minimum balance condition fails
                print("Insufficient balance.")
                print("Minimum balance of 500 must remain in account.")

        # Option 4: Display all past transactions
        elif user_choice == "4":

            print("\n--- Transaction History ---")

            # If no transactions have been made
            if len(transaction_history) == 0:
                print("No transactions yet.")

            # Display each transaction stored in list
            else:
                for transaction in transaction_history:
                    print(transaction)

        # Option 5: Exit ATM system
        elif user_choice == "5":
            print("Thank you for using the ATM.")
            break  # Exit the loop

        # If user enters invalid menu option
        else:
            print("Invalid choice. Please try again.")


# Call the ATM function to start the program
atm_simulator()