def smallestFactorization(self, num: int) -> int:
    if num < 10:
        return num
    res = 0
    m = 1
    for i in range(9, 1, -1):
        while num % i == 0:
            num //= i
            res = m * i + res
            m *= 10
    return res if num == 1 and res <= 2 ** 31 - 1 else 0