class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m, n = len(matrix), len(matrix[0])
        res = []
        for j in range(n):
            row = []
            for i in range(m):
                row.append(matrix[i][j])
            res.append(row)
        return res