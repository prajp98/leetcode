def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
    countAB = defaultdict(int)
    for a in A:
        for b in B:
            countAB[a + b] += 1
    count = 0
    for c in C:
        for d in D:
            target = -(c + d)
            if target in countAB:
                count += countAB[target]
    return count
