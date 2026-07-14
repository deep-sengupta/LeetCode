class Solution:
    def setZeroes(self, a: List[List[int]]) -> None:
        R, C = set(), set()
        for i, r in enumerate(a):
            for j, x in enumerate(r):
                if x == 0:
                    R.add(i)
                    C.add(j)
        for i in range(len(a)):
            for j in range(len(a[0])):
                if i in R or j in C:
                    a[i][j] = 0