"""
Problem: Minimum Number of Increments on Subarrays to Form a Target Array

Given an array target, you need to find the minimum number of operations to form
this target array from an initially all-zero array. In each operation, you can
choose any subarray and increment all its elements by 1.

Example:
- Input: target = [1,2,3,2,1]
- Output: 3
- Explanation: We need at least 3 operations to form the target array:
  1. Increment [0,0,0,0,0] to [1,1,1,1,1]
  2. Increment [0,1,2,1,0] to [1,2,3,2,1]
"""


# Approach 1: Brute Force (Simulation)
# Time Complexity: O(N * max(target)) where N is length of array and max(target) is the maximum value
# Space Complexity: O(N)
def minIncrementsBruteForce(target):
    n = len(target)
    arr = [0] * n
    res = 0
    while arr != target:
        start = -1
        for i in range(n):
            if arr[i] < target[i]:
                start = i
                break
        if start == -1:
            break
        end = start
        while end < n and arr[end] < target[end]:
            end += 1
        for i in range(start, end):
            arr[i] += 1
        res += 1
    return res


# Approach 2: Greedy Approach
# Time Complexity: O(N)
# Space Complexity: O(1)
def minIncrementsGreedy(target):
    operations = target[0]
    for i in range(1, len(target)):
        if target[i] > target[i - 1]:
            operations += target[i] - target[i - 1]
    return operations


# Approach 3: Mathematical Insight (Most Optimized)
# Time Complexity: O(N)
# Space Complexity: O(1)
def minIncrements(target):
    """
    Insight: The number of operations needed equals the sum of all positive differences
    between adjacent elements plus the first element.

    Explanation:
    1. We need target[0] operations to reach the first element's value
    2. For each position i, if target[i] > target[i-1], we need (target[i] - target[i-1])
       additional operations to reach that height
    """
    if not target:
        return 0

    result = target[0]
    for i in range(1, len(target)):
        # Only count positive differences
        result += max(0, target[i] - target[i - 1])

    return result


# Testing with examples
def test_algorithms():
    test_cases = [
        [1, 2, 3, 2, 1],  # Expected: 3
        [3, 1, 5, 4, 2],  # Expected: 7
        [1, 1, 1, 1],  # Expected: 1
        [1, 2, 3, 4, 5],  # Expected: 5
        [5, 4, 3, 2, 1]  # Expected: 5
    ]

    for tc in test_cases:
        brute_result = minIncrementsBruteForce(tc)
        greedy_result = minIncrementsGreedy(tc)
        optimized_result = minIncrements(tc)

        print(f"Target: {tc}")
        print(f"Brute Force: {brute_result}")
        print(f"Greedy: {greedy_result}")
        print(f"Optimized: {optimized_result}")
        print("All approaches match:", brute_result == greedy_result == optimized_result)
        print("-" * 40)


# Additional explanation of the optimal solution:
"""
Optimal Solution Explanation:

The key insight is understanding what each operation actually means. When we increment
a subarray, we're essentially adding a "layer" to a part of our array.

Consider target = [1,2,3,2,1]:

Starting from all zeros [0,0,0,0,0]:
1. First layer: [1,1,1,1,1] → adds target[0] operations (1)
2. For position 1, we need to add (target[1] - target[0]) = 1 more layer
3. For position 2, we need to add (target[2] - target[1]) = 1 more layer
4. For position 3, we need to add (target[3] - target[2]) = 0 more layers (it's smaller)
5. For position 4, we need to add (target[4] - target[3]) = 0 more layers (it's smaller)

Total operations = 1 + 1 + 1 + 0 + 0 = 3

This works because:
- We always need target[0] operations to reach the first element
- When target[i] > target[i-1], we need (target[i] - target[i-1]) additional operations
- When target[i] ≤ target[i-1], we need 0 additional operations (we can reuse layers)
"""

if __name__ == "__main__":
    test_algorithms()