class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        cs, prev, res = [0, 0], 0, float('Inf')
        for c in s:
            if int(c) - prev == 1: res = min(res, cs[1] - cs[0])
            cs[int(c)] += 1
        res = min(res, cs[1] - cs[0])
        return res + cs[0]
