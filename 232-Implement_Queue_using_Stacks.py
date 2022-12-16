class MyQueue:

    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def to_in_stack(self):
        while self.out_stack:
            self.in_stack.append(self.out_stack.pop())
    
    def to_out_stack(self):
        while self.in_stack:
            self.out_stack.append(self.in_stack.pop())

    def push(self, x: int) -> None:
        if self.out_stack:
            self.to_in_stack()
        self.in_stack.append(x)

    def pop(self) -> int:
        if self.in_stack:
            self.to_out_stack()
        return self.out_stack.pop()

    def peek(self) -> int:
        if self.in_stack:
            self.to_out_stack()
        return self.out_stack[-1]

    def empty(self) -> bool:
        return len(self.out_stack) == 0 and len(self.in_stack) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()