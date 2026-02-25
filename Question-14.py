# Q14: Factorial Calculator
# This program calculates factorial of a given number.

try:
    # Taking input
    num = int(input("Enter a number: "))

    # Check valid input
    if num < 0:
        print("Factorial is not defined for negative numbers.")

    else:
        factorial = 1

        # Loop to calculate factorial
        for i in range(1, num + 1):
            factorial = factorial * i

        # Display result
        print("\n----- RESULT -----")
        print("Number    :", num)
        print("Factorial :", factorial)
        print("------------------")

except:
    print("Please enter a valid integer.")