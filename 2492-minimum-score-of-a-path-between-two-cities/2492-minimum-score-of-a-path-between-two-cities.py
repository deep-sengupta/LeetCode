from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        g = [[] for _ in range(n + 1)]
        for a, b, d in roads:
            g[a].append((b, d))
            g[b].append((a, d))

        stack = [1]
        seen = [False] * (n + 1)
        seen[1] = True
        ans = 10**9

        while stack:
            u = stack.pop()
            for v, d in g[u]:
                if d < ans:
                    ans = d
                if not seen[v]:
                    seen[v] = True
                    stack.append(v)

        return ans