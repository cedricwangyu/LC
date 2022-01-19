class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        diff = abs((hour % 12) * 5 - 11 * minutes / 12)
        return min(diff, 60-diff) * 6
        
