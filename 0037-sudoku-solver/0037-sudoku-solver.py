class Solution:
    def solveSudoku(self, board):
        R = [set() for _ in range(9)]
        C = [set() for _ in range(9)]
        B = [set() for _ in range(9)]
        E = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    E.append((i, j))
                else:
                    x = board[i][j]
                    R[i].add(x)
                    C[j].add(x)
                    B[i // 3 * 3 + j // 3].add(x)

        def dfs(k):
            if k == len(E):
                return True
            i, j = E[k]
            b = i // 3 * 3 + j // 3
            for x in '123456789':
                if x not in R[i] and x not in C[j] and x not in B[b]:
                    board[i][j] = x
                    R[i].add(x); C[j].add(x); B[b].add(x)
                    if dfs(k + 1):
                        return True
                    R[i].remove(x); C[j].remove(x); B[b].remove(x)
            board[i][j] = '.'
            return False

        dfs(0)