from bisect import bisect_right
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        i = bisect_right([-grid[ii][-1] for ii in range(n)], 0)
        if i == n:
            return 0
        j, res = m, 0
        for ii in range(i, n):
            j = bisect_right([-a for a in grid[ii]], 0, lo=0, hi=j)
            res += m - j
            if j == 0:
                return res + (n - ii - 1) * m
        return res