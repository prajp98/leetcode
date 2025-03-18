def findPairs(self, nums: List[int], k: int) -> int:
    res = 0
    if k < 0:
        return 0
    count = Counter(nums)
    for num in count:
        if k == 0:
            if count[num] > 1:
                res += 1
        else:
            if num + k in count:
                res += 1
    return res