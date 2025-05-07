def maximumProduct(self, nums: List[int]) -> int:
    nums.sort()
    return max(nums[-1] * nums[-2] * nums[-3],
               nums[0] * nums[1] * nums[-1])

def maximumProduct(self, nums: List[int]) -> int:
    max1 = max2 = max3 = -math.inf
    min1 = min2 = math.inf
    for n in nums:
        if n > max1:
            max1, max2, max3 = n, max1, max2
        elif n > max2:
            max2, max3 = n, max2
        elif n > max3:
            max3 = n

        if n < min1:
            min1, min2 = n, min1
        elif n < min2:
            min2 = n

    return max(max1 * max2 * max3, max1 * min1 * min2)