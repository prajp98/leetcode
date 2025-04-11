def findTargetSumWays(self, nums: List[int], target: int) -> int:
    count = 0

    def dfs(i, total):
        nonlocal count
        if i == len(nums):
            if total == target:
                count += 1
            return
        dfs(i + 1, total + nums[i])
        dfs(i + 1, total - nums[i])

    dfs(0, 0)
    return count