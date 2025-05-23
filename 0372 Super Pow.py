def superPow(self, a: int, b: List[int]) -> int:
    m = 1337
    res = 1
    for i in b:
        res = pow(res, 10, m) * pow(a, i, m)
    return res % m