def arrayNesting(self, nums: List[int]) -> int:
    maxi = 0
    for i in range(len(nums)):
        if nums[i] != -1:
            count = 0
            while nums[i] != -1:
                nums[i], i = -1, nums[i]
                count += 1
            maxi = max(maxi, count)
    return maxi