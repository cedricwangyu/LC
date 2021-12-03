class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m, n = len(matrix), len(matrix[0])
        def same(i, j):
            d = 1 
            while i+d < m and j+d < n:
                if matrix[i+d][j+d] != matrix[i][j]: return False
                d += 1
            return True
        return all(same(i, 0) for i in range(m)) and all(same(0, j) for j in range(1, n))
            
