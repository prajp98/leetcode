def checkPossibility(self, nums: List[int]) -> bool:
    n = 0
    for i in range(1, len(nums)):
        if nums[i - 1] > nums[i]:
            if n == 1:
                return False
            n += 1
            if i < 2 or nums[i - 2] <= nums[i]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return True