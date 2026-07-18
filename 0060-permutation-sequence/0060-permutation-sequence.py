from math import factorial

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        a = list(map(str, range(1, n + 1)))
        k -= 1
        r = []
        for i in range(n, 0, -1):
            f = factorial(i - 1)
            j, k = divmod(k, f)
            r.append(a.pop(j))
        return ''.join(r)