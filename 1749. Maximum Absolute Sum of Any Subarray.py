"""
Problem: Maximum Absolute Sum of Any Subarray

Given an array of integers nums, find the maximum absolute sum of any subarray of nums.

A subarray is a contiguous non-empty sequence of elements within an array.
The absolute sum of a subarray [nums[l], nums[l+1], ..., nums[r-1], nums[r]] is |nums[l] + nums[l+1] + ... + nums[r-1] + nums[r]|.

Example:
Input: nums = [1,-3,2,3,-4]
Output: 5
Explanation: The subarray [2,3] has absolute sum = |2+3| = 5.
"""


# Solution 1: Brute Force Approach
# Time Complexity: O(n³) - Three nested loops
# Space Complexity: O(1) - Constant extra space
def maxAbsoluteSum_brute_force(nums):
    n = len(nums)
    max_abs_sum = 0

    for i in range(n):
        for j in range(i, n):
            # Calculate sum of subarray nums[i...j]
            current_sum = 0
            for k in range(i, j + 1):
                current_sum += nums[k]

            # Update max_abs_sum if current absolute sum is larger
            max_abs_sum = max(max_abs_sum, abs(current_sum))

    return max_abs_sum


# Solution 2: Improved Brute Force
# Time Complexity: O(n²) - Two nested loops
# Space Complexity: O(1) - Constant extra space
def maxAbsoluteSum_improved_brute_force(nums):
    res = 0
    n = len(nums)
    for i in range(n):
        curSum = 0
        for j in range(i, n):
            curSum += nums[j]
            res = max(res, abs(curSum))
    return res


# Solution 3: Kadane's Algorithm Adaptation
# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(1) - Constant extra space
def maxAbsoluteSum_kadane(nums):
    # We need to find both the maximum and minimum subarray sum
    # The maximum absolute sum will be max(max_sum, |min_sum|)

    max_sum = 0  # Maximum subarray sum
    min_sum = 0  # Minimum subarray sum
    current_max = 0
    current_min = 0

    for num in nums:
        # Update maximum subarray sum ending at current position
        current_max = max(current_max + num, num)
        max_sum = max(max_sum, current_max)

        # Update minimum subarray sum ending at current position
        current_min = min(current_min + num, num)
        min_sum = min(min_sum, current_min)

    return max(max_sum, abs(min_sum))


# Solution 4: Prefix Sum Approach
# Time Complexity: O(n) - Single pass to compute prefix sums + single pass to find min/max
# Space Complexity: O(n) - Extra space for the prefix sum array
def maxAbsoluteSum_prefix_sum(nums):
    n = len(nums)
    prefix_sum = [0] * (n + 1)

    # Compute prefix sums
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]

    # The maximum absolute subarray sum is the maximum difference
    # between any two prefix sums
    min_prefix = min(prefix_sum)
    max_prefix = max(prefix_sum)

    return max_prefix - min_prefix


# Solution 5: Optimized One-Pass Approach
# Time Complexity: O(n) - Single pass through the array
# Space Complexity: O(1) - Constant extra space
def maxAbsoluteSum_optimized(nums):
    max_prefix = min_prefix = current_sum = 0

    for num in nums:
        current_sum += num
        max_prefix = max(max_prefix, current_sum)
        min_prefix = min(min_prefix, current_sum)

    return max_prefix - min_prefix


# Test cases
test_cases = [
    [1, -3, 2, 3, -4],  # Expected: 5
    [2, -5, 1, -4, 3, -2],  # Expected: 8
    [-7, -1, -5, -4],  # Expected: 17
    [1, 2, 3, 4, 5]  # Expected: 15
]

for i, nums in enumerate(test_cases):
    print(f"Test Case {i + 1}: {nums}")
    print(f"Brute Force (O(n³)): {maxAbsoluteSum_brute_force(nums)}")
    print(f"Improved Brute Force (O(n²)): {maxAbsoluteSum_improved_brute_force(nums)}")
    print(f"Kadane's Algorithm (O(n)): {maxAbsoluteSum_kadane(nums)}")
    print(f"Prefix Sum (O(n)): {maxAbsoluteSum_prefix_sum(nums)}")
    print(f"Optimized One-Pass (O(n)): {maxAbsoluteSum_optimized(nums)}")
    print()