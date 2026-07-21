class Solution {
    public Node connect(Node root) {
        if (root == null) return null;
        Node l = root;
        while (l.left != null) {
            for (Node c = l; c != null; c = c.next) {
                c.left.next = c.right;
                if (c.next != null) c.right.next = c.next.left;
            }
            l = l.left;
        }
        return root;
    }
}