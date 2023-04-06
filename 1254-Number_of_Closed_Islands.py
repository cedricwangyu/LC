class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n, res = len(grid), len(grid[0]), 0
        if m < 3 or n < 3: return res
        for i in range(1, m-1):
            for j in range(1, n-1):
                if grid[i][j] == 0:
                    todo = [(i, j)]
                    add_one = True
                    while todo:
                        ii, jj = todo.pop(0)
                        grid[ii][jj] = 1
                        if ii == 0 or ii == m-1 or jj == 0 or jj == n-1:
                            add_one = False
                        for ni, nj in ((ii+1, jj), (ii-1, jj), (ii, jj+1), (ii, jj-1)):
                            if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 0:
                                todo.append((ni, nj))
                    
                    if add_one:
                        res += 1
        
        return res
        