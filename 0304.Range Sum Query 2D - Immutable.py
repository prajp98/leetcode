class NumMatrix:
    def __init__(self, matrix):
        if not matrix or not matrix[0]:
            self.prefix = []
            return
        rows, cols = len(matrix), len(matrix[0])
        self.prefix = [[0] * (cols + 1) for _ in range(rows + 1)]
        for r in range(rows):
            for c in range(cols):
                self.prefix[r + 1][c + 1] = self.prefix[r + 1][c] + self.prefix[r][c + 1] - self.prefix[r][c] + \
                                            matrix[r][c]

    def sumRegion(self, row1, col1, row2, col2):
        if not self.prefix:
            return 0

        return self.prefix[row2 + 1][col2 + 1] - self.prefix[row2 + 1][col1] - self.prefix[row1][col2 + 1] + \
            self.prefix[row1][col1]