class MinStack:
    def __init__(self):
        self.s=[]

    def push(self, x: int) -> None:
        self.s+=[(x,min(x,self.s[-1][1]))] if self.s else [(x,x)]

    def pop(self) -> None:
        self.s.pop()

    def top(self) -> int:
        return self.s[-1][0]

    def getMin(self) -> int:
        return self.s[-1][1]