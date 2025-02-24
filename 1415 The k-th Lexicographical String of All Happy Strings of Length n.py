def getHappyString(self, n: int, k: int) -> str:
    nextMap = {'a': 'bc', 'b': 'ac', 'c': 'ab'}
    res = []

    def dfs(c):
        if len(c) == n:
            res.append(c)
            return
        for nxt in nextMap[c[-1]]:
            dfs(c + nxt)

    for c in "abc":
        dfs(c)
    return res[k - 1] if k <= len(res) else ""