class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        self.p = sorted([item for item in zip(startTime, endTime, profit)], key=lambda x: x[0])
        self.s = [item[0] for item in self.p]
        @functools.lru_cache()
        def dp(i):
            if i >= len(self.p): return 0
            return max(dp(i+1), dp(bisect.bisect_left(self.s, self.p[i][1])) + self.p[i][2])
        return dp(0)