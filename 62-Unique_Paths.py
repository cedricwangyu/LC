class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @functools.lru_cache(maxsize=m*n)
        def dp(i, j):
            if i == m-1 and j == n-1: return 1
            elif i == m-1: return dp(i, j+1)
            elif j == n-1: return dp(i+1, j)
            else: return dp(i+1, j) + dp(i, j+1)
        return dp(0,0)
