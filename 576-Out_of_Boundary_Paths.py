class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        @functools.lru_cache(maxsize=(m+2)*(n+2)*(maxMove+2))
        def dp(x, y, r):
            if x >= m or x < 0 or y >= n or y < 0: return 1 
            if r <= 0: return 0
            res = 0
            for d in ((1, 0), (-1, 0), (0, 1), (0, -1)): res += dp(x+d[0], y+d[1], r-1) 
            return res
        return dp(startRow, startColumn, maxMove) % (10 ** 9 + 7)
