# Q6: Grade Calculator
# This program calculates grade based on marks.

try:
    # Taking input and converting to integer
    marks = int(input("Enter your marks (0 to 100): "))

    # Check valid range
    if marks < 0 or marks > 100:
        print("Marks must be between 0 and 100.")

    else:
        # Grade calculation
        if marks >= 90:
            grade = "A+"

        elif marks >= 80:
            grade = "A"

        elif marks >= 70:
            grade = "B"

        elif marks >= 60:
            grade = "C"

        elif marks >= 50:
            grade = "D"

        else:
            grade = "Fail"

        # Display result
        print("\n----- RESULT -----")
        print("Marks :", marks)
        print("Grade :", grade)
        print("------------------")

except:
    print("Please enter valid numeric marks.")