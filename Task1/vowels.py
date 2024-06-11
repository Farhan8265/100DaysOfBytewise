# Exercise: Count Vowels
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in user_input:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)