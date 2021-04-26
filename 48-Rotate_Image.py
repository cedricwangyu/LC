class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        for n in range(N // 2 + (N % 2)):
            for i in range(n, N - n - 1): matrix[n][i], matrix[i][N-n-1], matrix[N-n-1][N-i-1], matrix[N-i-1][n] = matrix[N-i-1][n], matrix[n][i], matrix[i][N-n-1], matrix[N-n-1][N-i-1]
