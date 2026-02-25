# Q13: Sum and Average Calculator
# This program calculates sum and average of given numbers.

try:
    # Taking how many numbers user wants to enter
    count = int(input("How many numbers do you want to enter? "))

    if count <= 0:
        print("Please enter a positive number.")

    else:
        total = 0

        # Loop to take numbers
        for i in range(1, count + 1):
            num = float(input(f"Enter number {i}: "))
            total += num

        # Calculate average
        average = total / count

        # Display result
        print("\n----- RESULT -----")
        print("Sum     :", total)
        print("Average :", round(average, 2))
        print("------------------")

except:
    print("Please enter valid numeric values.")