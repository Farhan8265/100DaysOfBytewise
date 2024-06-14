# Exercise: Minimum Edit Distance
def min_operations(str1, str2):
    a, b = len(str1), len(str2)

    min_op = [[0] * (b + 1) for _ in range(a + 1)]
    
    for i in range(a + 1):
        min_op[i][0] = i
    for j in range(b + 1):
        min_op[0][j] = j
    
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            if str1[i - 1] == str2[j - 1]:
                min_op[i][j] = min_op[i - 1][j - 1]
            else:
                min_op[i][j] = 1 + min(min_op[i - 1][j], min_op[i][j - 1], min_op[i - 1][j - 1])    
    return min_op[a][b]

str1 = input("Enter the First String: ")
str2 = input("Enter the Second String: ")
min_ops = min_operations(str1, str2)
print("Minimum Number of Operations:", min_ops)
