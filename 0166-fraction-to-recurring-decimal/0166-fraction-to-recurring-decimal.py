class Solution:
    def fractionToDecimal(self, n: int, d: int) -> str:
        if n % d == 0: return str(n // d);
        s = "-" if n * d < 0 else ""
        n, d = abs(n), abs(d)
        s += str(n // d) + "."
        n %= d
        m = {}
        while n:
            if n in m: return s[:m[n]] + "(" + s[m[n]:] + ")"
            m[n] = len(s)
            n *= 10
            s += str(n // d)
            n %= d
        return s