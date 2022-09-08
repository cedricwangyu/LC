class HitCounter:

    def __init__(self):
        self.hits = []
        
    def update(self, timestamp: int) -> None:
        while self.hits and self.hits[0] <= timestamp - 300:
            self.hits.pop(0)
        
    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)
        self.update(timestamp)

    def getHits(self, timestamp: int) -> int:
        self.update(timestamp)
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)