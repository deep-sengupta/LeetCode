class Solution {
    int ans = Integer.MIN_VALUE;

    public int maxPathSum(TreeNode root) {
        dfs(root);
        return ans;
    }

    int dfs(TreeNode r) {
        if (r == null) return 0;
        int l = Math.max(0, dfs(r.left));
        int x = Math.max(0, dfs(r.right));
        ans = Math.max(ans, l + x + r.val);
        return Math.max(l, x) + r.val;
    }
}