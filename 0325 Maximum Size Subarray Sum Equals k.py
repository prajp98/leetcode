def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    prefix = 0
    res = 0
    indices = {0: -1}

    for i, num in enumerate(nums):
        prefix += num
        if prefix - k in indices:
            res = max(res, i - indices[prefix - k])
        if prefix not in indices:
            indices[prefix] = i
    return res