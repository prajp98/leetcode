def longestConsecutive(self, nums: List[int]) -> int:
    s = set(nums)
    maxl = 0
    for n in nums:
        if n - 1 not in s:
            l = 1
            while (n + l) in s:
                l += 1
            maxl = max(maxl, l)
    return maxl