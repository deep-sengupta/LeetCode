class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = (1 << 31) - 1
        INT_MIN = -(1 << 31)

        if dividend == INT_MIN and divisor == -1:
            return INT_MAX

        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1

        a = abs(dividend)
        b = abs(divisor)

        ans = 0
        while a >= b:
            temp = b
            multiple = 1
            while a >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            a -= temp
            ans += multiple

        return ans if sign > 0 else -ans