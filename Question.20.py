# Q20: Number System Using Functions
# This program converts numbers between different number systems.

# Function: Decimal to Binary
def decimal_to_binary(n):
    return bin(n)[2:]


# Function: Decimal to Octal
def decimal_to_octal(n):
    return oct(n)[2:]


# Function: Decimal to Hexadecimal
def decimal_to_hex(n):
    return hex(n)[2:].upper()


# Function: Binary to Decimal
def binary_to_decimal(b):
    return int(b, 2)


# Main Program
while True:

    print("\n----- NUMBER SYSTEM MENU -----")
    print("1. Decimal to Binary")
    print("2. Decimal to Octal")
    print("3. Decimal to Hexadecimal")
    print("4. Binary to Decimal")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice (1-5): "))

        # Exit
        if choice == 5:
            print("Thank you for using Number System Program.")
            break

        # Decimal to Binary
        elif choice == 1:
            num = int(input("Enter decimal number: "))

            if num < 0:
                print("Enter a positive number.")

            else:
                print("Binary:", decimal_to_binary(num))

        # Decimal to Octal
        elif choice == 2:
            num = int(input("Enter decimal number: "))

            if num < 0:
                print("Enter a positive number.")

            else:
                print("Octal:", decimal_to_octal(num))

        # Decimal to Hexadecimal
        elif choice == 3:
            num = int(input("Enter decimal number: "))

            if num < 0:
                print("Enter a positive number.")

            else:
                print("Hexadecimal:", decimal_to_hex(num))

        # Binary to Decimal
        elif choice == 4:
            binary = input("Enter binary number: ")

            # Validate binary input
            valid = True
            for ch in binary:
                if ch not in "01":
                    valid = False
                    break

            if not valid:
                print("Invalid binary number.")

            else:
                print("Decimal:", binary_to_decimal(binary))

        else:
            print("Invalid choice. Select between 1 to 5.")

    except:
        print("Please enter valid numeric input.")