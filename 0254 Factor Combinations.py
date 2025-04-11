def getFactors(self, n: int) -> List[List[int]]:
    res = []

    def dfs(start, num, path):
        for i in range(start, int(num ** 0.5) + 1):
            if num % i == 0:
                res.append(path + [i, num // i])
                dfs(i, num // i, path + [i])

    dfs(2, n, [])
    return res