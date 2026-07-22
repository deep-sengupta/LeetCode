from typing import List

class SparseTable:
    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.st = [nums[:]]
        j = 1
        while (1 << j) <= self.n:
            prev = self.st[-1]
            size = self.n - (1 << j) + 1
            half = 1 << (j - 1)
            cur = [0] * size
            for i in range(size):
                cur[i] = max(prev[i], prev[i + half])
            self.st.append(cur)
            j += 1

    def query(self, l: int, r: int) -> int:
        i = (r - l + 1).bit_length() - 1
        return max(self.st[i][l], self.st[i][r - (1 << i) + 1])


class Solution:
    def maxActiveSectionsAfterTrade(self, s: str, queries: List[List[int]]) -> List[int]:
        ones = s.count('1')
        zero_groups, zero_group_index = self._get_zero_groups(s)

        if not zero_groups:
            return [ones] * len(queries)

        zero_merge_lengths = [a[1] + b[1] for a, b in zip(zero_groups, zero_groups[1:])]
        st = SparseTable(zero_merge_lengths) if zero_merge_lengths else None

        ans = []
        for l, r in queries:
            left = -1 if zero_group_index[l] == -1 else zero_groups[zero_group_index[l]][1] - (l - zero_groups[zero_group_index[l]][0])
            right = -1 if zero_group_index[r] == -1 else (r - zero_groups[zero_group_index[r]][0] + 1)

            start_adj = zero_group_index[l] + 1
            end_adj = zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1
            end_adj -= 1

            active = ones

            if s[l] == '0' and s[r] == '0' and zero_group_index[l] + 1 == zero_group_index[r]:
                active = max(active, ones + left + right)
            elif st is not None and start_adj <= end_adj:
                active = max(active, ones + st.query(start_adj, end_adj))

            if s[l] == '0' and zero_group_index[l] + 1 <= (zero_group_index[r] if s[r] == '1' else zero_group_index[r] - 1):
                active = max(active, ones + left + zero_groups[zero_group_index[l] + 1][1])

            if s[r] == '0' and zero_group_index[l] < zero_group_index[r] - 1:
                active = max(active, ones + right + zero_groups[zero_group_index[r] - 1][1])

            ans.append(active)

        return ans

    def _get_zero_groups(self, s: str):
        zero_groups = []
        zero_group_index = []
        for i, ch in enumerate(s):
            if ch == '0':
                if i > 0 and s[i - 1] == '0':
                    zero_groups[-1][1] += 1
                else:
                    zero_groups.append([i, 1])
            zero_group_index.append(len(zero_groups) - 1)
        return zero_groups, zero_group_index