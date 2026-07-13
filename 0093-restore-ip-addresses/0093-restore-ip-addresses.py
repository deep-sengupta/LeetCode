class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        def dfs(i, p):
            if len(p) == 4:
                if i == len(s): ans.append('.'.join(p))
                return
            for j in range(i + 1, min(i + 4, len(s) + 1)):
                x = s[i:j]
                if (x == '0' or x[0] != '0') and int(x) < 256:
                    dfs(j, p + [x])
        dfs(0, [])
        return ans