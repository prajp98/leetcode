def findSubsequences(self, nums: List[int]) -> List[List[int]]:
    res = set()
    path = []

    def backtrack(i):
        if i == len(nums):
            if len(path) >= 2:
                res.add(tuple(path))
            return
        if not path or path[-1] <= nums[i]:
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()
        backtrack(i + 1)

    backtrack(0)
    return list(res)