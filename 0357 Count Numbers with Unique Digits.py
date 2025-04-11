def countNumbersWithUniqueDigits(self, n: int) -> int:
    if n == 0:
        return 1
    res = 10
    unique = 9
    available = 9
    for i in range(2, n + 1):
        unique *= available
        res += unique
        available -= 1
    return res