class Solution {
    int post;
    Map<Integer, Integer> map = new HashMap<>();

    public TreeNode buildTree(int[] inorder, int[] postorder) {
        post = postorder.length - 1;
        for (int i = 0; i < inorder.length; i++)
            map.put(inorder[i], i);
        return build(postorder, 0, inorder.length - 1);
    }

    private TreeNode build(int[] postorder, int l, int r) {
        if (l > r) return null;
        TreeNode root = new TreeNode(postorder[post--]);
        int i = map.get(root.val);
        root.right = build(postorder, i + 1, r);
        root.left = build(postorder, l, i - 1);
        return root;
    }
}