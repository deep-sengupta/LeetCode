class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        return list({*map(tuple, permutations(nums))})