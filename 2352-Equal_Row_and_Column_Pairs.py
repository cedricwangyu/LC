from collections import Counter
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        p, res = Counter(tuple(row) for row in grid), 0
        for j in range(len(grid[0])):
            col = tuple(grid[i][j] for i in range(len(grid)))
            if col in p:
                res += p[col]
        return res