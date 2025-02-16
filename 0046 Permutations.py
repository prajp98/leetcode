def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(nums, cur):
        if not nums:
            res.append(cur[::])
            return
        for i in range(len(nums)):
            newNums = nums[:i] + nums[i + 1:]
            cur.append(nums[i])
            dfs(newNums, cur)
            cur.pop()

    dfs(nums, [])
    return res