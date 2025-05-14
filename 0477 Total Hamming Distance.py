def totalHammingDistance(self, nums: List[int]) -> int:
    total = 0
    n = len(nums)
    for i in range(32):
        count = 0
        for num in nums:
            if (num >> i) & 1:
                count += 1
        total += count * (n - count)
    return total