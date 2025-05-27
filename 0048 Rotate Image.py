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