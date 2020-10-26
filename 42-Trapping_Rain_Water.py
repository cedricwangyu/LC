class Solution:
    def trap(self, height: List[int]) -> int:
        left = 0
        right = 0
        wall = 0
        t = 0
        for h in height:
            t = max([t, h])
            wall += h
            left += t
        t = 0
        for h in height[::-1]:
            t = max([t, h])
            right += t
        
        return(left + right - t * len(height) - wall)
        
        