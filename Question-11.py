# Q11: Number Pattern Printer
# This program prints a number pattern based on user input.

try:
    # Taking input
    rows = int(input("Enter number of rows: "))

    if rows <= 0:
        print("Please enter a positive number.")

    else:
        # Outer loop for rows
        for i in range(1, rows + 1):

            # Inner loop for numbers
            for j in range(1, i + 1):
                print(j, end="")

            print()  # Move to next line

except:
    print("Please enter a valid numeric value.")