# Exercise: Palindrome Sentences
import string
sentence = input ("Enter a sentence to check if it is a Palindrome: ")

sentence = sentence.translate(str.maketrans('', '', string.punctuation)).replace(" ", "").lower()

if sentence == sentence[::-1]:
    print("The sentence is a Palindrome.")
else:
    print("The sentence is not a Palindrome.")