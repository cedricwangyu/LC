class Solution:
    def __init__(self):
        self.dir = ((0, 1), (0, -1), (1, 0), (-1, 0))
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        res, island = set(), []
        def findandrecord(I, J, i, j):
            if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]): return
            if grid[i][j] == 1:
                island.append((i - I, j - J))
                grid[i][j] = 0
                for pos in self.dir: findandrecord(I, J, i + pos[0], j + pos[1])
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    island.clear()
                    findandrecord(i, j, i, j)
                    res.add(tuple(island))
        return len(res)