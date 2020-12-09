class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        time = [t % 60 for t in time]
        p = {}
        res = 0
        for t in time:
            if t == 0:
                if 0 in p:
                    p[0] += 1
                    res += p[0] - 1
                else: p[0] = 1
                continue
            if t in p: res += p[t]
            if 60 - t in p: p[60 - t] += 1
            else: p[60 - t] = 1
        return res
        