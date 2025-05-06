def solve(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    rows = len(board)
    cols = len(board[0])
    visit = set()
    directions = [[1, 0], [-1, 0], [0, -1], [0, 1]]

    def dfs(r, c):
        if r < 0 or r >= rows or c < 0 or c >= cols or (r, c) in visit or board[r][c] == "X":
            return
        visit.add((r, c))
        if board[r][c] == "O":
            board[r][c] = "1"
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    for r in range(rows):
        dfs(r, 0)
        dfs(r, cols - 1)
    for c in range(cols):
        dfs(0, c)
        dfs(rows - 1, c)
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == "O":
                board[r][c] = "X"
            if board[r][c] == "1":
                board[r][c] = "O"