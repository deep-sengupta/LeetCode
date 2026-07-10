class Solution:
    def multiply(self, a: str, b: str) -> str:
        if a == "0" or b == "0":
            return "0"
        n, m = len(a), len(b)
        r = [0] * (n + m)
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                p = (ord(a[i]) - 48) * (ord(b[j]) - 48) + r[i + j + 1]
                r[i + j + 1] = p % 10
                r[i + j] += p // 10
        i = 0
        while r[i] == 0:
            i += 1
        return ''.join(map(str, r[i:]))