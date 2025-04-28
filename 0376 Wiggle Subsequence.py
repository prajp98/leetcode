def wiggleMaxLength(self, nums: List[int]) -> int:
    if not nums:
        return 0
    count = 1
    prev = 0
    for i in range(1, len(nums)):
        diff = nums[i] - nums[i - 1]
        if (diff > 0 and prev <= 0) or (diff < 0 and prev >= 0):
            count += 1
            prev = diff
    return count