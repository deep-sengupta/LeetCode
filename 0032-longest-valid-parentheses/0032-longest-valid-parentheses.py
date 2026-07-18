class Solution:
    def longestValidParentheses(self, s: str) -> int:
        st, ans = [-1], 0
        for i, c in enumerate(s):
            if c == '(':
                st.append(i)
            else:
                st.pop()
                if st:
                    ans = max(ans, i - st[-1])
                else:
                    st.append(i)
        return ans