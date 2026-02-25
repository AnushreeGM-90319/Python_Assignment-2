# Q3: String Manipulator
# This program performs different operations on a string.

# Taking input from user
text = input("Enter a string: ")

# Check if string is empty
if text == "":
    print("String cannot be empty.")

else:
    # Convert to uppercase
    upper_text = text.upper()

    # Convert to lowercase
    lower_text = text.lower()

    # Find length of string
    length = len(text)

    # Reverse the string
    reversed_text = text[::-1]

    # Count vowels
    vowel_count = 0
    vowels = "aeiouAEIOU"

    for ch in text:
        if ch in vowels:
            vowel_count += 1

    # Display results
    print("\n--- STRING MANIPULATION RESULT ---")
    print("Original String :", text)
    print("Uppercase       :", upper_text)
    print("Lowercase       :", lower_text)
    print("Length          :", length)
    print("Reversed String :", reversed_text)
    print("Vowel Count     :", vowel_count)