class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 0, min(time) * totalTrips
        while right - left > 1:
            mid = (left + right) // 2
            total = 0
            for t in time:
                total +=  mid // t
            if total >= totalTrips:
                right = mid
            else:
                left = mid
        return right