"""
Check if There is a Valid Partition For The Array
-----------------------------------------------
Given an array nums, check if there exists a valid partition where each subset satisfies:
1. Exactly 2 equal elements, or
2. Exactly 3 equal elements, or
3. Exactly 3 consecutive increasing elements (difference of 1)

Return true if partition exists, false otherwise.
"""

def validPartition_recursive(nums):
    """
    Approach 1: Basic Recursive Solution (Brute Force)
    ------------------------------------------------
    - Try all possible partitioning options at each step
    - Check if any combination leads to valid partition

    Time Complexity: O(3^n)
        - At each step, we have up to 3 choices
        - Tree height could be n in worst case

    Space Complexity: O(n)
        - Recursion stack depth
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
def validPartition_memoization(nums):
    """
    Approach 2: Top-down Dynamic Programming (Memoization)
    ---------------------------------------------------
    - Cache results for each starting index
    - Avoid recalculating same subproblems

    Time Complexity: O(n)
        - Each index is computed once
        - Constant work for checking each partition

    Space Complexity: O(n)
        - Memoization cache stores result for each index
        - Recursion stack depth is O(n)
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

def validPartition_tabulation(nums):
    """
    Approach 3: Bottom-up Dynamic Programming (Tabulation)
    ---------------------------------------------------
    - Build solution iteratively using boolean array
    - dp[i] = whether valid partition exists for nums[0:i]

    Time Complexity: O(n)
        - Single pass through array
        - Constant work for checking each partition

    Space Complexity: O(n)
        - DP array stores result for each index
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

def validPartition_optimized(nums):
    """
    Approach 4: Space-Optimized Dynamic Programming
    --------------------------------------------
    - Only need last three states for dp
    - Use rolling array technique

    Time Complexity: O(n)
        - Single pass through array

    Space Complexity: O(1)
        - Only store three previous states
    """
    n = len(nums)
    if n < 2:
        return False

    # Keep track of last 3 states
    dp = [True, False, False, False]  # dp[0] is dummy value

    for i in range(2, n + 1):
        current = False

        # Check partition of size 2
        if i >= 2:
            current = current or (
                dp[(i-2) % 4] and nums[i-1] == nums[i-2]
            )

        # Check partition of size 3
        if i >= 3:
            current = current or (
                dp[(i-3) % 4] and (
                    nums[i-1] == nums[i-2] == nums[i-3] or
                    (nums[i-2] == nums[i-3] + 1 and
                     nums[i-1] == nums[i-2] + 1)
                )
            )

        dp[i % 4] = current

    return dp[n % 4]

def test_valid_partition():
    """
    Test function to verify all implementations
    """
    test_cases = [
        ([4,4,4,5,6], True),
        ([1,1,1,2], False),
        ([1,1], True),
        ([1,2], False),
        ([1,1,1,1,1], True),
        ([1,2,3,4], False),
        ([1,1,1,2,2,2], True),
    ]

    solutions = [
        (validPartition_recursive, "Recursive (Brute Force)"),
        (validPartition_memoization, "Memoization"),
        (validPartition_tabulation, "Tabulation"),
        (validPartition_optimized, "Space Optimized")
    ]

    for i, (nums, expected) in enumerate(test_cases):
        print(f"\nTest case {i + 1}: nums = {nums}")
        print(f"Expected: {expected}")

        for solution, name in solutions:
            # Skip brute force for larger arrays
            if name == "Recursive (Brute Force)" and len(nums) > 10:
                print(f"{name}: Skipped (too slow for large input)")
                continue

            result = solution(nums)
            status = "✓" if result == expected else "✗"
            print(f"{name}: {result} {status}")

if __name__ == "__main__":
    nums = [4,4,4,5,6]
    print(f"\nChecking valid partition for {nums}:")
    print(f"Using optimized DP: {validPartition_optimized(nums)}")

    print("\nRunning all test cases:")
    test_valid_partition()