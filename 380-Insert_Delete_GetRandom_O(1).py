import random
class RandomizedSet:

    def __init__(self):
        self.p = set()
        
    def insert(self, val: int) -> bool:
        if val not in self.p:
            self.p.add(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.p:
            self.p.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return list(self.p)[randint(0, len(self.p)-1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
