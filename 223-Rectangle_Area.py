class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        total = (ax2 - ax1) * (ay2 - ay1) + (bx2 - bx1) * (by2 - by1)
        if ax2 < bx1 or ax1 > bx2 or ay2 < by1 or ay1 > by2:
            intersection = 0
        else:
            _, x1, x2, _ = sorted([ax1, ax2, bx1, bx2])
            _, y1, y2, _ = sorted([ay1, ay2, by1, by2])
            intersection = (x2 - x1) * (y2 - y1)
        return total - intersection