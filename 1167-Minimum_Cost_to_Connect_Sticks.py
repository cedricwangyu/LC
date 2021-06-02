import bisect
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        res = 0
        sticks.sort()
        while(len(sticks) > 1):
            a = sticks.pop(0)
            b = sticks.pop(0)
            bisect.insort_left(sticks, a+b)
            res += a + b
        return res