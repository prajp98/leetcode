def recursion(W, wt, val, i):
    if i == 0 or W == 0:
        return 0
    if wt[i-1] > W:
        return recursion(W, wt, val, i - 1)
    else:
        return max(val[i-1] + recursion(W - wt[i - 1], wt, val, i - 1),
                   recursion(W, wt, val, i - 1))


def knapsack(W, wt, val, n):
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(W + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif wt[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(val[i - 1] + dp[i - 1][j - wt[i - 1]],
                               dp[i - 1][j])
    return dp[n][W]


if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    capacity = 50
    n = len(profit)
    print("Recursion:")
    print(recursion(capacity, weight, profit, n))
    print("2D DP:")
    print(knapsack(capacity, weight, profit, n))
