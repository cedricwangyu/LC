class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        curr, res = 0, []
        for i in range(len(heights)-1, -1, -1):
            if heights[i] > curr:
                res.insert(0, i)
                curr = heights[i]
        return res
