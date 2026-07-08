class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        mod = 10 ** 9 + 7
        n = len(s)

        pre = [0] * (n + 1)
        cnt = 0
        for i, c in enumerate(s):
            if c != '0':
                cnt += 1
            pre[i + 1] = cnt

        pow10 = [1] * (cnt + 1)
        for i in range(1, cnt + 1):
            pow10[i] = pow10[i - 1] * 10 % mod

        val = [0] * (cnt + 1)
        sm = [0] * (cnt + 1)
        idx = 0
        for c in s:
            if c != '0':
                d = ord(c) - 48
                idx += 1
                val[idx] = (val[idx - 1] * 10 + d) % mod
                sm[idx] = sm[idx - 1] + d

        ans = []
        for l, r in queries:
            a = pre[l]
            b = pre[r + 1]
            if a == b:
                ans.append(0)
                continue
            x = (val[b] - val[a] * pow10[b - a]) % mod
            ans.append(x * (sm[b] - sm[a]) % mod)

        return ans