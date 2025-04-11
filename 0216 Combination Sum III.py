def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    res = []

    def dfs(i, path, total):
        if len(path) == k and total == n:
            res.append(path[:])
            return
        if len(path) > k or total > n:
            return
        for j in range(i, 10):
            path.append(j)
            dfs(j + 1, path, total + j)
            path.pop()

    dfs(1, [], 0)
    return res