func solve(b [][]byte) {
	if len(b) == 0 {
		return
	}
	m, n := len(b), len(b[0])
	var f func(int, int)
	f = func(i, j int) {
		if i < 0 || j < 0 || i == m || j == n || b[i][j] != 'O' {
			return
		}
		b[i][j] = '#'
		f(i+1, j)
		f(i-1, j)
		f(i, j+1)
		f(i, j-1)
	}
	for i := 0; i < m; i++ {
		f(i, 0)
		f(i, n-1)
	}
	for j := 0; j < n; j++ {
		f(0, j)
		f(m-1, j)
	}
	for i := 0; i < m; i++ {
		for j := 0; j < n; j++ {
			if b[i][j] == 'O' {
				b[i][j] = 'X'
			} else if b[i][j] == '#' {
				b[i][j] = 'O'
			}
		}
	}
}