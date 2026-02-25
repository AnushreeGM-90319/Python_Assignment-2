# Q15: Prime Number Checker
# This program checks whether a given number is prime.

try:
    # Taking input
    num = int(input("Enter a number: "))

    # Check valid input
    if num <= 1:
        print(num, "is NOT a Prime Number.")

    else:
        is_prime = True  # Flag variable

        # Check divisibility from 2 to sqrt(num)
        for i in range(2, int(num**0.5) + 1):

            if num % i == 0:
                is_prime = False
                break

        # Display result
        if is_prime:
            print(num, "is a Prime Number.")
        else:
            print(num, "is NOT a Prime Number.")

except:
    print("Please enter a valid integer.")