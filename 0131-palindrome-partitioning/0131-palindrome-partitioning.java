class Solution {
    public List<List<String>> partition(String s) {
        List<List<String>> ans = new ArrayList<>();
        dfs(s, 0, new ArrayList<>(), ans);
        return ans;
    }

    void dfs(String s, int i, List<String> cur, List<List<String>> ans) {
        if (i == s.length()) {
            ans.add(new ArrayList<>(cur));
            return;
        }
        for (int j = i; j < s.length(); j++) {
            if (pal(s, i, j)) {
                cur.add(s.substring(i, j + 1));
                dfs(s, j + 1, cur, ans);
                cur.remove(cur.size() - 1);
            }
        }
    }

    boolean pal(String s, int l, int r) {
        while (l < r)
            if (s.charAt(l++) != s.charAt(r--)) return false;
        return true;
    }
}