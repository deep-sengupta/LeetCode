func minCut(s string) int {
	n := len(s)
	dp := make([]int, n)
	for i := range dp {
		dp[i] = i
	}
	for i := 0; i < n; i++ {
		for _, p := range [][2]int{{i, i}, {i, i + 1}} {
			l, r := p[0], p[1]
			for l >= 0 && r < n && s[l] == s[r] {
				if l == 0 {
					dp[r] = 0
				} else if dp[l-1]+1 < dp[r] {
					dp[r] = dp[l-1] + 1
				}
				l--
				r++
			}
		}
	}
	return dp[n-1]
}