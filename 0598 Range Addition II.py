def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
    if not ops:
        return m * n
    minr, minc = m, n
    for op in ops:
        minr = min(minr, op[0])
        minc = min(minc, op[1])
    return minr * minc