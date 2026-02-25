# Q18: Calculator Using Functions
# This program performs calculations using functions.

# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    else:
        return a / b


# Main program
while True:
    try:
        # Display menu
        print("\n----- CALCULATOR MENU -----")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = int(input("Enter your choice (1-5): "))

        # Exit option
        if choice == 5:
            print("Thank you for using calculator.")
            break

        # Taking numbers
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        # Perform operation
        if choice == 1:
            result = add(num1, num2)
            print("Result:", result)

        elif choice == 2:
            result = subtract(num1, num2)
            print("Result:", result)

        elif choice == 3:
            result = multiply(num1, num2)
            print("Result:", result)

        elif choice == 4:
            result = divide(num1, num2)
            print("Result:", result)

        else:
            print("Invalid choice. Please select 1 to 5.")

    except:
        print("Please enter valid numeric input.")