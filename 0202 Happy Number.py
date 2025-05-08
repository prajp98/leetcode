def isHappy(self, n: int) -> bool:
    s = set()
    while n > 0:
        m = 0
        while n > 0:
            x = n % 10
            m += (x * x)
            n = n // 10
        if m == 1:
            return True
        if m in s:
            return False
        s.add(m)
        n = m
    return True