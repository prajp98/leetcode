def newInteger(self, n: int) -> int:
    res = ""
    while n:
        res = str(n % 9) + res
        n = n // 9
    return int(res)