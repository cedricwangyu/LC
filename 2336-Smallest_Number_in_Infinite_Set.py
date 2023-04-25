class SmallestInfiniteSet:

    def __init__(self):
        self.p = set()
        self.curr = 1
        
    def popSmallest(self) -> int:
        self.p.add(self.curr)
        res = self.curr
        self.curr += 1
        while self.curr in self.p:
            self.curr += 1
        return res

    def addBack(self, num: int) -> None:
        if num in self.p:
            self.p.remove(num)
            if num < self.curr:
                self.curr = num
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)