# Exercise: Check for Palindrome
user_input = input("Enter a string: ")
processed_input = user_input.replace(" ", "").lower()
if processed_input == processed_input[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")
