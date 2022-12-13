from functools import lru_cache 
class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        if n == 1:
            return matrix[0][0]
        @lru_cache(maxsize=n**2)
        def dp(i, j):
            if i == n-1:
                return matrix[i][j]
            elif j==0:
                return min(dp(i+1, j), dp(i+1, j+1)) + matrix[i][j]
            elif j==n-1:
                return min(dp(i+1, j), dp(i+1, j-1)) + matrix[i][j]
            else:
                return min(dp(i+1, j), dp(i+1, j-1), dp(i+1, j+1)) + matrix[i][j]
        
        return min(dp(0, j) for j in range(n))