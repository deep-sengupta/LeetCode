func longestConsecutive(nums []int) int {
	m := map[int]bool{}
	for _, x := range nums {
		m[x] = true
	}
	ans := 0
	for x := range m {
		if m[x-1] {
			continue
		}
		y := x
		for m[y] {
			y++
		}
		if y-x > ans {
			ans = y - x
		}
	}
	return ans
}