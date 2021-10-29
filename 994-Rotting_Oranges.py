class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        todo, m, n, res, total_fresh = [], len(grid), len(grid[0]), 0, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2: todo.append((i, j, 0))
                elif grid[i][j] == 1: total_fresh += 1
        while len(todo) > 0:
            i, j, t = todo.pop(0)
            res = max(res, t)
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    grid[ni][nj], total_fresh = 2, total_fresh - 1
                    todo.append((ni, nj, t+1))
        return res if total_fresh == 0 else -1
