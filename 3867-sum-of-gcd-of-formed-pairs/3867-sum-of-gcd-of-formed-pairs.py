from math import gcd

class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        a, m = [], 0
        for x in nums:
            m = max(m, x)
            a.append(gcd(x, m))
        a.sort()
        return sum(gcd(a[i], a[~i]) for i in range(len(a) // 2))