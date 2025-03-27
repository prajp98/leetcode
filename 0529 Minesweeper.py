def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
    rows, cols = len(board), len(board[0])
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    r, c = click
    if board[r][c] == 'M':
        board[r][c] = 'X'
        return board
    q = deque([(r, c)])
    while q:
        r, c = q.popleft()
        mines = 0
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "M":
                mines += 1
        if mines > 0:
            board[r][c] = str(mines)

        else:
            board[r][c] = 'B'
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and board[nr][nc] == "E":
                    q.append((nr, nc))
                    board[nr][nc] = "B"
    return board
