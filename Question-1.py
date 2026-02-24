# Q1: Personal Bio Card
# This program creates a simple bio card.

# Take name input and check if empty
name = input("Enter your name: ")
if name == "":
    print("Name cannot be empty.")
else:
    try:
        # Take age and convert to integer
        age = int(input("Enter your age: "))
        # Take other inputs
        course = input("Enter your course: ")
        college = input("Enter your college name: ")
        # Display bio card
        print("\n----- PERSONAL BIO CARD -----")
        print("Name    :", name)
        print("Age     :", age)
        print("Course  :", course)
        print("College :", college)
        print("------------------------------")
    except:
        print("Please enter a valid number for age.")