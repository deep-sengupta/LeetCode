class Solution:
    def jump(self, nums: List[int]) -> int:
        ans = end = far = 0
        for i in range(len(nums) - 1):
            far = max(far, i + nums[i])
            if i == end:
                ans += 1
                end = far
        return ans