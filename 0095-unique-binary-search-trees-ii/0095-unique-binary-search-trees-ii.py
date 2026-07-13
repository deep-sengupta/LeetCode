class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def f(l, r):
            if l > r: return [None]
            return [TreeNode(i, a, b)
                    for i in range(l, r + 1)
                    for a in f(l, i - 1)
                    for b in f(i + 1, r)]
        return f(1, n)