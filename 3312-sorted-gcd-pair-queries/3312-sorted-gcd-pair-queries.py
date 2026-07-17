from bisect import bisect_left

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        m = max(nums)
        f = [0] * (m + 1)
        for x in nums:
            f[x] += 1

        c = [0] * (m + 1)
        g = [0] * (m + 1)

        for i in range(m, 0, -1):
            s = 0
            for j in range(i, m + 1, i):
                s += f[j]
            c[i] = s * (s - 1) // 2
            for j in range(i * 2, m + 1, i):
                c[i] -= g[j]
            g[i] = c[i]

        p = []
        t = 0
        for i in range(1, m + 1):
            t += g[i]
            p.append(t)

        return [bisect_left(p, q + 1) + 1 for q in queries]