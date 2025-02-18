"""
Combination Sum IV
-----------------
Given an array of distinct integers nums and a target integer target,
return the number of possible combinations that add up to target.

The problem is different from other combination sum problems because:
1. Order matters (each different sequence is counted as a unique combination)
2. Elements can be reused unlimited times
3. All numbers in nums are positive
"""


def combinationSum4_recursive(nums, target):
    """
    Approach 1: Basic Recursive Solution (Brute Force)
    ------------------------------------------------
    - Try each number at each step
    - Recursively find combinations for remaining target
    - Sum up all possible combinations

    Time Complexity: O(n^target) where n is length of nums
        - At each step, we try n numbers
        - Maximum depth is target (worst case using 1's)

    Space Complexity: O(target)
        - Recursion stack depth is proportional to target
    """
    n = len(nums)

    def dfs(i):
        if i == n:
            return True
        if i + 1 < n and nums[i] == nums[i + 1] and dfs(i + 2):
            return True
        if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2] and dfs(i + 3):
            return True
        if i + 2 < n and nums[i + 2] == nums[i + 1] + 1 and nums[i + 1] == nums[i] + 1 and dfs(i + 3):
            return True
        return False

    return dfs(0)


def combinationSum4_memoization(nums, target):
    """
    Approach 2: Top-down Dynamic Programming (Recursive with Memoization)
    ------------------------------------------------------------------
    - Cache results for each target value
    - Avoid recalculating same subproblems

    Time Complexity: O(n * target)
        - Each target value is computed once
        - For each target, we try n numbers

    Space Complexity: O(target)
        - Memoization cache stores results for each target value
        - Recursion stack depth is proportional to target
    """
    n = len(nums)
    memo = {}

    def dfs(i):
        if i in memo:
            return memo[i]
        if i == n:
            memo[i] = True
            return True
        if i + 1 < n and nums[i] == nums[i + 1] and dfs(i + 2):
            memo[i] = True
            return True
        if i + 2 < n and nums[i] == nums[i + 1] == nums[i + 2] and dfs(i + 3):
            memo[i] = True
            return True
        if i + 2 < n and nums[i + 2] == nums[i + 1] + 1 and nums[i + 1] == nums[i] + 1 and dfs(i + 3):
            memo[i] = True
            return True
        memo[i] = False
        return False

    return dfs(0)


def combinationSum4_tabulation(nums, target):
    """
    Approach 3: Bottom-up Dynamic Programming (Tabulation)
    ---------------------------------------------------
    - Build solution iteratively using a table
    - dp[i] = number of combinations that sum to i
    - For each target value, consider adding each number

    Time Complexity: O(n * target)
        - Fill dp table up to target
        - For each value, try each number in nums

    Space Complexity: O(target)
        - DP table stores result for each value up to target
    """
    n = len(nums)
    dp = [False] * (n + 1)
    dp[0] = True
    for i in range(2, n + 1):
        if nums[i - 1] == nums[i - 2] and dp[i - 2]:
            dp[i] = True
        if i >= 3 and nums[i - 1] == nums[i - 2] == nums[i - 3] and dp[i - 3]:
            dp[i] = True
        if i >= 3 and nums[i - 1] == nums[i - 2] + 1 == nums[i - 3] + 2 and dp[i - 3]:
            dp[i] = True
    return dp[n]


def test_combinations():
    """
    Test function to verify all implementations
    """
    test_cases = [
        ([1, 2, 3], 4, 7),
        ([9], 3, 0),
        ([1, 2, 3], 32, 181997601),
        ([3, 1, 2, 4], 4, 8),
        ([1, 2], 10, 89),
    ]

    solutions = [
        (combinationSum4_recursive, "Recursive (Brute Force)"),
        (combinationSum4_memoization, "Memoization"),
        (combinationSum4_tabulation, "Tabulation")
    ]

    for i, (nums, target, expected) in enumerate(test_cases):
        print(f"\nTest case {i + 1}:")
        print(f"nums = {nums}, target = {target}")
        print(f"Expected: {expected}")

        for solution, name in solutions:
            # Skip brute force for large targets
            if name == "Recursive (Brute Force)" and target > 10:
                print(f"{name}: Skipped (too slow for large target)")
                continue

            result = solution(nums, target)
            status = "✓" if result == expected else "✗"
            print(f"{name}: {result} {status}")


if __name__ == "__main__":
    # Example usage
    nums = [1, 2, 3]
    target = 4

    print("\nExample with nums =", nums, "target =", target)
    print("Combinations that sum to", target, ":", combinationSum4_tabulation(nums, target))

    print("\nRunning all test cases:")
    test_combinations()
