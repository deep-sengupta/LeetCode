class Solution:
    def convertToTitle(self, n: int) -> str:
        s = ""
        while n:
            n -= 1
            n, r = divmod(n, 26)
            s = chr(r + 65) + s
        return s