"""
Minimum Cost For Tickets
-----------------------
Given an array of days (in ascending order) where you want to travel,
and an array of costs for 1-day, 7-day, and 30-day passes.
Return the minimum cost to cover all travel days.

Example:
days = [1,4,6,7,8,20]
costs = [2,7,15]  # 1-day, 7-day, 30-day pass costs
"""


def minCostTickets_recursive(days, costs):
    """
    Approach 1: Recursive Solution (Brute Force)
    ------------------------------------------
    - For each day, try all three pass options
    - Recursively find minimum cost for remaining days

    Time Complexity: O(3^n) where n is number of days
        - Three choices for each day
        - Exponential due to overlapping subproblems

    Space Complexity: O(n) for recursion stack
    """

    n = len(days)

    def dfs(i):
        if i >= n:
            return 0
        # 1day
        cost1 = costs[0] + dfs(i + 1)
        # 7days
        j = i
        while j < n and days[j] < days[i] + 7:
            j += 1
        cost7 = costs[1] + dfs(j)
        # 30days
        j = i
        while j < n and days[j] < days[i] + 30:
            j += 1
        cost30 = costs[2] + dfs(j)
        return min(cost1, cost7, cost30)

    return dfs(0)


def minCostTickets_memoization(days, costs):
    """
    Approach 2: Top-down Dynamic Programming (Memoization)
    ---------------------------------------------------
    - Cache results for each starting index
    - Avoid recalculating same subproblems

    Time Complexity: O(n) where n is number of days
        - Each index computed once
        - Constant work for each pass option

    Space Complexity: O(n) for memo cache
    """
    n = len(days)
    memo = {}

    def dfs(i):
        if i == memo:
            return memo[i]
        if i >= n:
            return 0
        # 1day
        cost1 = costs[0] + dfs(i + 1)
        # 7days
        j = i
        while j < n and days[j] < days[i] + 7:
            j += 1
        cost7 = costs[1] + dfs(j)
        # 30days
        j = i
        while j < n and days[j] < days[i] + 30:
            j += 1
        cost30 = costs[2] + dfs(j)
        memo[i] = min(cost1, cost7, cost30)
        return memo[i]

    return dfs(0)


def minCostTickets_dp(days, costs):
    """
    Approach 3: Bottom-up Dynamic Programming
    ---------------------------------------
    - dp[i] = minimum cost to cover days[i:]
    - For each day, try all three pass options

    Time Complexity: O(n) where n is number of days
        - Single pass through days array
        - Constant work for each pass type

    Space Complexity: O(n) for dp array
    """
    n = days[-1]
    dp = [0] * (n + 1)
    days = set(days)
    for i in range(1, n + 1):
        if i not in days:
            dp[i] = dp[i - 1]
        else:
            dp[i] = min(
                dp[max(0, i - 1)] + costs[0],  # 1-day pass
                dp[max(0, i - 7)] + costs[1],  # 7-day pass
                dp[max(0, i - 30)] + costs[2]  # 30-day pass
            )
    return dp[n]


def minCostTickets_optimized(days, costs):
    """
    Approach 4: Window-based Dynamic Programming
    -----------------------------------------
    - Keep track of minimum cost for last 30 days
    - Use rolling window to optimize space

    Time Complexity: O(n) where n is number of days
        - Single pass through days
        - Constant work for each day

    Space Complexity: O(1)
        - Fixed size window of 30 days
    """
    dp = [0] * 31  # window of 31 days
    days_set = set(days)  # for O(1) lookup
    last_day = days[-1]

    for day in range(days[0], last_day + 1):
        if day not in days_set:
            dp[day % 31] = dp[(day - 1) % 31]
        else:
            dp[day % 31] = min(
                dp[(day - 1) % 31] + costs[0],  # 1-day pass
                dp[max(0, day - 7) % 31] + costs[1],  # 7-day pass
                dp[max(0, day - 30) % 31] + costs[2]  # 30-day pass
            )

    return dp[last_day % 31]


def test_min_cost_tickets():
    """
    Test function to verify all implementations
    """
    test_cases = [
        ([1, 4, 6, 7, 8, 20], [2, 7, 15], 11),
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31], [2, 7, 15], 17),
        ([1, 4, 6, 7, 8, 20], [7, 2, 15], 6),
        ([1], [2, 7, 15], 2),
        ([1, 2, 3, 4, 5], [2, 7, 15], 7),
    ]

    solutions = [
        (minCostTickets_recursive, "Recursive"),
        (minCostTickets_memoization, "Memoization"),
        (minCostTickets_dp, "DP"),
        (minCostTickets_optimized, "Optimized")
    ]

    for i, (days, costs, expected) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print(f"Days: {days}")
        print(f"Costs: {costs}")
        print(f"Expected: {expected}")

        for solution, name in solutions:
            # Skip recursive for large inputs
            if name == "Recursive" and len(days) > 10:
                print(f"{name}: Skipped (too slow for large input)")
                continue

            result = solution(days, costs)
            status = "✓" if result == expected else "✗"
            print(f"{name}: {result} {status}")


if __name__ == "__main__":
    # Example usage
    days = [1, 4, 6, 7, 8, 20]
    costs = [2, 7, 15]  # 1-day, 7-day, 30-day pass costs

    print(f"\nMinimum cost to cover days {days}:")
    print(f"Using optimized solution: {minCostTickets_optimized(days, costs)}")

    print("\nRunning all test cases:")
    test_min_cost_tickets()