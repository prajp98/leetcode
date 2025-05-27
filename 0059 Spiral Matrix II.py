def generateMatrix(self, n: int) -> List[List[int]]:
    x, y, dx, dy = 0, 0, 1, 0
    res = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n * n):
        res[y][x] = i + 1
        if not 0 <= x + dx < n or not 0 <= y + dy < n or res[y + dy][x + dx] != 0:
            dx, dy = -dy, dx
        x += dx
        y += dy
    return res

def generateMatrix(self, n: int) -> List[List[int]]:
    matrix = [[0] * n for _ in range(n)]
    count = 1
    top, left = 0, 0
    down, right = n - 1, n - 1

    while count <= n * n:
        # Fill top row (left to right)
        for i in range(left, right + 1):
            matrix[top][i] = count
            count += 1
        top += 1

        # Fill right column (top to bottom)
        for i in range(top, down + 1):
            matrix[i][right] = count
            count += 1
        right -= 1

        # Fill bottom row (right to left)
        for i in range(right, left - 1, -1):
            matrix[down][i] = count
            count += 1
        down -= 1

        # Fill left column (bottom to top)
        for i in range(down, top - 1, -1):
            matrix[i][left] = count
            count += 1
        left += 1

    return matrix