func sumNumbers(root *TreeNode) int {
	var f func(*TreeNode, int) int
	f = func(n *TreeNode, x int) int {
		if n == nil {
			return 0
		}
		x = x*10 + n.Val
		if n.Left == nil && n.Right == nil {
			return x
		}
		return f(n.Left, x) + f(n.Right, x)
	}
	return f(root, 0)
}