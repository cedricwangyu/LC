class MyCircularQueue:

    def __init__(self, k: int):
        self.k = k
        self.p = [0] * self.k
        self.start = 0
        self.end = 0
        self.full = False
    def enQueue(self, value: int) -> bool:
        if not self.full: 
            self.p[self.end] = value
            self.end = (self.end + 1) % self.k
            if self.start == self.end: self.full = True
            return True
        else: return False

    def deQueue(self) -> bool:
        if self.isEmpty(): return False
        self.start = (self.start + 1) % self.k
        if self.full: self.full = False
        return True

    def Front(self) -> int:
        if self.isEmpty(): return -1
        return self.p[self.start]

    def Rear(self) -> int:
        if self.isEmpty(): return -1
        return self.p[self.end - 1]

    def isEmpty(self) -> bool:
        return True if self.start == self.end and not self.full else False

    def isFull(self) -> bool:
        return self.full


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
