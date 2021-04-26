import bisect
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        hd, s = [], 0
        for i in range(1, len(heights)):
            if heights[i] > heights[i-1]: 
                I = bisect.bisect_left(hd, heights[i] - heights[i-1])
                hd.insert(I, heights[i] - heights[i-1])
                if len(hd) > ladders and I < len(hd) - ladders: s += hd[I]
                elif len(hd) > ladders and I >= len(hd) - ladders: s += hd[len(hd) - ladders - 1]
                if s > bricks: return i - 1
        return i
