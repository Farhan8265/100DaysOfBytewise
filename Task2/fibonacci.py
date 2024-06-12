# Exercise: Nth Fibonacci Number
n = int (input ("Enter the position of Fibonacci Number: ") )
if n == 1:
    nth_fib = 1
elif n == 2:
    nth_fib = 2
else:
    a, b = 0, 1
    for i in range(n - 1):
        a, b = b, a + b
    nth_fib = b

if 10 <= n % 100 <= 20:
    suffix = "th"
else:
    suffix = {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

print(f"The {n}{suffix} Fibonacci Number is {nth_fib}.")
