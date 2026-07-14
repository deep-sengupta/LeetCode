class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        def dfs(i, j, k):
            if k == len(word): return True
            if i < 0 or i == m or j < 0 or j == n or board[i][j] != word[k]:
                return False
            t, board[i][j] = board[i][j], '#'
            ok = dfs(i+1,j,k+1) or dfs(i-1,j,k+1) or dfs(i,j+1,k+1) or dfs(i,j-1,k+1)
            board[i][j] = t
            return ok
        return any(dfs(i, j, 0) for i in range(m) for j in range(n))