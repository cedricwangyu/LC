def helper(grid, i, j):
    if grid[i][j] == "0":
        return
    else:
        grid[i][j] = "0"
        helper(grid, max([i - 1, 0]), j)
        helper(grid, min([i + 1, len(grid) - 1]), j)
        helper(grid, i, max([j - 1, 0]))
        helper(grid, i, min([j + 1, len(grid[0]) - 1]))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    helper(grid, i, j)
                    res += 1
        return res
        
        