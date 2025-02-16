#Recursion T:O(2^n) S:O(n)
def rob(self, nums: List[int]) -> int:
    n = len(nums)
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]

    def recursion(arr, i):
        if i >= len(arr):
            return 0
        return max(recursion(arr, i + 1), recursion(arr, i + 2) + arr[i])

    return max(recursion(nums[1:], 0), recursion(nums[:-1], 0))

#Memoization T:O(n) S:O(n)
def rob(self, nums: List[int]) -> int:
    n=len(nums)
    if not nums:
        return 0
    if len(nums)==1:
        return nums[0]
    def recursion(arr,i,memo):
        if i >= len(arr):
            return 0
        if i in memo:
            return memo[i]
        memo[i]=max(recursion(arr,i + 1,memo), recursion(arr,i + 2,memo) + arr[i])
        return memo[i]
    return max(recursion(nums[1:],0,{}),recursion(nums[:-1],0,{}))

#DP Bottom up O(n) O(n)
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    def helper(arr):
        if not arr:
            return 0
        n = len(arr)
        dp = [0]*(n + 1)
        dp[n] = 0
        dp[n-1] = arr[n-1]
        for i in range(n-2,-1,-1):
            dp[i] = max(arr[i] + dp[i + 2], dp[i + 1])
        return dp[0]
    return max(helper(nums[:-1]), helper(nums[1:]))

#Space DP O(n) O(1)
def rob(self, nums: List[int]) -> int:
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    def helper(arr):
        rob1, rob2 = 0, 0
        for num in arr:
            temp = max(num + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
    return max(helper(nums[:-1]), helper(nums[1:]))