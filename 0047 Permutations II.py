def permuteUnique(self, nums: List[int]) -> List[List[int]]:
    res = []

    def dfs(path, counter):
        if len(path) == len(nums):
            res.append(path[:])
            return
        for num in counter:
            if counter[num] > 0:
                path.append(num)
                counter[num] -= 1
                dfs(path, counter)
                path.pop()
                counter[num] += 1

    dfs([], Counter(nums))
    return res