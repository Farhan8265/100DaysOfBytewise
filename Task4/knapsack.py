# Exercise: Knapsack Problem
def knapsack(weight, value, max_capacity):
    n = len(weight)
    dp = [[0 for x in range(max_capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(max_capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weight[i - 1] <= w:
                dp[i][w] = max(value[i - 1] + dp[i - 1][w - weight[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    return dp[n][max_capacity]

weight = list(map(int, input("Enter the Weights (separated by space): ").split()))
value = list(map(int, input("Enter the Values (separated by space): ").split()))
max_capacity = int(input("Enter the maximum capacity of the Knapsack: "))
max_value = knapsack(weight, value, max_capacity)

print("The maximum value that can be put in the Knapsack is: ", max_value)
