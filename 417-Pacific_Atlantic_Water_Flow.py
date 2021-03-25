class Solution:
    def __init__(self):
        self.d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix: return None
        M, N = len(matrix), len(matrix[0])
        def update(curr, todo, rec):
            while len(todo) > 0:
                curr.update(todo)
                todo.clear()
                for coor in curr: rec[coor[0]][coor[1]] = True
                for coor in curr:
                    for dire in self.d:
                        coornew = (coor[0] + dire[0], coor[1] + dire[1])
                        if 0 <= coornew[0] < M and 0 <= coornew[1] < N and matrix[coornew[0]][coornew[1]] >= matrix[coor[0]][coor[1]]:
                            if not rec[coornew[0]][coornew[1]]: todo.add(coornew)
                            rec[coornew[0]][coornew[1]] = True
                curr.clear()
            todo.clear()
        curr, todo, rec1, rec2 = set(), set(), [[False] * N for _ in range(M)], [[False] * N for _ in range(M)]
        todo.update([(M-1, j) for j in range(N)], [(i, N-1) for i in range(M)])
        update(curr, todo, rec1)
        todo.update([(0, j) for j in range(N)], [(i, 0) for i in range(M)])
        update(curr, todo, rec2)
        res = []
        for i in range(M):
            for j in range(N):
                if rec1[i][j] and rec2[i][j]: res.append((i, j))
        return res