class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if len(matrix) == 0 or len(matrix[0]) == 0: return []
        rows, cols, i, j, d, N, n, res = len(matrix), len(matrix[0]), 0, 0, 1, len(matrix) * len(matrix[0]), 0, []
        while n < N:
            res.append(matrix[i][j])
            if j == cols - 1 and d == 1: i, d = i + 1, -1
            elif i == rows - 1 and d == -1: j, d = j + 1, 1
            elif j == 0 and d == -1: i, d = i + 1, 1
            elif i == 0 and d == 1: j, d = j + 1, -1
            else: i, j = i - d, j + d
            n += 1
        return res
            
        
        