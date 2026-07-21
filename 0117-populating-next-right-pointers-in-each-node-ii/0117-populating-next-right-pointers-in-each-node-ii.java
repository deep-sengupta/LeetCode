class Solution {
    public Node connect(Node root) {
        Node cur = root;
        while (cur != null) {
            Node d = new Node(0), t = d;
            while (cur != null) {
                if (cur.left != null) t = t.next = cur.left;
                if (cur.right != null) t = t.next = cur.right;
                cur = cur.next;
            }
            cur = d.next;
        }
        return root;
    }
}