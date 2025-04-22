def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    m = {}
    for i, num in enumerate(nums):
        if num in m:
            if i - m[num] <= k:
                return True
        m[num] = i
    return False

def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
        if len(seen) > k:
            seen.remove(nums[i - k])
    return False