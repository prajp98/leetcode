def subarraySum(self, nums: List[int], k: int) -> int:
    res = 0
    prefix = 0
    dic = defaultdict(int)
    dic[0] = 1
    for num in nums:
        prefix += num
        if prefix - k in dic:
            res += dic[prefix - k]
        dic[prefix] += 1
    return res