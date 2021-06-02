class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def area(i, j):
            if i < len(grid) and i >= 0 and j < len(grid[0]) and j >= 0 and grid[i][j] == 1:
                grid[i][j] = 0
                return 1 + area(i-1, j) + area(i+1, j) + area(i, j-1) + area(i, j+1)
            else: return 0
        i, j, res = 0, 1, grid[0][0]
        while i < len(grid):
            while j < len(grid[0]):
                res = max(res, area(i, j))
                j += 1
            i, j = i+1, 0
        return res