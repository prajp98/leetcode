def hIndex(self, citations: List[int]) -> int:
    n = len(citations)
    res = [0] * (n + 1)

    for i in range(n):
        if citations[i] > n:
            res[n] += 1
        else:
            res[citations[i]] += 1
    s = 0
    for i in range(n, -1, -1):
        s += res[i]
        if s >= i:
            return i
    return 0