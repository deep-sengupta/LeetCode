class Solution:
    def maxActiveSectionsAfterTrade(self, s: str) -> int:
        a = sum(c == '1' for c in s)
        t = '1' + s + '1'
        c, l = [], []
        for x in t:
            if c and c[-1] == x:
                l[-1] += 1
            else:
                c.append(x)
                l.append(1)
        ans = a
        for i in range(1, len(c) - 1):
            if c[i] == '1':
                ans = max(ans, a + l[i - 1] + l[i + 1])
        return ans