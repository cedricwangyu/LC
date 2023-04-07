class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m, n, todo = len(grid), len(grid[0]), []
        for i in range(m):
            J = range(n) if i in (0, m-1) else (0, n-1)
            for j in J:
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    todo.append((i, j))
        
        while todo:
            i, j = todo.pop(0)
            for ii, jj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ii < m and 0 <= jj < n and grid[ii][jj] == 1:
                    grid[ii][jj] = 0
                    todo.append((ii, jj))
                
        return sum(sum(row) for row in grid)