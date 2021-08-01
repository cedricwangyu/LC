class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        self.boundary, self.dir, maximum = {}, ((1, 0), (-1, 0), (0, 1), (0, -1)), 0
        def find_island(I, J):
            b, todo, grid[I][J], area = set(), [(I, J)], -1, 1
            while len(todo) > 0:
                i, j = todo.pop(0)
                for di, dj in self.dir:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]):
                        if grid[ni][nj] == 1: 
                            todo.append((ni, nj))
                            grid[ni][nj], area = -1, area + 1
                        elif grid[ni][nj] == 0: b.add((ni, nj)) 
            return area, b
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    a, b = find_island(i, j)
                    for loc in b: 
                        self.boundary[loc] = self.boundary[loc] + a if loc in self.boundary else a
                        maximum = max(maximum, self.boundary[loc])
        return maximum + 1 if len(self.boundary) > 0 or (grid[0][0] == 0) else len(grid) * len(grid[0])    
