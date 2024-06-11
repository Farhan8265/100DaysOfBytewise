# Exercise: Sum of two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
sum = num1 + num2
print(f"The sum is {sum}")


# Exercise: Area of Circle
radius = float (input ("Enter the Radius of Circle: "))
area = 3.14*(radius*radius)
print(f"The area of the circle is {area}")


# Exercise: Even or Odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"The number {num} is even.")
else:
    print(f"The number {num} is odd.")


# Exercise: Simple Calculator
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = "Error: Invalid operation."
print(f"The result of {num1} {operation} {num2} is: {result}")


# Exercise: Find the Largest Number
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))
if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3
print(f"The largest number among {num1}, {num2}, and {num3} is {largest}.")


# Exercise: Reverse a String
user_input = input("Enter a string: ")
reversed_string = ""
for char in user_input:
    reversed_string = char + reversed_string
print("Reversed string:", reversed_string)


# Exercise: Count Vowels
user_input = input("Enter a string: ")
vowels = "aeiouAEIOU"
vowel_count = 0
for char in user_input:
    if char in vowels:
        vowel_count += 1
print("Number of vowels:", vowel_count)


# Exercise: Fabonacci Sequence
n = int(input("Enter the number of terms: "))
a, b = 0, 1
print("Fibonacci sequence: ")
for i in range(n):
    print(a, end=" ")

    a, b = b, a + b


# Exercise: Check for Palindrome
user_input = input("Enter a string: ")
processed_input = user_input.replace(" ", "").lower()
if processed_input == processed_input[::-1]:
    print("The string is a Palindrome.")
else:
    print("The string is not a Palindrome.")

