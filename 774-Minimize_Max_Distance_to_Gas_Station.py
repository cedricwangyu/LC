class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:
        def possible(D):
            return sum(int((stations[i+1]-stations[i])/D) for i in range(len(stations)-1)) <= k

        lo, hi = 0, 10**8
        while hi - lo > 1e-6:
            mi = (lo + hi) / 2.0
            if possible(mi): hi = mi
            else: lo = mi
        return lo