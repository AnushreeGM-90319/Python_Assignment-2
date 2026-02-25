# Q9: Ticket Pricing System
# This program calculates ticket price based on age.

try:
    # Taking input and converting to integer
    age = int(input("Enter your age: "))

    # Check valid age
    if age <= 0:
        print("Age must be a positive number.")

    else:
        # Ticket pricing logic
        if age < 12:
            price = 50
            category = "Child"

        elif age <= 60:
            price = 100
            category = "Adult"

        else:
            price = 70
            category = "Senior Citizen"

        # Display result
        print("\n----- TICKET DETAILS -----")
        print("Age      :", age)
        print("Category :", category)
        print("Price    : ₹", price)
        print("--------------------------")

except:
    print("Please enter a valid numeric age.")