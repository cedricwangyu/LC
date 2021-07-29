class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m, n, curr, new, dist = len(mat), len(mat[0]), set(), set(), 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: curr.add((i, j))
                else: mat[i][j] = -1
        while len(curr) > 0:
            new.clear()
            for i, j in curr:
                for ii, jj in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                    iii, jjj = i + ii, j + jj
                    if 0 <= iii < m and 0 <= jjj < n and mat[iii][jjj] < 0: 
                        new.add((iii, jjj))
                        mat[iii][jjj] = dist
            curr, new, dist = new, curr, dist + 1
        return mat
