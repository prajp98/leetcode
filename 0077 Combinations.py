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