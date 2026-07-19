class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def f(x):
            if not x: return 0
            l, r = f(x.left), f(x.right)
            return -1 if l < 0 or r < 0 or abs(l - r) > 1 else 1 + max(l, r)
        return f(root) >= 0