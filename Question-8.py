# Q8: Leap Year Checker
# This program checks whether a given year is a leap year.

try:
    # Taking input and converting to integer
    year = int(input("Enter a year: "))

    # Check valid year
    if year <= 0:
        print("Year must be a positive number.")

    else:
        # Leap year logic
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            print(year, "is a Leap Year.")
        else:
            print(year, "is NOT a Leap Year.")

except:
    print("Please enter a valid numeric year.")