import "strconv"

func countAndSay(n int) string {
	s := "1"
	for ; n > 1; n-- {
		t := ""
		for i := 0; i < len(s); {
			j := i
			for j < len(s) && s[j] == s[i] {
				j++
			}
			t += strconv.Itoa(j-i) + s[i:i+1]
			i = j
		}
		s = t
	}
	return s
}