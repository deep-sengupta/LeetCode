class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        a = b = p = None
        def dfs(r):
            nonlocal a, b, p
            if not r: return
            dfs(r.left)
            if p and p.val > r.val:
                b = r
                if not a: a = p
            p = r
            dfs(r.right)
        dfs(root)
        a.val, b.val = b.val, a.val