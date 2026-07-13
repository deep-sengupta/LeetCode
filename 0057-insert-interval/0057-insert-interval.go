func insert(a [][]int, n []int) (r [][]int) {
	for _, v := range a {
		if v[1] < n[0] {
			r = append(r, v)
		} else if v[0] > n[1] {
			r = append(r, n)
			n = v
		} else {
			if v[0] < n[0] {
				n[0] = v[0]
			}
			if v[1] > n[1] {
				n[1] = v[1]
			}
		}
	}
	return append(r, n)
}