class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows,cols=len(board),len(board[0])
        count=0
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=="X":
                    if (r==0 or board[r-1][c]==".") and (c==0 or board[r][c-1]=="."):
                        count+=1
        return count