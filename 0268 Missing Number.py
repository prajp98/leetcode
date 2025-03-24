def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    ans = 0
    for i in range(1, n + 1):
        ans ^= i
    for num in nums:
        ans ^= num
    return ans

def missingNumber(self, nums: List[int]) -> int:
    res=len(nums)
    for i in range(len(nums)):
        res += i - nums[i]
    return res

def missingNumber(self, nums: List[int]) -> int:
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum