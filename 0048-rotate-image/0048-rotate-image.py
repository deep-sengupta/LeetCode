class Solution:
    def rotate(self, a: List[List[int]]) -> None:
        a[:] = map(list, zip(*a[::-1]))