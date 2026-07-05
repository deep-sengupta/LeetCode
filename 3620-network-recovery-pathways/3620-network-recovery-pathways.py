from typing import List
from collections import deque

class Solution:
    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)
        g = [[] for _ in range(n)]
        indeg = [0] * n
        vals = {0}

        for u, v, c in edges:
            g[u].append((v, c))
            indeg[v] += 1
            vals.add(c)

        q = deque(i for i, d in enumerate(indeg) if d == 0)
        topo = []
        while q:
            u = q.popleft()
            topo.append(u)
            for v, _ in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        vals = sorted(vals)
        last = n - 1
        inf = 10**30
        on = online
        adj = g
        order = topo

        def can(t: int) -> bool:
            dp = [inf] * n
            dp[0] = 0
            for u in order:
                du = dp[u]
                if du > k or not on[u]:
                    continue
                if u == last:
                    return True
                for v, c in adj[u]:
                    if c >= t and on[v]:
                        nd = du + c
                        if nd < dp[v]:
                            dp[v] = nd
            return dp[last] <= k

        if not can(0):
            return -1

        lo, hi = 0, len(vals) - 1
        while lo < hi:
            mid = (lo + hi + 1) >> 1
            if can(vals[mid]):
                lo = mid
            else:
                hi = mid - 1
        return vals[lo]