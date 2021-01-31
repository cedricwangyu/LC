class Solution:
    def countCornerRectangles(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        if rows < 2 or cols < 2: return 0
        p, res = {}, 0
        for row in grid:
            pos = [i for i in range(cols) if row[i] == 1]
            if len(pos) < 2: continue
            for l, left in enumerate(pos[:-1]):
                for right in pos[l + 1:]:
                    if (left, right) in p:
                        res += p[(left, right)]
                        p[(left, right)] += 1
                    else: p[(left, right)] = 1
        return res
        