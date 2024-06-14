# Exercise: Longest Palindromic Substring
def is_palindrome(s):
    return s == s[::-1]

def longest_palindromic_substring(s):
    n = len(s)
    if n == 0:
        return ""

    max_length = 0
    longest_palindrome = ""

    for i in range(n):
        for j in range(i, n):
            substring = s[i:j+1]
            if is_palindrome(substring) and len(substring) > max_length:
                max_length = len(substring)
                longest_palindrome = substring
    return longest_palindrome

input_string = input("Enter a String: ")

longest_palindrome = longest_palindromic_substring(input_string)

if longest_palindrome:
    print("Longest Palindromic Substring:", longest_palindrome)
else:
    print("No Palindromic Substring found in the input string.")
