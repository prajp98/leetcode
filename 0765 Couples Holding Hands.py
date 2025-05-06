def minSwapsCouples(self, nums):
    m = {}
    for i, num in enumerate(nums):
        m[num] = i
    n = len(nums)
    res = 0
    for i in range(0, n, 2):
        a = nums[i]
        b = a ^ 1
        if nums[i + 1] == b:
            continue
        bi = m[b]
        m[nums[i + 1]] = bi
        m[b] = i + 1
        nums[bi], nums[i + 1] = nums[i + 1], nums[bi]
        res += 1
    return res