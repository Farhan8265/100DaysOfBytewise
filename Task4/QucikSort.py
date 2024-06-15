# Exercise: QuickSort Algorithm
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        element = arr[0]
        left = []
        middle = []
        right = []
        
        for x in arr:
            if x < element:
                left.append(x)
            elif x == element:
                middle.append(x)
            else:
                right.append(x)
        return quicksort(left) + middle + quicksort(right)

input_array = input("Enter Array Elements (separated by space): ").split()
input_array = [int(x) for x in input_array]
sorted_array = quicksort(input_array)
print("Sorted Array:", sorted_array)
