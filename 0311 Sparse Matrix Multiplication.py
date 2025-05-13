def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m, k, n = len(mat1), len(mat2), len(mat2[0])
    res = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            for x in range(k):
                res[r][c] += mat1[r][x] * mat2[x][c]
    return res