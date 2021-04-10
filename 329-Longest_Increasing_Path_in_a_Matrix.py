class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        M, N, self.dir = len(matrix), len(matrix[0]), ((1, 0), (-1, 0), (0, 1), (0, -1))
        curr, new = set(), set()
        for i, row in enumerate(matrix):
            for j, n in enumerate(row):
                if all(n >= matrix[i + d[0]][j + d[1]] for d in self.dir if i + d[0] >= 0 and i + d[0] < M and j + d[1] >= 0 and j + d[1] < N): curr.add((i, j))
        lev = 0
        while len(curr) > 0:
            for pos in curr:
                for d in self.dir:
                    new_pos = pos[0] + d[0], pos[1] + d[1]
                    if new_pos[0] >= 0 and new_pos[0] < M and new_pos[1] >= 0 and new_pos[1] < N and matrix[new_pos[0]][new_pos[1]] < matrix[pos[0]][pos[1]]: new.add(new_pos)
            curr.clear()
            curr.update(new)
            new.clear()
            lev += 1
        return lev