def permute(self, nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(path):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for num in nums:
            if num not in path:
                path.append(num)
                dfs(path)
                path.pop()

    dfs([])
    return res