def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False

    rows, cols = len(matrix), len(matrix[0])
    r, c = 0, cols - 1
    while r < rows and c >= 0:
        val = matrix[r][c]
        if val == target:
            return True
        elif val > target:
            c -= 1  # move left
        else:
            r += 1  # move down
    return False