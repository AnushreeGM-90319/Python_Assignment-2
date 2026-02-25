# Q12: Multiplication Table Generator
# This program prints multiplication table of a given number.

try:
    # Taking input
    number = int(input("Enter a number: "))

    # Check valid input
    if number <= 0:
        print("Please enter a positive number.")

    else:
        print("\nMultiplication Table of", number)
        print("--------------------------")

        # Loop to generate table
        for i in range(1, 11):
            result = number * i
            print(number, "x", i, "=", result)

except:
    print("Please enter a valid numeric value.")