def nthUglyNumber(self, n: int) -> int:
    s = set()
    s.add(1)
    cur = 1
    for i in range(n):
        cur = min(s)
        s.remove(cur)
        s.add(cur * 2)
        s.add(cur * 3)
        s.add(cur * 5)
    return cur