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

def nthUglyNumber(self, n: int) -> int:
    heap = [1]
    visit = {1}
    for _ in range(n):
        cur = heappop(heap)
        for prime in [2,3,5]:
            new = cur * prime
            if new not in visit:
                heappush(heap, new)
                visit.add(new)
    return cur