class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int start = 0, tank = 0, total = 0;
        for (int i = 0; i < gas.length; i++) {
            int diff = gas[i] - cost[i];
            tank += diff;
            total += diff;
            if (tank < 0) {
                start = i + 1;
                tank = 0;
            }
        }
        return total < 0 ? -1 : start;
    }
}