class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        h, res = [], [0] * len(temperatures)
        for i, t in enumerate(temperatures):
            heapq.heappush(h, (t, i))
            while len(h) > 0 and h[0][0] < t:
                _, ii = heapq.heappop(h)
                res[ii] = i-ii
        return res
