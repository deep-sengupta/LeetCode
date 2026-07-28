class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        a = b = ans = nums[0]
        for x in nums[1:]:
            a, b = max(x, a*x, b*x), min(x, a*x, b*x)
            ans = max(ans, a)
        return ans