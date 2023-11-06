def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(capacity + 1):
            if weights[i - 1] <= j:
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]
    
    selected_items = []
    i, j = n, capacity
    while i > 0 and j > 0:
        if dp[i][j] != dp[i - 1][j]:
            selected_items.append(i - 1)
            j -= weights[i - 1]
        i -= 1
    
    return dp[n][capacity], selected_items[::-1]

n = int(input("Enter the number of items: "))
value = []
weight =[]
for i in range(n):
    v,w = map(int, input(f"Enter value and weight for {i+1} space separated: ").split())
    value.append(v)
    weight.append(w)
capacity = int(input("Enter capacity: "))

max_value, selected_items = knapsack_dynamic_programming(value, weight, capacity)

print("Maximum value:", max_value)
print("Selected items:", selected_items)
