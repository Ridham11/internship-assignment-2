# Name: Ridham Mishra
# Question 7 – Temperature Converter

# This program converts temperature between different units
# It uses a menu-based system and runs until user chooses Exit

while True:

    # Displaying menu options
    print("\n--- TEMPERATURE CONVERTER ---")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    # Taking user choice
    user_choice = input("Enter your choice (1-7): ")

    # If user selects Exit
    if user_choice == "7":
        print("Exiting program.")
        break

    try:
        # Taking temperature input
        input_temperature = float(input("Enter temperature value: "))

        # Celsius to Fahrenheit
        if user_choice == "1":
            converted_temperature = (input_temperature * 9/5) + 32
            print("Converted Temperature:", converted_temperature)

        # Fahrenheit to Celsius
        elif user_choice == "2":
            converted_temperature = (input_temperature - 32) * 5/9
            print("Converted Temperature:", converted_temperature)

        # Celsius to Kelvin
        elif user_choice == "3":
            converted_temperature = input_temperature + 273.15
            print("Converted Temperature:", converted_temperature)

        # Kelvin to Celsius
        elif user_choice == "4":
            converted_temperature = input_temperature - 273.15
            print("Converted Temperature:", converted_temperature)

        # Fahrenheit to Kelvin
        elif user_choice == "5":
            converted_temperature = ((input_temperature - 32) * 5/9) + 273.15
            print("Converted Temperature:", converted_temperature)

        # Kelvin to Fahrenheit
        elif user_choice == "6":
            converted_temperature = ((input_temperature - 273.15) * 9/5) + 32
            print("Converted Temperature:", converted_temperature)

        # If invalid option
        else:
            print("Invalid choice! Please select between 1 and 7.")

    except ValueError:
        # If user enters non-numeric temperature
        print("Invalid input! Please enter numeric value.")