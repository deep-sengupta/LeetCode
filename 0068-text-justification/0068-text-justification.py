class Solution:
    def fullJustify(self, words, maxWidth):
        ans, i = [], 0
        while i < len(words):
            j, l = i, 0
            while j < len(words) and l + len(words[j]) + j - i <= maxWidth:
                l += len(words[j])
                j += 1
            g = j - i - 1
            if j == len(words) or g == 0:
                s = ' '.join(words[i:j]).ljust(maxWidth)
            else:
                q, r = divmod(maxWidth - l, g)
                s = ''
                for k in range(g):
                    s += words[i + k] + ' ' * (q + (k < r))
                s += words[j - 1]
            ans.append(s)
            i = j
        return ans