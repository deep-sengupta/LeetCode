class Solution {
    int pre = 0;
    Map<Integer, Integer> map = new HashMap<>();

    public TreeNode buildTree(int[] preorder, int[] inorder) {
        for (int i = 0; i < inorder.length; i++)
            map.put(inorder[i], i);
        return build(preorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] preorder, int l, int r) {
        if (l > r) return null;
        TreeNode root = new TreeNode(preorder[pre++]);
        int i = map.get(root.val);
        root.left = build(preorder, l, i - 1);
        root.right = build(preorder, i + 1, r);
        return root;
    }
}