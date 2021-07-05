class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat) * len(mat[0]): return mat
        ii, jj, res = 0, 0, [[0] * c for _ in range(r)]
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                res[ii][jj] = mat[i][j]
                ii, jj = ii + int(jj + 1 >= c), (jj + 1) % c
        return res