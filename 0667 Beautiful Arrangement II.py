def constructArray(self, n: int, k: int) -> List[int]:
    l, r = 1, n
    res = []
    for i in range(k):
        if i % 2 == 0:
            res.append(l)
            l += 1
        else:
            res.append(r)
            r -= 1
    for i in range(k, n):
        if k % 2 == 0:
            res.append(r)
            r -= 1
        else:
            res.append(l)
            l += 1
    return res