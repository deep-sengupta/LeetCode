func combinationSum(c []int, t int) (r [][]int) {
	var p []int
	var f func(int, int)
	f = func(i, s int) {
		if s == 0 {
			r = append(r, append([]int{}, p...))
			return
		}
		if i == len(c) || s < 0 {
			return
		}
		p = append(p, c[i])
		f(i, s-c[i])
		p = p[:len(p)-1]
		f(i+1, s)
	}
	f(0, t)
	return
}