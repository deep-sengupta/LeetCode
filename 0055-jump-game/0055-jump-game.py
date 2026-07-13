class Solution:
    def canJump(self, nums: List[int]) -> bool:
        r = 0
        for i, n in enumerate(nums):
            if i > r: return False
            r = max(r, i + n)
        return True