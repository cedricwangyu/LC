class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        for i, time in enumerate(timePoints):
            hour, minute = time.split(":")
            timePoints[i] = int(hour) * 60 + int(minute)
        timePoints.sort()
        res = 1440
        for i in range(len(timePoints)-1): res = min(res, timePoints[i+1] - timePoints[i])
        res = min(res, timePoints[0] - timePoints[-1] + 1440)
        return res