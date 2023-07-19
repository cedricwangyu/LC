class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: x[1])
        k, res = float("-Inf"), 0
        for a, b in intervals:
            if a >= k:
                k = b
            else:
                res += 1
        return res