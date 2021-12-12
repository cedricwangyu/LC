class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == "0": matrix[i][j] = 0
                else: 
                    if i == 0: matrix[i][j] = int(matrix[i][j] == "1")
                    elif j == 0: matrix[i][j] = int(matrix[i][j] == "1")
                    else: matrix[i][j] = 1 + min(matrix[i-1][j-1], matrix[i][j-1], matrix[i-1][j])
                    res = max(res, matrix[i][j])
        return res ** 2