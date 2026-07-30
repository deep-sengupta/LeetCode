class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        c = n = 0
        for x in nums:
            if c == 0:
                n = x
            c += 1 if x == n else -1
        return n