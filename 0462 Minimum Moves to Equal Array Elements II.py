def minMoves2(self, nums: List[int]) -> int:
    nums.sort()
    l, r = 0, len(nums) - 1
    total = 0
    while l < r:
        total += nums[r] - nums[l]
        l += 1
        r -= 1
    return total