# Solution 1: Brute Force (Recursive)
# Time Complexity: O(2^n) where n is length of nums
# Space Complexity: O(n) for recursion stack
def deleteAndEarn_brute(nums: list[int]) -> int:
    points = defaultdict(int)
    maxi = 0
    for num in nums:
        points[num] += num
        maxi = max(maxi, num)

    def dfs(num):
        if num == 0:
            return 0
        if num == 1:
            return points[1]
        return max(dfs(num - 1), points[num] + dfs(num - 2))

    return dfs(maxi)


# Solution 2: Top-down DP with Counter
# Time Complexity: O(n) where n is max number in nums
# Space Complexity: O(n) for memo array
def deleteAndEarn_topdown(nums: list[int]) -> int:
    points = defaultdict(int)
    maxi = 0
    memo = {}
    for num in nums:
        points[num] += num
        maxi = max(maxi, num)

    def dfs(num):
        if num in memo:
            return memo[num]
        if num == 0:
            return 0
        if num == 1:
            return points[1]
        memo[num] = max(dfs(num - 1), points[num] + dfs(num - 2))
        return memo[num]

    return dfs(maxi)


# Solution 3: Bottom-up DP
# Time Complexity: O(n) where n is max number in nums
# Space Complexity: O(n)
def deleteAndEarn_bottomup(nums: list[int]) -> int:
    if not nums:
        return 0

    # Convert array into sum of values
    max_num = max(nums)
    points = defaultdict(int)
    for num in nums:
        points[num] += num

    # DP array to store maximum points at each number
    dp = [0] * (max_num + 1)
    dp[1] = points[1]

    # For each number, we can either:
    # 1. Take it and the best from 2 numbers before
    # 2. Skip it and take the best from previous number
    for i in range(2, max_num + 1):
        dp[i] = max(dp[i - 1], dp[i - 2] + points[i])

    return dp[max_num]


# Solution 4: Space Optimized Bottom-up DP
# Time Complexity: O(n) where n is max number in nums
# Space Complexity: O(1)
def deleteAndEarn_optimized(nums: list[int]) -> int:
    if not nums:
        return 0

    # Convert array into sum of values
    max_num = max(nums)
    points = [0] * (max_num + 1)
    for num in nums:
        points[num] += num

    # Only need to keep track of two previous values
    two_back = 0
    one_back = points[1]

    for i in range(2, max_num + 1):
        # Current is max of:
        # 1. Taking current number + two steps back
        # 2. Skipping current number (keeping one step back)
        current = max(one_back, two_back + points[i])
        two_back = one_back
        one_back = current

    return one_back


# Example inputs and outputs
nums1 = [3, 4, 2]
print(f"Input: nums = {nums1}")
print(f"Output: {deleteAndEarn_optimized(nums1)}")  # 6

nums2 = [2, 2, 3, 3, 3, 4]
print(f"Input: nums = {nums2}")
print(f"Output: {deleteAndEarn_optimized(nums2)}")  # 9