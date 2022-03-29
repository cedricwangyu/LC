class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        val, self.todo, self.seen, self.dirs = set(), [], set(), ((1,0), (-1,0), (0,1), (0,-1))
        for row in grid:
            for num in row:
                val.add(num)
        val = list(val)
        val.sort()
        def is_done(least_val):
            if least_val > grid[-1][-1]: return False
            self.todo.clear()
            self.seen.clear()
            self.todo.append((0,0))
            self.seen.add((0,0))
            while len(self.todo) > 0:
                i, j = self.todo.pop()
                if i == len(grid)-1 and j == len(grid[0])-1:
                    return True
                if grid[i][j] < least_val: continue
                for ii, jj in self.dirs:
                    if (i+ii, j+jj) not in self.seen and 0 <= i+ii < len(grid) and 0 <= j+jj < len(grid[0]) :
                        self.todo.append((i+ii, j+jj))
                        self.seen.add((i+ii, j+jj))
            return False
        l, r = 0, len(val)-1
        if is_done(val[r]): return val[r]
        while r-l > 1:
            m = (l+r) // 2
            if is_done(val[m]): l = m
            else: r = m
        
        return val[l]
                        
                    