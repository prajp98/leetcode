def triangleNumber(self, nums: List[int]) -> int:
    nums.sort()
    res = 0
    n = len(nums)
    for i in range(n - 1, 1, -1):
        start = 0
        end = i - 1
        while start < end:
            if nums[start] + nums[end] > nums[i]:
                res += end - start
                end -= 1
            elif nums[start] + nums[end] <= nums[i]:
                start += 1
    return res