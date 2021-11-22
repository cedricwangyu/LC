from collections import OrderedDict
class FirstUnique:
    def __init__(self, nums: List[int]):
        self.q = OrderedDict()
        self.u = {}
        for n in nums: self.add(n)

    def showFirstUnique(self) -> int:
        if self.q: return next(iter(self.q))
        return -1

    def add(self, value: int) -> None:
        if value not in self.u:
            self.u[value] = True
            self.q[value] = None
        elif self.u[value]:
            self.u[value] = False
            self.q.pop(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
