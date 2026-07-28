from collections import Counter
from math import gcd

class Solution:
    def maxPoints(self, p: List[List[int]]) -> int:
        ans = 1
        for i, (x1, y1) in enumerate(p):
            c = Counter()
            for x2, y2 in p[i + 1:]:
                dx, dy = x2 - x1, y2 - y1
                g = gcd(dx, dy)
                dx, dy = dx // g, dy // g
                if dx < 0: dx, dy = -dx, -dy
                if dx == 0: dy = 1
                if dy == 0: dx = 1
                c[(dx, dy)] += 1
            ans = max(ans, max(c.values(), default=0) + 1)
        return ans