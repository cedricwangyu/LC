class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        # M, N, self.dir = len(matrix), len(matrix[0]), ((1, 0), (-1, 0), (0, 1), (0, -1))
        # curr, new = set(), set()
        # for i, row in enumerate(matrix):
        #     for j, n in enumerate(row):
        #         if all(n >= matrix[i + d[0]][j + d[1]] for d in self.dir if i + d[0] >= 0 and i + d[0] < M and j + d[1] >= 0 and j + d[1] < N): curr.add((i, j))
        # lev = 0
        # while len(curr) > 0:
        #     for pos in curr:
        #         for d in self.dir:
        #             new_pos = pos[0] + d[0], pos[1] + d[1]
        #             if new_pos[0] >= 0 and new_pos[0] < M and new_pos[1] >= 0 and new_pos[1] < N and matrix[new_pos[0]][new_pos[1]] < matrix[pos[0]][pos[1]]: new.add(new_pos)
        #     curr.clear()
        #     curr.update(new)
        #     new.clear()
        #     lev += 1
        # return lev

        M, N, directions = len(matrix), len(matrix[0]), ((1, 0), (-1, 0), (0, 1), (0, -1))
        def is_good_index(i, j): return i >= 0 and i < M and j >= 0 and j < N
        
        @functools.lru_cache(maxsize=40000)
        def helper(i, j):
            if all(matrix[i][j] >= matrix[i + d[0]][j + d[1]] for d in directions if is_good_index(i + d[0], j + d[1])): return 1
            return 1 + max(helper(i + d[0], j + d[1]) for d in directions if is_good_index(i + d[0], j + d[1]) and matrix[i + d[0]][j + d[1]] > matrix[i][j])
        Max = 0
        for i in range(M):
            for j in range(N): Max = max(Max, helper(i, j))
        return Max