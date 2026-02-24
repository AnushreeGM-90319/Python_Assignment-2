# Q2: Simple Calculator

try:
    # Taking inputs
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    operator = input("Enter operator (+, -, *, /): ")

    # Switch using match-case
    match operator:
        case "+":
            result = num1 + num2

        case "-":
            result = num1 - num2

        case "*":
            result = num1 * num2

        case "/":
            if num2 == 0:
                print("Error: Division by zero not allowed.")
                result = None
            else:
                result = num1 / num2

        case _:
            print("Invalid operator.")
            result = None

    # Display result
    if result is not None:
        print("Result:", result)

except:
    print("Please enter valid numbers.")