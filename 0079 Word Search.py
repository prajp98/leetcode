def exist(self, board: List[List[str]], word: str) -> bool:
    rows, cols = len(board), len(board[0])
    directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def dfs(r, c, i):
        if i == len(word):
            return True
        if r < 0 or r >= rows or c < 0 or c >= cols or board[r][c] != word[i]:
            return False
        t = board[r][c]
        board[r][c] = "#"
        for dr, dc in directions:
            if dfs(r + dr, c + dc, i + 1):
                return True
        board[r][c] = t
        return False

    if rows * cols < len(word):
        return False
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0] and dfs(r, c, 0):
                return True
    return False