class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        i = j = 0
        star = -1
        k = 0
        while i < len(s):
            if j < len(p) and p[j] in (s[i], '?'):
                i += 1
                j += 1
            elif j < len(p) and p[j] == '*':
                star, k, j = j, i, j + 1
            elif star != -1:
                k += 1
                i, j = k, star + 1
            else:
                return False
        return all(c == '*' for c in p[j:])