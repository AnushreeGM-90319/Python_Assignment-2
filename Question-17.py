# Q17: Palindrome Checker
# This program checks whether a given input is a palindrome.

# Taking input
text = input("Enter a word or number: ")

# Remove spaces and convert to lowercase
text = text.replace(" ", "").lower()

# Check empty input
if text == "":
    print("Input cannot be empty.")

else:
    # Reverse the string
    reversed_text = text[::-1]

    # Compare original and reversed
    if text == reversed_text:
        print("It is a Palindrome.")

    else:
        print("It is NOT a Palindrome.")