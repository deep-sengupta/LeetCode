import "sort"

func searchRange(a []int, t int) []int {
	l := sort.SearchInts(a, t)
	if l == len(a) || a[l] != t {
		return []int{-1, -1}
	}
	return []int{l, sort.Search(len(a), func(i int) bool { return a[i] > t }) - 1}
}