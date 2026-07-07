class Solution {
    public long sumAndMultiply(int n) {
        long x = 0;
        int sum = 0;
        if (n == 0) return 0;
        char[] digits = String.valueOf(n).toCharArray();
        for (char c : digits) {
            if (c != '0') {
                int d = c - '0';
                x = x * 10 + d;
                sum += d;
            }
        }
        return x * sum;
    }
}