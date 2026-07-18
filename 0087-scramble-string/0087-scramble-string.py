from functools import cache

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def f(a, b):
            if a == b:
                return True
            if sorted(a) != sorted(b):
                return False
            for i in range(1, len(a)):
                if f(a[:i], b[:i]) and f(a[i:], b[i:]) or \
                   f(a[:i], b[-i:]) and f(a[i:], b[:-i]):
                    return True
            return False
        return f(s1, s2)