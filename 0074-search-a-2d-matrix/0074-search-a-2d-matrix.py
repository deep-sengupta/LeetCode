from bisect import bisect_left

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        a = sum(matrix, [])
        i = bisect_left(a, target)
        return i < len(a) and a[i] == target