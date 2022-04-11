class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        k %= m*n
        i_loc, j_loc = ((m*n - k) // n) % m, (m*n - k) % n
        res = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                res[i][j] = grid[i_loc][j_loc]
                j_loc += 1
                if j_loc >= n:
                    i_loc, j_loc = i_loc+1, 0
                    if i_loc >= m:
                        i_loc = 0
        return res