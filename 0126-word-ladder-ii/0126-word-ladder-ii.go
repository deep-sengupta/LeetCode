func findLadders(beginWord string, endWord string, wordList []string) [][]string {
	dict := map[string]bool{}
	for _, w := range wordList {
		dict[w] = true
	}
	if !dict[endWord] {
		return [][]string{}
	}

	parent := map[string][]string{}
	level := map[string]int{beginWord: 0}
	q := []string{beginWord}
	l := len(beginWord)

	for len(q) > 0 {
		cur := q
		q = nil
		found := false
		vis := map[string]bool{}

		for _, w := range cur {
			b := []byte(w)
			for i := 0; i < l; i++ {
				c := b[i]
				for ch := byte('a'); ch <= 'z'; ch++ {
					if ch == c {
						continue
					}
					b[i] = ch
					n := string(b)
					if !dict[n] {
						continue
					}
					if _, ok := level[n]; !ok {
						level[n] = level[w] + 1
						parent[n] = append(parent[n], w)
						if !vis[n] {
							vis[n] = true
							q = append(q, n)
						}
					} else if level[n] == level[w]+1 {
						parent[n] = append(parent[n], w)
					}
					if n == endWord {
						found = true
					}
				}
				b[i] = c
			}
		}
		if found {
			break
		}
	}

	var ans [][]string
	var path []string
	var dfs func(string)
	dfs = func(w string) {
		path = append(path, w)
		if w == beginWord {
			t := make([]string, len(path))
			for i := range path {
				t[i] = path[len(path)-1-i]
			}
			ans = append(ans, t)
		} else {
			for _, p := range parent[w] {
				dfs(p)
			}
		}
		path = path[:len(path)-1]
	}

	if _, ok := parent[endWord]; ok {
		dfs(endWord)
	}
	return ans
}