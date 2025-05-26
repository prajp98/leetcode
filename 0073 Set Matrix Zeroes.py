def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])

    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == 0:
                for i in range(rows):
                    if matrix[i][c] != 0:
                        matrix[i][c] = "."
                for i in range(cols):
                    if matrix[r][i] != 0:
                        matrix[r][i] = "."
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c] == ".":
                matrix[r][c] = 0