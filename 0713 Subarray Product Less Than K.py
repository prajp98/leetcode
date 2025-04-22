def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
    if k <= 1:
        return 0
    product = 1
    l = 0
    res = 0
    for r in range(len(nums)):
        product *= nums[r]
        while product >= k:
            product //= nums[l]
            l += 1
        res += r - l + 1
    return res