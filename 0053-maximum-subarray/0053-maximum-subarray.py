class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        s = a = nums[0]
        for x in nums[1:]:
            s = max(x, s + x)
            a = max(a, s)
        return a