class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def f(n, l, r):
            return not n or l < n.val < r and f(n.left, l, n.val) and f(n.right, n.val, r)
        return f(root, float('-inf'), float('inf'))