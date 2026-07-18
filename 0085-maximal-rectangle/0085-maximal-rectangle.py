class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0
        h = [0] * len(matrix[0])
        ans = 0
        for r in matrix:
            for i, x in enumerate(r):
                h[i] = h[i] + 1 if x == '1' else 0
            st = []
            for i, x in enumerate(h + [0]):
                while st and h[st[-1]] > x:
                    H = h[st.pop()]
                    W = i if not st else i - st[-1] - 1
                    ans = max(ans, H * W)
                st.append(i)
        return ans