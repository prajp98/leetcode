def checkSubarraySum(self, nums: List[int], k: int) -> bool:
    m = {0: -1}
    total = 0

    for i, num in enumerate(nums):
        total = (total + num) % k
        if total in m:
            if i - m[total] > 1:
                return True
        else:
            m[total] = i
    return False