# Exercise: Anagram Checker
string1 = input("Enter the First String: ")
string2 = input("Enter the Second String: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

# Check if the sorted characters of both strings are the same
if sorted(string1) == sorted(string2):
    print("The Strings are Anagrams.")
else:
    print("The Strings are not Anagrams.")