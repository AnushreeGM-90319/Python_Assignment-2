# Q4: Age Calculator
# This program calculates age using birth year and current year.

try:
    # Taking inputs and converting to integer
    birth_year = int(input("Enter your birth year: "))
    current_year = int(input("Enter current year: "))

    # Check valid years
    if birth_year > current_year:
        print("Birth year cannot be greater than current year.")

    elif birth_year <= 0 or current_year <= 0:
        print("Year must be positive.")

    else:
        # Calculate age
        age = current_year - birth_year

        # Display result
        print("\n----- AGE DETAILS -----")
        print("Birth Year  :", birth_year)
        print("Current Year:", current_year)
        print("Your Age    :", age, "years")
        print("------------------------")

except:
    print("Please enter valid numeric values for years.")