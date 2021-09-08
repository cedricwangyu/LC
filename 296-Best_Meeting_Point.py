class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        row, col = [], []
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    bisect.insort(row, i)
                    bisect.insort(col, j)
        res = 0
        while len(row) > 1: res += row.pop() - row.pop(0)
        while len(col) > 1: res += col.pop() - col.pop(0)
        return res
