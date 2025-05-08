def dominantIndex(self, nums: List[int]) -> int:
    maxv = max(nums)
    maxi = nums.index(maxv)

    for i in range(len(nums)):
        if i != maxi and maxv < 2 * nums[i]:
            return -1
    return maxi