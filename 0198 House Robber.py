#Recursion T:O(2^n) S:O(n)
def rob(self, nums: List[int]) -> int:
    def recursion(i):
        if i >= len(nums):
            return 0
        return max(nums[i] + recursion(nums, i + 2), recursion(nums, i + 1))
    return recursion(0)

#Memoization T:O(n) S:O(n)
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    memo = {}

    def rob(i):
        if i < 0:
            return 0
        if i in memo:
            return memo[i]
        memo[i] = max(rob(i - 1), rob(i - 2) + nums[i])
        return memo[i]

    return rob(n - 1)


#DP Bottom up O(n) O(n)
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    n = len(nums)
    dp = [0]*(n + 1)
    dp[n] = 0
    dp[n-1] = nums[n-1]
    for i in range(n-2,-1,-1):
        dp[i] = max(nums[i] + dp[i + 2], dp[i + 1])
    return dp[0]

#Space DP O(n) O(1)
def rob(self, nums: List[int]) -> int:
    rob1, rob2 = 0, 0
    for num in nums:
        temp = max(num + rob1, rob2)
        rob1 = rob2
        rob2 = temp
    return rob2