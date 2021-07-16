class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for s, e, a in updates:
            res[s] += a
            if e < length - 1: res[e+1] -= a
        for i in range(1, length): res[i] += res[i-1]
        return res
