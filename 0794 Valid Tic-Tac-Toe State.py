def validTicTacToe(self, board: List[str]) -> bool:
    def check(mark):
        for i in range(3):
            if all(board[i][j] == mark for j in range(3)):
                return True
            if all(board[j][i] == mark for j in range(3)):
                return True
        if all(board[i][i] == mark for i in range(3)):
            return True
        return all(board[i][2 - i] == mark for i in range(3))

    count_x = sum(row.count('X') for row in board)
    count_o = sum(row.count('O') for row in board)
    if count_x != count_o and count_x - 1 != count_o:
        return False
    if check('X') and count_x - 1 != count_o:
        return False
    if check('O') and count_x != count_o:
        return False
    return True