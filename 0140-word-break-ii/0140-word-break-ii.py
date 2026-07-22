class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        d = set(wordDict)
        memo = {}

        def dfs(s):
            if s in memo:
                return memo[s]
            if not s:
                return [""]
            res = []
            for w in d:
                if s.startswith(w):
                    for x in dfs(s[len(w):]):
                        res.append(w + (" " + x if x else ""))
            memo[s] = res
            return res

        return dfs(s)