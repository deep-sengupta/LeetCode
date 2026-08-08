class Solution:
    def validSequence(self, a: str, b: str) -> list[int]:
        n, m = len(a), len(b)
        r = [-1] * m
        j = m - 1

        for i in range(n - 1, -1, -1):
            if j >= 0 and a[i] == b[j]:
                r[j] = i
                j -= 1

        ans = []
        j = 0
        changed = 0

        for i, c in enumerate(a):
            if j == m:
                break
            if c == b[j] or (not changed and (j == m - 1 or i < r[j + 1])):
                ans.append(i)
                changed |= c != b[j]
                j += 1

        return ans if j == m else []