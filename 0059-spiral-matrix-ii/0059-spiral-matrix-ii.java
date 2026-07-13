class Solution {
    public int[][] generateMatrix(int n) {
        int[][] a = new int[n][n];
        int l = 0, r = n - 1, t = 0, b = n - 1, v = 1;
        while (l <= r && t <= b) {
            for (int i = l; i <= r; i++) a[t][i] = v++;
            t++;
            for (int i = t; i <= b; i++) a[i][r] = v++;
            r--;
            for (int i = r; t <= b && i >= l; i--) a[b][i] = v++;
            b--;
            for (int i = b; l <= r && i >= t; i--) a[i][l] = v++;
            l++;
        }
        return a;
    }
}