# Exercise: Merge Sorted Arrays
def merge_sort(arr1, arr2):
    a, b = 0, 0
    merged_array = []
    
    while a < len(arr1) and b < len(arr2):
        if arr1[a] < arr2[b]:
            merged_array.append(arr1[a])
            a = a+1
        else:
            merged_array.append(arr2[b])
            b = b+1
    
    while a < len(arr1):
        merged_array.append(arr1[a])
        a = a+1
    
    while b < len(arr2):
        merged_array.append(arr2[b])
        b = b+1
    
    return merged_array

arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(merge_sort(arr1, arr2))

# Expected output: [1, 2, 3, 4, 5, 6]