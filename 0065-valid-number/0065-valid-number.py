class Solution:
    def isNumber(self, s: str) -> bool:
        n = d = e = False
        for i, c in enumerate(s):
            if c.isdigit():
                n = True
            elif c in '+-':
                if i and s[i - 1] not in 'eE':
                    return False
            elif c == '.':
                if d or e:
                    return False
                d = True
            elif c in 'eE':
                if e or not n:
                    return False
                e = True
                n = False
            else:
                return False
        return n