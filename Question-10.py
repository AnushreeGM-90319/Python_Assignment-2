# Q10: Simple ATM Simulator
# This program simulates basic ATM operations.

# Initial details
correct_pin = "1234"
balance = 5000.0

# PIN verification
entered_pin = input("Enter your ATM PIN: ")

if entered_pin != correct_pin:
    print("Incorrect PIN. Access Denied.")

else:
    print("\nLogin Successful!")

    while True:
        try:
            # Display menu
            print("\n----- ATM MENU -----")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = int(input("Enter your choice (1-4): "))

            # Menu operations
            if choice == 1:
                print("Current Balance: ₹", balance)

            elif choice == 2:
                amount = float(input("Enter amount to deposit: "))

                if amount <= 0:
                    print("Enter a valid amount.")

                else:
                    balance += amount
                    print("Deposit Successful!")
                    print("Updated Balance: ₹", balance)

            elif choice == 3:
                amount = float(input("Enter amount to withdraw: "))

                if amount <= 0:
                    print("Enter a valid amount.")

                elif amount > balance:
                    print("Insufficient Balance.")

                else:
                    balance -= amount
                    print("Withdrawal Successful!")
                    print("Remaining Balance: ₹", balance)

            elif choice == 4:
                print("Thank you for using ATM.")
                break

            else:
                print("Invalid choice. Try again.")

        except:
            print("Please enter valid numeric input.")