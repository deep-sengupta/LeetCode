from functools import cache

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        @cache
        def f(i, j):
            return i == len(s1) and j == len(s2) or \
            i < len(s1) and s1[i] == s3[i+j] and f(i+1, j) or \
            j < len(s2) and s2[j] == s3[i+j] and f(i, j+1)
        return f(0, 0)