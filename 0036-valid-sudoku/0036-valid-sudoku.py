class Solution:
    def isValidSudoku(self, board):
        s = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    x = board[i][j]
                    if (i,x) in s or (x,j) in s or (i//3,j//3,x) in s:
                        return False
                    s |= {(i,x),(x,j),(i//3,j//3,x)}
        return True