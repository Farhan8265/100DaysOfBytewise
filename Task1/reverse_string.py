# Exercise: Reverse a String
user_input = input("Enter a string: ")
reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)