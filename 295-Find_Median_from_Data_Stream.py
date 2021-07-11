class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.p = []
        self.idx = [0, 0]

    def addNum(self, num: int) -> None:
        bisect.insort_left(self.p, num)
        if len(self.p) % 2 == 1: self.idx.pop(0)
        else: self.idx.append(len(self.p) // 2)

    def findMedian(self) -> float:
        return sum(self.p[i] for i in self.idx) / len(self.idx)
            


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
