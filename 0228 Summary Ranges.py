def summaryRanges(self, nums: List[int]) -> List[str]:
    i = 0
    res = []
    j = 0
    while i < (len(nums)):
        s = nums[i]
        while i < len(nums) - 1 and nums[i + 1] - nums[i] == 1:
            i += 1
        if s == nums[i]:
            res.append(str(s))
        else:
            res.append(str(s) + "->" + str(nums[i]))
        i += 1
    return res