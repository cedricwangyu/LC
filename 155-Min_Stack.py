class MinStack:

    def __init__(self):
        self.p = []
        
    def push(self, val: int) -> None:
        if len(self.p) == 0: self.p.append((val, val))
        else: self.p.append((val, min(val, self.p[-1][1])))
        
    def pop(self) -> None:
        self.p.pop()
        
    def top(self) -> int:
        return self.p[-1][0]

    def getMin(self) -> int:
        return self.p[-1][1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
