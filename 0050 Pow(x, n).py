def myPow(self, x: float, n: int) -> float:
    def power(x: float, n: int) -> float:
        if n == 0:
            return 1
        half = power(x, n // 2)
        return half * half if n % 2 == 0 else half * half * x

    if n < 0:
        x = 1 / x
        n = -n

    return power(x, n)