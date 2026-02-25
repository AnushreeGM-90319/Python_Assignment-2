# Q5: Bill Splitter
# This program splits a bill equally among people.

try:
    # Taking inputs
    total_bill = float(input("Enter total bill amount: "))
    people = int(input("Enter number of people: "))

    # Check valid input
    if total_bill <= 0:
        print("Bill amount must be greater than zero.")

    elif people <= 0:
        print("Number of people must be greater than zero.")

    else:
        # Calculate share
        share = total_bill / people

        # Display result
        print("\n----- BILL SPLIT DETAILS -----")
        print("Total Bill   : ₹", total_bill)
        print("People       :", people)
        print("Each Pays    : ₹", round(share, 2))
        print("------------------------------")

except:
    print("Please enter valid numeric values.")