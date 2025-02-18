"""
Integer Break
------------
Given an integer n, break it into the sum of k positive integers, where k >= 2,
and maximize the product of those integers.
Return the maximum product you can get.

Example:
n = 10
Output = 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36
"""


def integerBreak_recursive(n):
    """
    Approach 1: Recursive Solution (Brute Force)
    ------------------------------------------
    - Try all possible ways to break number
    - For each break point, recursively solve subproblems

    Time Complexity: O(n^n)
        - Each number can be broken n-1 ways
        - Tree height could be n

    Space Complexity: O(n) for recursion stack
    """

    if n == 2:
        return 1
    if n == 3:
        return 2

    def dfs(n):
        if n == 1:
            return 1
        maxi = 0
        for i in range(1, n):
            maxi = max(maxi, i * (n - i), i * dfs(n - i))
        return maxi

    return dfs(n)

def integerBreak_memoization(n):
    """
    Approach 2: Top-down Dynamic Programming (Memoization)
    ---------------------------------------------------
    - Cache results for each number
    - Avoid recalculating same subproblems

    Time Complexity: O(n^2)
        - Each number computed once
        - For each number, try n-1 break points

    Space Complexity: O(n) for memo cache
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    memo = {}

    def dfs(num):
        if num in memo:
            return memo[num]
        if num == 1:
            return 1
        maxi = 0
        for i in range(1, num):
            maxi = max(maxi, i * (num - i), i * dfs(num - i))
        memo[num] = maxi
        return maxi

    return dfs(n)

def integerBreak_dp(n):
    """
    Approach 3: Bottom-up Dynamic Programming
    ---------------------------------------
    - dp[i] = maximum product possible by breaking number i
    - Build solution iteratively

    Time Complexity: O(n^2)
        - Fill dp array up to n
        - For each number, try n-1 break points

    Space Complexity: O(n) for dp array
    """
    if n == 2:
        return 1
    if n == 3:
        return 2
    dp = [0] * (n + 1)
    dp[2] = 1
    for i in range(3, n + 1):
        for j in range(1, i):
            dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
    return dp[n]


def integerBreak_math(n):
    """
    Approach 4: Mathematical Solution
    ------------------------------
    - Based on mathematical observation
    - Optimal break is to use as many 3's as possible
    - Use 2's only when necessary

    Time Complexity: O(1)
        - Constant time calculation

    Space Complexity: O(1)
        - No extra space needed
    """
    if n <= 1:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    # For n > 3, try to break into 3's
    quotient = n // 3
    remainder = n % 3

    if remainder == 0:
        return 3 ** quotient
    if remainder == 1:
        return 3 ** (quotient - 1) * 4
    return 3 ** quotient * 2


def test_integer_break():
    """
    Test function to verify all implementations
    """
    test_cases = [
        (2, 1),
        (3, 2),
        (4, 4),
        (10, 36),
        (15, 243),
    ]

    solutions = [
        (integerBreak_recursive, "Recursive"),
        (integerBreak_memoization, "Memoization"),
        (integerBreak_dp, "DP"),
        (integerBreak_math, "Mathematical")
    ]

    for i, (n, expected) in enumerate(test_cases):
        print(f"\nTest case {i + 1}: n = {n}")
        print(f"Expected: {expected}")

        for solution, name in solutions:
            # Skip recursive for large inputs
            if name == "Recursive" and n > 10:
                print(f"{name}: Skipped (too slow for large input)")
                continue

            result = solution(n)
            status = "✓" if result == expected else "✗"
            print(f"{name}: {result} {status}")


if __name__ == "__main__":
    n = 10
    print(f"\nMaximum product for n = {n}:")
    print(f"Using mathematical solution: {integerBreak_math(n)}")

    print("\nRunning all test cases:")
    test_integer_break()