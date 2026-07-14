class Solution:
    def sortColors(self, nums: List[int]) -> None:
        c = nums.count
        nums[:] = [0]*c(0) + [1]*c(1) + [2]*c(2)