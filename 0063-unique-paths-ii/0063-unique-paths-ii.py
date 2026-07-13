class Solution:
    def uniquePathsWithObstacles(self, g: List[List[int]]) -> int:
        n = len(g[0])
        dp = [1] + [0] * (n - 1)
        for r in g:
            for j in range(n):
                if r[j]:
                    dp[j] = 0
                elif j:
                    dp[j] += dp[j - 1]
        return dp[-1]