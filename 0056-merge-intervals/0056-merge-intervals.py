class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        r = [intervals[0]]
        for s, e in intervals[1:]:
            if s <= r[-1][1]:
                r[-1][1] = max(r[-1][1], e)
            else:
                r += [[s, e]]
        return r