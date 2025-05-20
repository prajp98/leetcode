def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        for j in range(i + 1, len(nums)):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue
            l, r = j + 1, len(nums) - 1

            while l < r:
                sumTotal = nums[i] + nums[j] + nums[l] + nums[r]
                if sumTotal < target:
                    l += 1
                elif sumTotal > target:
                    r -= 1
                else:
                    quad = [nums[i], nums[j], nums[l], nums[r]]
                    res.append(quad)
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
    return res