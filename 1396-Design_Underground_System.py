class UndergroundSystem:

    def __init__(self):
        self.p = {}
        self.going = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.going[id] = (t, stationName)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        rec = self.going[id]
        del self.going[id]
        pid = (rec[1], stationName)
        if pid not in self.p: self.p[pid] = [0, 0]
        self.p[pid][0] += 1
        self.p[pid][1] += t - rec[0]
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        rec = self.p[(startStation, endStation)]
        return rec[1] / rec[0]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)