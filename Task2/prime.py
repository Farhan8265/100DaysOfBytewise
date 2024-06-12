# Exercise: Prime Number Checker
num = int (input ("Enter a Number: "))
is_prime = True

if num < 2:
    is_prime = False
else:
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(f"{num} is a Prime Number.")
else:
    print(f"{num} is not a Prime Number.")
    