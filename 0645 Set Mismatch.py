def findErrorNums(self, nums: List[int]) -> List[int]:
    count = defaultdict(int)
    res = [0, 0]
    for num in nums:
        count[num] += 1
    for i in range(1, len(nums) + 1):
        if count[i] == 2:
            res[0] = i
        if count[i] == 0:
            res[1] = i
    return res