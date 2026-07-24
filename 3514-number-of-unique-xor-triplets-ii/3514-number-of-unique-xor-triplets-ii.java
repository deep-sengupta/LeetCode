class Solution {
    public int uniqueXorTriplets(int[] nums) {
        boolean[] p = new boolean[2048], d = new boolean[2048], t = new boolean[2048];
        for (int x : nums) p[x] = true;
        for (int i = 0; i < 2048; i++)
            if (p[i])
                for (int j = 0; j < 2048; j++)
                    if (p[j]) d[i ^ j] = true;
        int ans = 0;
        for (int i = 0; i < 2048; i++)
            if (d[i])
                for (int j = 0; j < 2048; j++)
                    if (p[j]) t[i ^ j] = true;
        for (boolean x : t) if (x) ans++;
        return ans;
    }
}