class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        def f(a, b):
            return a == b if not a or not b else a.val == b.val and f(a.left, b.right) and f(a.right, b.left)
        return f(root.left, root.right)