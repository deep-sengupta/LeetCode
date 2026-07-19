class Solution:
    def smallestSubsequence(self, s: str) -> str:
        c = Counter(s)
        st = []
        v = set()
        for x in s:
            c[x] -= 1
            if x in v:
                continue
            while st and st[-1] > x and c[st[-1]]:
                v.remove(st.pop())
            st.append(x)
            v.add(x)
        return ''.join(st)