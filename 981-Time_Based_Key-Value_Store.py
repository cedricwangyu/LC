from bisect import bisect_right
class TimeMap:

    def __init__(self):
        self.p = defaultdict(list)
        self.mask = "z"*100

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.p[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.p:
            i = bisect_right(self.p[key], (timestamp, self.mask))
            if i > 0:
                return self.p[key][i-1][1]
        return ""

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)