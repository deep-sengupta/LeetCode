class Solution {
    public int maxProfit(int[] p) {
        int min = Integer.MAX_VALUE, ans = 0;
        for (int x : p) {
            min = Math.min(min, x);
            ans = Math.max(ans, x - min);
        }
        return ans;
    }
}