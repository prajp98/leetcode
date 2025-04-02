def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    m = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in m:
            d = i - m[nums[i]]
            if d <= k:
                return True
        m[nums[i]] = i
    return False