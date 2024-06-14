# Exercise: Maximum Subarray
def max_subarray(num):
    max_sum = float('-inf')
    current_sum = 0

    for i in num:
        current_sum = max(i, current_sum + i)
        max_sum = max(max_sum, current_sum)
    return max_sum

input_array = input("Enter the array (comma-separated integers): ")
input_array = [int(x) for x in input_array.split(',')]

max_sum = max_subarray(input_array)

print("Maximum Subarray Sum:", max_sum)
