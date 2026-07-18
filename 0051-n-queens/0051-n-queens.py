class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        r, c, d1, d2 = [], set(), set(), set()

        def dfs(i, b):
            if i == n:
                r.append(b)
                return
            for j in range(n):
                if j in c or i - j in d1 or i + j in d2:
                    continue
                c.add(j)
                d1.add(i - j)
                d2.add(i + j)
                dfs(i + 1, b + ['.' * j + 'Q' + '.' * (n - j - 1)])
                c.remove(j)
                d1.remove(i - j)
                d2.remove(i + j)

        dfs(0, [])
        return r