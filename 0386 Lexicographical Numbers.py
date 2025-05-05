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

def lexicalOrder(self, n: int) -> List[int]:
    res = []
    curr = 1
    for _ in range(n):
        res.append(curr)
        if curr * 10 <= n:
            curr *= 10
        else:
            while curr % 10 == 9 or curr + 1 > n:
                curr //= 10
            curr += 1
    return res