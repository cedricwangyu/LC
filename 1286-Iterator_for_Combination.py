class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.s = characters
        self.idx = [i for i in range(combinationLength)]
        
    def inc(self):
        self.idx[-1] += 1
        i = len(self.idx) - 1
        while i > 0 and self.idx[i] > len(self.s) - len(self.idx) + i:
            self.idx[i-1], i = self.idx[i-1]+1, i-1
        if i == 0 and self.idx[0] > len(self.s) - len(self.idx): self.idx.clear()
        else:
            for j in range(i+1, len(self.idx)): self.idx[j]=self.idx[j-1]+1
            
    def next(self) -> str:
        res = "".join(self.s[i] for i in self.idx)
        self.inc()
        return res

    def hasNext(self) -> bool:
        return True if self.idx else False


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()
