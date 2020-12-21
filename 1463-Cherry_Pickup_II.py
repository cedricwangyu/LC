class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols, left, right, r = len(grid), len(grid[0]), 1, len(grid[0]) - 2, 0
        while (r < rows) and (right - left >= 0):
            for c in range(left, right + 1): grid[r][c] = 0 
            r += 1
            left += 1
            right -= 1
        
        P1 = [[0] * cols for _ in range(cols)]
        P2 = [[0] * cols for _ in range(cols)]
        P1[0][cols - 1] = grid[0][0] + grid[0][cols - 1]

        for r in range(1, rows):
            if r % 2 == 1: p, q = P1, P2
            else: q, p = P1, P2
            for i in range(cols):
                for j in range(cols):
                    q[i][j] = 0
                    for ii in range(-1,2):
                        for jj in range(-1,2):
                            q[i][j] = max(q[i][j], p[min(max(i + ii, 0), cols - 1)][min(max(j + jj, 0), cols - 1)])
                    if i == j: q[i][j] += grid[r][i]
                    else: q[i][j] += (grid[r][i] + grid[r][j])
        return max([max(row) for row in q])
                    
                    
            