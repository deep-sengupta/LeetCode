class Solution:
    def postorderTraversal(self, root):
        return self.postorderTraversal(root.left)+self.postorderTraversal(root.right)+[root.val] if root else []