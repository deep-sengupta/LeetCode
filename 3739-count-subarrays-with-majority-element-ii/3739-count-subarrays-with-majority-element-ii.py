class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        s = 0
        pref = [0]
        for x in nums:
            if x == target:
                s += 1
            else:
                s -= 1
            pref.append(s)

        vals = sorted(set(pref))
        m = len(vals)
        pos = {v: i + 1 for i, v in enumerate(vals)}

        bit = [0] * (m + 2)

        def add(i):
            while i <= m:
                bit[i] += 1
                i += i & -i

        def query(i):
            res = 0
            while i:
                res += bit[i]
                i -= i & -i
            return res

        ans = 0
        for v in pref:
            idx = pos[v]
            ans += query(idx - 1)
            add(idx)
        return ans