class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        for i in range(n-2,-1,-1):
            grid[i][-1] += grid[i+1][-1]
        for j in range(m-2,-1,-1):
            grid[-1][j] += grid[-1][j+1]
        for i in range(n-2, -1, -1):
            for j in range(m-2, -1, -1):
                grid[i][j] += min(grid[i][j+1], grid[i+1][j])
        
        return grid[0][0]
        