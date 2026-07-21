class Solution {
    public int numDistinct(String s, String t) {
        int n = t.length();
        long[] dp = new long[n + 1];
        dp[0] = 1;
        for (char c : s.toCharArray())
            for (int i = n - 1; i >= 0; i--)
                if (c == t.charAt(i))
                    dp[i + 1] += dp[i];
        return (int) dp[n];
    }
}