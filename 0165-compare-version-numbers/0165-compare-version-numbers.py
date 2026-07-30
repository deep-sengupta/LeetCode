class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        a, b = map(int, version1.split('.')), map(int, version2.split('.'))
        from itertools import zip_longest
        for x, y in zip_longest(a, b, fillvalue=0):
            if x != y:
                return 1 if x > y else -1
        return 0