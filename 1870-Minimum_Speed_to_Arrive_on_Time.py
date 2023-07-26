from math import ceil
class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        def validate(speed):
            res = 0
            for dis in dist[:-1]:
                res += ceil(dis / speed)
            return (res + dist[-1] / speed) <= hour
        if hour <= len(dist) - 1:
            return -1
        
        mini, maxi = 1, max(max(dist), int(dist[-1]/(hour - len(dist) + 1) + 1))
        if validate(mini):
            return mini
        while maxi > mini + 1:
            mid = (mini + maxi) // 2
            if validate(mid):
                maxi = mid
            else:
                mini = mid
        return maxi
        
        
        