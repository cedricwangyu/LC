class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        dirs, m, n, res = ((1, 0), (-1, 0), (0, 1), (0, -1)), len(grid), len(grid[0]), 0
        def count_p(i, j):
            res = 0
            for di, dj in dirs:
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj]: res += 1
            return res
        for i in range(m):
            for j in range(n):
                if grid[i][j]: res += 4 - count_p(i, j)
        return res
