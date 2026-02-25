# Q19: Text Analysis Using Functions
# This program analyzes text using different functions.

# Function to count characters (excluding spaces)
def count_characters(text):
    return len(text.replace(" ", ""))


# Function to count words
def count_words(text):
    words = text.split()
    return len(words)


# Function to count vowels and consonants
def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    for ch in text:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Function to find longest word
def longest_word(text):
    words = text.split()

    if len(words) == 0:
        return "No words found"

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


# Function to convert to uppercase
def to_upper(text):
    return text.upper()


# Function to convert to lowercase
def to_lower(text):
    return text.lower()


# Main Program
while True:
    print("\n----- TEXT ANALYSIS MENU -----")
    print("1. Count Characters")
    print("2. Count Words")
    print("3. Count Vowels and Consonants")
    print("4. Find Longest Word")
    print("5. Convert to Uppercase")
    print("6. Convert to Lowercase")
    print("7. Exit")

    try:
        choice = int(input("Enter your choice (1-7): "))

        if choice == 7:
            print("Thank you for using Text Analyzer.")
            break

        text = input("Enter your text: ")

        if text.strip() == "":
            print("Text cannot be empty.")
            continue

        # Perform operations
        if choice == 1:
            result = count_characters(text)
            print("Character Count:", result)

        elif choice == 2:
            result = count_words(text)
            print("Word Count:", result)

        elif choice == 3:
            v, c = count_vowels_consonants(text)
            print("Vowels     :", v)
            print("Consonants :", c)

        elif choice == 4:
            result = longest_word(text)
            print("Longest Word:", result)

        elif choice == 5:
            result = to_upper(text)
            print("Uppercase Text:", result)

        elif choice == 6:
            result = to_lower(text)
            print("Lowercase Text:", result)

        else:
            print("Invalid choice. Please select 1 to 7.")

    except:
        print("Please enter a valid number.")