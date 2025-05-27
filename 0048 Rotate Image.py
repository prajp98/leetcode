def rotate(self, matrix: List[List[int]]) -> None:
    rows = len(matrix)
    cols = rows
    l, r, u, d = 0, cols - 1, 0, rows - 1
    while l < r:
        for i in range(r - l):
            u, d = l, r
            t = matrix[u][l + i]
            matrix[u][l + i] = matrix[d - i][l]
            matrix[d - i][l] = matrix[d][r - i]
            matrix[d][r - i] = matrix[u + i][r]
            matrix[u + i][r] = t
        r -= 1
        l += 1

def rotate(self, matrix: List[List[int]]) -> None:
    # reverse
    l = 0
    r = len(matrix) -1
    while l < r:
        matrix[l], matrix[r] = matrix[r], matrix[l]
        l += 1
        r -= 1
    # transpose
    for i in range(len(matrix)):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]