def findDuplicates(self, nums: List[int]) -> List[int]:
    res = []
    n = len(nums)
    for i, num in enumerate(nums):
        if nums[abs(num) - 1] < 0:
            res.append(abs(num))
        nums[abs(num) - 1] *= -1
    return res