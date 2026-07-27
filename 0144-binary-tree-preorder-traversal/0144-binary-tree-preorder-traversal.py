class Solution:
    def preorderTraversal(self, root):
        return [root.val]+self.preorderTraversal(root.left)+self.preorderTraversal(root.right) if root else []