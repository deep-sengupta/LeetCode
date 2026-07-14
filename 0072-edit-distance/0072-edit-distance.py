class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = list(range(n + 1))
        for i in range(1, m + 1):
            pre, dp[0] = dp[0], i
            for j in range(1, n + 1):
                t = dp[j]
                dp[j] = pre if word1[i - 1] == word2[j - 1] else 1 + min(pre, dp[j], dp[j - 1])
                pre = t
        return dp[-1]