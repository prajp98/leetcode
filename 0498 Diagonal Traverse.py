def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
    m, n = len(mat), len(mat[0])
    d = defaultdict(list)
    for c in range(n):
        for r in range(m):
            d[r + c].append(mat[r][c])
    res = []
    for i in range(m + n):
        if i % 2 == 0:
            res += d[i]
        else:
            res += d[i][::-1]
    return res