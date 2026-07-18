func totalNQueens(n int) int {
	c, d1, d2 := map[int]bool{}, map[int]bool{}, map[int]bool{}

	var dfs func(int) int
	dfs = func(r int) int {
		if r == n {
			return 1
		}
		ans := 0
		for i := 0; i < n; i++ {
			if c[i] || d1[r-i] || d2[r+i] {
				continue
			}
			c[i], d1[r-i], d2[r+i] = true, true, true
			ans += dfs(r + 1)
			delete(c, i)
			delete(d1, r-i)
			delete(d2, r+i)
		}
		return ans
	}

	return dfs(0)
}