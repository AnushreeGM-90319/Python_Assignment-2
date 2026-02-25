# Q7: Temperature Converter
# This program converts temperature between Celsius and Fahrenheit.

try:
    # Taking temperature input
    temp = float(input("Enter temperature value: "))

    # Taking choice
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")

    choice = int(input("Enter your choice (1 or 2): "))

    # Conversion
    if choice == 1:
        # Celsius to Fahrenheit
        result = (temp * 9/5) + 32
        print("\nTemperature in Fahrenheit:", round(result, 2))

    elif choice == 2:
        # Fahrenheit to Celsius
        result = (temp - 32) * 5/9
        print("\nTemperature in Celsius:", round(result, 2))

    else:
        print("Invalid choice. Please select 1 or 2.")

except:
    print("Please enter valid numeric values.")