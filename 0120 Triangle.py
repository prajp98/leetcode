# Solution 1: Brute Force (Recursive)
# Time Complexity: O(2^n) where n is number of rows
# Space Complexity: O(n) for recursion stack
def minimumTotal_brute(triangle: list[list[int]]) -> int:
    def dfs(r, c):
        if r == len(triangle):
            return 0
        return triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))

    return dfs(0, 0)


# Solution 2: Memoization (Top-down DP)
# Time Complexity: O(n²) where n is number of rows
# Space Complexity: O(n²) for memo dictionary
def minimumTotal_memo(triangle: list[list[int]]) -> int:
    memo = {}

    def dfs(r, c):
        if (r, c) in memo:
            return memo[(r, c)]
        if r == len(triangle):
            return 0
        memo[(r, c)] = triangle[r][c] + min(dfs(r + 1, c), dfs(r + 1, c + 1))
        return memo[(r, c)]

    return dfs(0, 0)


# Solution 3: Bottom-up DP (2D array)
# Time Complexity: O(n²)
# Space Complexity: O(n²)
def minimumTotal_dp_2d(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[n - 1][i] = triangle[n - 1][i]
    for r in range(n - 2, -1, -1):
        for c in range(r + 1):
            dp[r][c] = triangle[r][c] + min(dp[r + 1][c], dp[r + 1][c + 1])
    return dp[0][0]


# Solution 4: Bottom-up DP (1D array - Space Optimized)
# Time Complexity: O(n²)
# Space Complexity: O(n)
def minimumTotal_dp_1d(triangle: list[list[int]]) -> int:
    n = len(triangle)
    dp = [0] * n
    for i in range(n):
        dp[i] = triangle[n - 1][i]
    for r in range(n - 2, -1, -1):
        for c in range(r + 1):
            dp[c] = triangle[r][c] + min(dp[c], dp[c + 1])
    return dp[0]


# Example usage with explanation at each step
triangle1 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]

print("Example triangle:")
for row in triangle1:
    print(row)

print("\nBrute Force result:", minimumTotal_brute(triangle1))
print("Path: 2 -> 3 -> 5 -> 1 = 11")

print("\nMemoization result:", minimumTotal_memo(triangle1))
print("Same path, but faster with memoization")

print("\n2D DP result:", minimumTotal_dp_2d(triangle1))
print("Bottom-up approach, building minimum paths from bottom")

print("\n1D DP result:", minimumTotal_dp_1d(triangle1))
print("Space optimized, only keeping track of one row at a time")