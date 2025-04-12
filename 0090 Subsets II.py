def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = []
    subset = []
    nums.sort()

    def dfs(i):
        if i >= len(nums):
            res.append(subset[::])
            return
        subset.append(nums[i])
        dfs(i + 1)
        subset.pop()
        while i < len(nums) - 1 and nums[i] == nums[i + 1]:
            i += 1
        dfs(i + 1)

    dfs(0)
    return res

def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()  # Sort to handle duplicates easily

    def dfs(start, path):
        res.append(path[:])
        for i in range(start, len(nums)):
            # Skip duplicates
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            dfs(i + 1, path)
            path.pop()

    dfs(0, [])
    return res