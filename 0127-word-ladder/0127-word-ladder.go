func ladderLength(beginWord, endWord string, wordList []string) int {
	m := map[string]bool{}
	for _, w := range wordList {
		m[w] = true
	}
	if !m[endWord] {
		return 0
	}
	q := []string{beginWord}
	step, n := 1, len(beginWord)
	for len(q) > 0 {
		t := q
		q = nil
		for _, w := range t {
			if w == endWord {
				return step
			}
			b := []byte(w)
			for i := 0; i < n; i++ {
				c := b[i]
				for ch := byte('a'); ch <= 'z'; ch++ {
					b[i] = ch
					s := string(b)
					if m[s] {
						delete(m, s)
						q = append(q, s)
					}
				}
				b[i] = c
			}
		}
		step++
	}
	return 0
}