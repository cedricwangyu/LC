class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        res = sum(mat[i][i] + mat[i][n-i-1] for i in range(n))
        return res if n % 2 == 0 else res - mat[n // 2][n // 2]