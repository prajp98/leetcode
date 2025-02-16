def solveNQueens(self, n: int) -> List[List[str]]:
    res = []
    col = set()
    posDiag = set()
    negDiag = set()

    board = [["." for i in range(n)] for j in range(n)]

    def dfs(r):
        if r == n:
            copy = ["".join(row) for row in board]
            res.append(copy)
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            dfs(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    dfs(0)
    return res