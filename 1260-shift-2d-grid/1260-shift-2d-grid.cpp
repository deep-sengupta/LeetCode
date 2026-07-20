class Solution {
public:
    vector<vector<int>> shiftGrid(vector<vector<int>>& g, int k) {
        int m = g.size(), n = g[0].size(), t = m * n;
        k %= t;
        vector<vector<int>> a(m, vector<int>(n));
        for (int i = 0; i < t; i++) {
            int j = (i + k) % t;
            a[j / n][j % n] = g[i / n][i % n];
        }
        return a;
    }
};