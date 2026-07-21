class Solution {
    public List<List<Integer>> pathSum(TreeNode r, int t) {
        List<List<Integer>> a = new ArrayList<>();
        f(r, t, new ArrayList<>(), a);
        return a;
    }

    void f(TreeNode n, int s, List<Integer> p, List<List<Integer>> a) {
        if (n == null) return;
        p.add(n.val);
        if (n.left == null && n.right == null && s == n.val) a.add(new ArrayList<>(p));
        f(n.left, s - n.val, p, a);
        f(n.right, s - n.val, p, a);
        p.remove(p.size() - 1);
    }
}