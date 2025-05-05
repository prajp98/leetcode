def lexicalOrder(self, n: int) -> List[int]:
    res = []

    def dfs(x, n):
        if x > n:
            return
        res.append(x)
        pe = x * 10
        for i in range(10):
            dfs(pe + i, n)

    for i in range(1, 10):
        dfs(i, n)
    return res