# Exercise: Recursive Factorial
num = int (input ("Enter a Number: ") )
result = 1
for i in range (1, num + 1):
    result = result * i

print (f"The Factorial of {num} is {result}")
