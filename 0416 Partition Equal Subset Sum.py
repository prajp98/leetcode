# Solution 1: Brute Force (Recursive)
# Time Complexity: O(2^n) where n is the length of nums
# Space Complexity: O(n) for recursion stack
def canPartition_brute(nums: list[int]) -> bool:
    n = len(nums)
    total = sum(nums)
    if total % 2:
        return False
    target = total / 2

    def dfs(i, curSum):
        if curSum == target:
            return True
        if curSum > target or i == n:
            return False
        # exclude
        exclude = dfs(i + 1, curSum)
        # include
        include = dfs(i + 1, curSum + nums[i])
        return include or exclude

    return dfs(0, 0)

# Solution 2: Dynamic Programming (Top-down with Memoization)
# Time Complexity: O(n * target) where n is length of nums, target is sum(nums)//2
# Space Complexity: O(n * target) for memo dictionary
def canPartition_memo(nums: list[int]) -> bool:
    n = len(nums)
    total = sum(nums)
    if total % 2:
        return False
    target = total / 2
    memo = {}

    def dfs(i, curSum):
        if (i, curSum) in memo:
            return memo[(i, curSum)]
        if curSum == target:
            return True
        if curSum > target or i == n:
            return False
        # exclude
        exclude = dfs(i + 1, curSum)
        # include
        include = dfs(i + 1, curSum + nums[i])
        memo[(i, curSum)] = include or exclude
        return memo[(i, curSum)]

    return dfs(0, 0)


# Solution 3: Dynamic Programming (Bottom-up)
# Time Complexity: O(n * target) where n is length of nums, target is sum(nums)//2
# Space Complexity: O(target) for dp array
def canPartition_2d(self, nums: list[int]) -> bool:
    n=len(nums)
    total=sum(nums)
    if total%2:
        return False
    target=total//2
    #dp[i][j] = True → We can make sum j using the first i elements.
    dp=[[False]*(target+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0]=True
    for i in range(1,n+1):
        for j in range(1,target+1):
            if j<nums[i-1]:
                dp[i][j]=dp[i-1][j]
            else:
                dp[i][j]=dp[i-1][j] or dp[i-1][j-nums[i-1]]
    return dp[-1][-1]
def canPartition_dp(nums: list[int]) -> bool:
    n = len(nums)
    total = sum(nums)
    if total % 2:
        return False
    target = total // 2
    dp = [False] * (target + 1)
    dp[0] = True
    for num in nums:
        for j in range(target, num - 1, -1):
            dp[j] = dp[j] or dp[j - num]
    return dp[-1]



# Example inputs and outputs
nums1 = [1, 5, 11, 5]
print(f"Input: nums = {nums1}")
print(f"Output: {canPartition_brute(nums1)}")  # True

nums2 = [1, 2, 3, 5]
print(f"Input: nums = {nums2}")
print(f"Output: {canPartition_memo(nums2)}")  # False

nums3 = [1, 2, 5]
print(f"Input: nums = {nums3}")
print(f"Output: {canPartition_dp(nums3)}")  # False
