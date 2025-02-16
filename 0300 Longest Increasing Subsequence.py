# Solution 1: Brute Force (Recursive)
# Time Complexity: O(2^n) as each element has two choices (include/exclude)
# Space Complexity: O(n) for recursion stack
from bisect import bisect


def lengthOfLIS_brute(nums: list[int]) -> int:
    n=len(nums)
    def dfs(prev,i):
        if i==n:
            return 0
        #exclude this num
        exclude=dfs(prev,i+1)
        #include this num
        include=0
        if nums[i]>prev:
            include=1+dfs(nums[i],i+1)
        return max(exclude, include)
    return dfs(float('-inf'),0)


# Solution 2: Dynamic Programming O(n²)
# Time Complexity: O(n²) where n is the length of nums
# Space Complexity: O(n) for the dp array
def lengthOfLIS_dp(nums: list[int]) -> int:
    n = len(nums)
    dp = [1] * n
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)


# Solution 3: Binary Search with Patience Sort concept
# Time Complexity: O(n log n) where n is the length of nums
# Space Complexity: O(n) for the tails array
def lengthOfLIS_binary(nums: list[int]) -> int:
    sub = []

    for num in nums:
        i = bisect.bisect_left(sub, num)  # Find the first element >= num
        if i == len(sub):
            sub.append(num)  # Append if num is the largest so far
        else:
            sub[i] = num  # Replace to keep subsequence minimal

    return len(sub)


# Example inputs and outputs
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
print(f"Input: nums = {nums1}")
print(f"Output (Brute Force): {lengthOfLIS_brute(nums1)}")  # 4
print(f"Output (DP): {lengthOfLIS_dp(nums1)}")  # 4
print(f"Output (Binary Search): {lengthOfLIS_binary(nums1)}")  # 4

nums2 = [0, 1, 0, 3, 2, 3]
print(f"\nInput: nums = {nums2}")
print(f"Output (Brute Force): {lengthOfLIS_brute(nums2)}")  # 4
print(f"Output (DP): {lengthOfLIS_dp(nums2)}")  # 4
print(f"Output (Binary Search): {lengthOfLIS_binary(nums2)}")  # 4

nums3 = [7, 7, 7, 7, 7, 7, 7]
print(f"\nInput: nums = {nums3}")
print(f"Output (Brute Force): {lengthOfLIS_brute(nums3)}")  # 1
print(f"Output (DP): {lengthOfLIS_dp(nums3)}")  # 1
print(f"Output (Binary Search): {lengthOfLIS_binary(nums3)}")  # 1