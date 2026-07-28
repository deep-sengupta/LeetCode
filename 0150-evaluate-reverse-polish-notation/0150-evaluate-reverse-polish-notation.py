class Solution:
    def evalRPN(self, t: List[str]) -> int:
        s = []
        for x in t:
            if x not in "+-*/":
                s.append(int(x))
            else:
                b, a = s.pop(), s.pop()
                s += [eval(f"int({a}{x}{b})") if x == "/" else eval(f"{a}{x}{b}")]
        return s[-1]