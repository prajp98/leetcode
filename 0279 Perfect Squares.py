"""
Perfect Squares (279)
--------------------
Given an integer n, return the least number of perfect square numbers that sum to n.

Perfect square numbers are: 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, ...
"""


def numSquares_recursive(n):
    """
    Approach 1: Basic Recursive Solution (Brute Force)
    ------------------------------------------------
    - Try each perfect square number less than n
    - Recursively find minimum for remaining value

    Time Complexity: O(n^(h/2)) where h is height of recursion tree
        - At each step, we try sqrt(n) numbers
        - Tree height could be n in worst case (using all 1's)

    Space Complexity: O(n) - recursion stack depth
    """

    def dfs(num):
        if num == 0:
            return 0
        count = float('inf')
        i = 1
        while i * i <= num:
            count = min(count, 1 + dfs(num - i * i))
            i += 1
        return count

    return dfs(n)


def numSquares_memoization(n):
    """
    Approach 2: Top-down Dynamic Programming (Memoization)
    ---------------------------------------------------
    - Cache results for each value to avoid recalculation
    - Use recursion with memoization

    Time Complexity: O(n * sqrt(n))
        - We compute each value once
        - For each value, we try sqrt(n) perfect squares

    Space Complexity: O(n)
        - Memoization cache stores result for each value
        - Recursion stack depth is O(n)
    """
    memo = {}

    def dfs(num):
        if num in memo:
            return memo[num]
        if num == 0:
            return 0
        count = float('inf')
        i = 1
        while i * i <= num:
            count = min(count, 1 + dfs(num - i * i))
            i += 1
        memo[num] = count
        return count

    return dfs(n)


def numSquares_tabulation(n):
    """
    Approach 3: Bottom-up Dynamic Programming (Tabulation)
    ---------------------------------------------------
    - Build solution iteratively using array
    - dp[i] = least number of perfect squares that sum to i

    Time Complexity: O(n * sqrt(n))
        - Fill dp array up to n
        - For each value, try sqrt(n) perfect squares

    Space Complexity: O(n)
        - DP array stores result for each value up to n
    """
    # Initialize dp array
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        j = 1
        while j * j <= i:
            dp[i] = min(dp[i], 1 + dp[i - j * j])
            j += 1
    return dp[n]


def numSquares_math(n):
    """
    Approach 4: Mathematical Solution (Lagrange's Four Square Theorem)
    ---------------------------------------------------------------
    - Based on mathematical properties of perfect squares
    - Uses Lagrange's four-square theorem
    - Any natural number can be represented as sum of at most 4 square numbers

    Time Complexity: O(sqrt(n))
        - Check if n is perfect square: O(1)
        - Check sum of two squares: O(sqrt(n))
        - Check sum of three squares: O(sqrt(n))

    Space Complexity: O(1)
        - Only uses constant extra space
    """

    def isSquare(n):
        sq = int(n ** 0.5)
        return sq * sq == n

    # Check if n is perfect square
    if isSquare(n):
        return 1

    # Check if n is sum of two squares
    for i in range(1, int(n ** 0.5) + 1):
        if isSquare(n - i * i):
            return 2

    # Check if n = 4^k(8m+7)
    while n % 4 == 0:
        n //= 4
    if n % 8 == 7:
        return 4

    # n must be sum of three squares
    return 3


def test_perfect_squares():
    """
    Test function to verify all implementations
    """
    test_cases = [
        (1, 1),
        (12, 3),  # 4 + 4 + 4
        (13, 2),  # 4 + 9
        (16, 1),  # 16
        (43, 3),  # 36 + 4 + 3
    ]

    solutions = [
        (numSquares_recursive, "Recursive (Brute Force)"),
        (numSquares_memoization, "Memoization"),
        (numSquares_tabulation, "Tabulation"),
        (numSquares_math, "Mathematical")
    ]

    for i, (n, expected) in enumerate(test_cases):
        print(f"\nTest case {i + 1}: n = {n}")
        print(f"Expected: {expected}")

        for solution, name in solutions:
            # Skip brute force for larger numbers
            if name == "Recursive (Brute Force)" and n > 20:
                print(f"{name}: Skipped (too slow for large n)")
                continue

            result = solution(n)
            status = "✓" if result == expected else "✗"
            print(f"{name}: {result} {status}")


if __name__ == "__main__":
    # Example usage
    n = 12
    print(f"\nLeast number of perfect squares summing to {n}:")
    print(f"Using DP: {numSquares_tabulation(n)}")
    print(f"Using Math: {numSquares_math(n)}")

    print("\nRunning all test cases:")
    test_perfect_squares()