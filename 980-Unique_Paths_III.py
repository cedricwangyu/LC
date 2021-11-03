class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        self.res, self.target, self.count, m, n, I, J = 0, 0, 0, len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] in (0, 1): self.target += 1
                if grid[i][j] == 1: I, J = i, j

        def dfs(i, j):
            if grid[i][j] == 2:
                if self.target == self.count: self.res += 1
                return
            grid[i][j] = -2
            self.count += 1
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] in (0, 2): dfs(ni, nj)
            self.count -= 1
            grid[i][j] = 0
        
        dfs(I, J)
        return self.res
