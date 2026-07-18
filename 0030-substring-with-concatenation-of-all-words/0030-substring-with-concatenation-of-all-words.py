from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        m, n = len(words[0]), len(words)
        cnt, ans = Counter(words), []
        for i in range(m):
            l = c = i
            d = Counter()
            for r in range(i, len(s) - m + 1, m):
                w = s[r:r + m]
                if w in cnt:
                    d[w] += 1
                    while d[w] > cnt[w]:
                        d[s[l:l + m]] -= 1
                        l += m
                        c += 1
                    if (r - l) // m + 1 == n:
                        ans.append(l)
                        d[s[l:l + m]] -= 1
                        l += m
                else:
                    d.clear()
                    l = r + m
        return ans