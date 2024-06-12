# Exercise: Check for Palindrome
word = input("Enter a Word: ")
word = word.lower()
if word == word[::-1]:
    print(f"'{word}' is a Palindrome.")
else:
    print(f"'{word}' is not a Palindrome.")