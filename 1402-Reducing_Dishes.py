class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()
        curr, res = 0, 0
        for i, s in enumerate(satisfaction):
            curr += s
            res += s * (i+1)
        
        for s in satisfaction:
            if curr < 0:
                res -= curr
                curr -= s
            else:
                return res
        return 0
        