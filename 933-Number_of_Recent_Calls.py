class RecentCounter:

    def __init__(self):
        self.record = []

    def ping(self, t: int) -> int:
        self.record.append(t)
        while(self.record[0] + 3000 < t): self.record.pop(0)
        return len(self.record)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)