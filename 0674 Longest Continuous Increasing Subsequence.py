def findLengthOfLCIS(self, nums: List[int]) -> int:
    if not nums:
        return 0
    maxi = 1
    curr = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            curr += 1
            maxi = max(maxi, curr)
        else:
            curr = 1
    return maxi