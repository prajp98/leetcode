def threeSumClosest(self, nums: List[int], target: int) -> int:
    nums.sort()
    closest = float('inf')
    res = 0

    for i in range(len(nums) - 2):
        l, r = i + 1, len(nums) - 1

        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if abs(target - total) < closest:
                closest = abs(target - total)
                res = total
            if total < target:
                l += 1
            elif total > target:
                r -= 1
            else:
                return total
    return res