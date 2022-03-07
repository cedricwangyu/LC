import heapq as hq
class Solution:
    def Taxi_Schedululing(self, n, cabTravelTime):
        cabs = [(t, t) for t in cabTravelTime]
        res = 0
        hq.heapify(cabs)
        while n > 0:
            time, cab = hq.heappop(cabs)
            res = max(res, time)
            hq.heappush((time+cab, cab))
            n -= 1

        return res
            