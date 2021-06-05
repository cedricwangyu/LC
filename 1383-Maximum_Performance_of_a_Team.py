import bisect
class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        if k == 1: return max(e * s for e, s in zip(efficiency, speed))
        eng, res, curr_sum = [(e, s) for e, s in zip(efficiency, speed)], 0, 0
        eng.sort(key=lambda x: x[0])
        speed.clear()
        while len(eng) > 0:
            e, s = eng.pop()
            res, curr_sum = max(res, e * (s + curr_sum)), curr_sum + s
            insort(speed, s)
            if len(speed) > k-1: curr_sum -= speed.pop(0)
        return res % (10 ** 9 + 7)
