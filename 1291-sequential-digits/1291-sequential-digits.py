class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = "123456789"
        return sorted(int(s[i:j]) for i in range(9) for j in range(i + 2, 10) if low <= int(s[i:j]) <= high)