def combine(self, n: int, k: int) -> List[List[int]]:
    res = []

    def backtrack(l, i):
        if len(l) == k:
            res.append(l[:])
            return
        for j in range(i, n + 1):
            l.append(j)
            backtrack(l, j + 1)
            l.pop()

    backtrack([], 1)
    return res

def combine(self, n: int, k: int) -> List[List[int]]:
    res = []
    def dfs(start, path):
        if len(path) == k:
            res.append(path[:])
            return
        # We only loop till n - (k - len(path)) + 1
        for i in range(start, n - (k - len(path)) + 2):
            path.append(i)
            dfs(i + 1, path)
            path.pop()
    dfs(1, [])
    return res