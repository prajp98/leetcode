def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    left = 0
    zero = 0
    maxi = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            zero += 1
        while zero > 1:
            if nums[left] == 0:
                zero -= 1
            left += 1
        maxi = max(maxi, right - left + 1)
    return maxi

def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
    maxi = 0
    last_zero = -1
    left = 0
    for right in range(len(nums)):
        if nums[right] == 0:
            left = last_zero + 1
            last_zero = right
        maxi = max(maxi, right - left + 1)

    return maxi