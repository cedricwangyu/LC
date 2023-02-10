class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n, todo, res = len(grid), [], 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    todo.append((i, j))
        
        while todo:
            i, j = todo.pop(0)
            for ni, nj in ((i+1, j), (i-1, j), (i, j-1), (i, j+1)):
                if 0 <= ni < n and 0 <= nj < n and grid[ni][nj] == 0:
                    grid[ni][nj] = grid[i][j] + 1
                    res = max(res, grid[ni][nj])
                    todo.append((ni, nj))
        return res-1