"""
Paint House Problem
------------------
Given a list of costs where costs[i][j] represents the cost of painting house i with color j,
return the minimum cost to paint all houses such that no two adjacent houses have the same color.
Colors are represented as: 0 = Red, 1 = Green, 2 = Blue
"""


def minCost_bruteforce(costs):
    """
    Approach 1: Brute Force (Recursive without memoization)
    ------------------------------------------------------
    - Try all possible color combinations recursively
    - For each house, try all colors except the color used in previous house
    - Calculate total cost for each valid combination
    - Return minimum cost among all combinations

    Time Complexity: O(3^n)
        - For first house, we try 3 colors
        - For each subsequent house, we try 2 colors
        - Total combinations = 3 * 2^(n-1) ≈ O(3^n)

    Space Complexity: O(n)
        - Recursion stack depth is equal to number of houses
    """
    n = len(costs)
    if not costs:
        return 0
    def dfs(prev, i):
        if i >= n:
            return 0
        x = float('inf')
        for color in range(3):
            if prev != color:
                x = min(x, costs[i][color] + dfs(color, i + 1))
        return x

    return min(dfs(0, 0), dfs(1, 0), dfs(2, 0))


def minCost_memoization(costs):
    """
    Approach 2: Top-down Dynamic Programming (Recursive with memoization)
    ------------------------------------------------------------------
    - Same as brute force but cache results of subproblems
    - Use (house_index, previous_color) as cache key
    - Avoid recalculating same subproblems multiple times

    Time Complexity: O(n)
        - Each subproblem (house, color combination) is solved once
        - Total subproblems = n houses * 3 colors = O(n)

    Space Complexity: O(n)
        - Memoization cache stores at most n*3 entries
        - Recursion stack depth is n
    """
    if not costs:
        return 0

    n = len(costs)
    memo = {}

    def dfs(prev, i):
        if (prev, i) in memo:
            return memo[(prev, i)]
        if i >= n:
            return 0
        x = float('inf')
        for color in range(3):
            if prev != color:
                x = min(x, costs[i][color] + dfs(color, i + 1))
        memo[(prev, i)] = x
        return x

    return min(dfs(0, 0), dfs(1, 0), dfs(2, 0))


def minCost_tabulation(costs):
    """
    Approach 3: Bottom-up Dynamic Programming (Tabulation)
    ---------------------------------------------------
    - Build solution iteratively using a table
    - dp[i][j] = min cost to paint houses 0...i with house i painted color j
    - For each house and color, consider min cost from valid previous colors

    Time Complexity: O(n)
        - Single pass through all houses
        - Constant work for each house (trying 3 colors)

    Space Complexity: O(n)
        - DP table stores cost for each house-color combination
        - Total space = n houses * 3 colors = O(n)
    """
    if not costs:
        return 0

    n = len(costs)
    dp = [[0] * 3 for _ in range(n)]

    # Base case: The cost of painting the first house is itself
    dp[0] = costs[0]

    # Fill DP table
    for i in range(1, n):
        dp[i][0] = costs[i][0] + min(dp[i - 1][1], dp[i - 1][2])  # If Red, previous house should be Blue/Green
        dp[i][1] = costs[i][1] + min(dp[i - 1][0], dp[i - 1][2])  # If Blue, previous house should be Red/Green
        dp[i][2] = costs[i][2] + min(dp[i - 1][0], dp[i - 1][1])  # If Green, previous house should be Red/Blue

    # Return the minimum cost to paint all houses
    return min(dp[n - 1][0], dp[n - 1][1], dp[n - 1][2])


def minCost_optimized(costs):
    """
    Approach 4: Space-Optimized Dynamic Programming
    ---------------------------------------------
    - Observe that we only need previous house's costs
    - Instead of full DP table, keep track of just previous costs
    - Update costs in-place for current house

    Time Complexity: O(n)
        - Single pass through all houses
        - Constant work for each house

    Space Complexity: O(1)
        - Only store costs for previous house (3 variables)
        - No extra space scaling with input size
    """
    if not costs:
        return 0
    n = len(costs)
    dp = [0, 0, 0]
    for i in range(n):
        dp0 = costs[i][0] + min(dp[1], dp[2])
        dp1 = costs[i][1] + min(dp[0], dp[2])
        dp2 = costs[i][2] + min(dp[0], dp[1])
        dp = [dp0, dp1, dp2]
    return min(dp)


# Test function to verify all implementations
def test_paint_house():
    test_cases = [
        ([], 0),
        ([[17, 2, 17]], 2),
        ([[7, 6, 2]], 2),
        ([[17, 2, 17], [16, 16, 5], [14, 3, 19]], 10),
        ([[1, 5, 3], [2, 9, 4]], 5)
    ]

    solutions = [
        (minCost_bruteforce, "Brute Force"),
        (minCost_memoization, "Memoization"),
        (minCost_tabulation, "Tabulation"),
        (minCost_optimized, "Space Optimized")
    ]

    for i, (costs, expected) in enumerate(test_cases):
        print(f"\nTest case {i + 1}: {costs}")
        print(f"Expected: {expected}")

        for solution, name in solutions:
            result = solution(costs)
            status = "✓" if result == expected else "✗"
            print(f"{name}: {result} {status}")


if __name__ == "__main__":
    test_paint_house()