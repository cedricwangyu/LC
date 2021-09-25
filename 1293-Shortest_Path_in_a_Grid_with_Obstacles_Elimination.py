class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n, todo, seen = len(grid), len(grid[0]), [(0, (0,0,k))], set((0,0,k))
        while len(todo) > 0:
            steps, (i, j, kk) = todo.pop(0)
            if i == m-1 and j == n-1: return steps
            for ni, nj in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= ni < m and 0 <= nj < n and kk-grid[ni][nj] >= 0 and (ni, nj, kk-grid[ni][nj]) not in seen:
                    todo.append((steps + 1, (ni, nj, kk-grid[ni][nj])))
                    seen.add((ni, nj, kk-grid[ni][nj]))
        return -1