def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m, k, n = len(mat1), len(mat2), len(mat2[0])
    res = [[0] * n for _ in range(m)]
    for r in range(m):
        for c in range(n):
            for x in range(k):
                res[r][c] += mat1[r][x] * mat2[x][c]
    return res

def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
    m, n, k = len(mat1), len(mat1[0]), len(mat2[0])
    res = [[0] * k for _ in range(m)]

    for i in range(m):
        for j in range(n):
            if mat1[i][j] != 0:
                for x in range(k):
                    if mat2[j][x] != 0:
                        res[i][x] += mat1[i][j]*mat2[j][x]
    return res