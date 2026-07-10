class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[int]:
        order = sorted((v, i) for i, v in enumerate(nums))
        vals = [v for v, _ in order]
        rank = [0] * n
        comp = [0] * n

        cid = 0
        for i, (_, idx) in enumerate(order):
            if i and vals[i] - vals[i - 1] > maxDiff:
                cid += 1
            rank[idx] = i
            comp[idx] = cid

        m = n
        nxt = [0] * m
        j = 0
        for i in range(m):
            while j + 1 < m and vals[j + 1] - vals[i] <= maxDiff:
                j += 1
            nxt[i] = j
            if j == i:
                j += 1

        LOG = (n).bit_length()
        up = [nxt]
        for _ in range(1, LOG):
            prev = up[-1]
            up.append([prev[prev[i]] for i in range(m)])

        ans = []
        for u, v in queries:
            if comp[u] != comp[v]:
                ans.append(-1)
                continue
            l, r = rank[u], rank[v]
            if l > r:
                l, r = r, l
            if l == r:
                ans.append(0)
                continue
            cur = l
            steps = 0
            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < r:
                    cur = up[k][cur]
                    steps += 1 << k
            ans.append(steps + 1)

        return ans