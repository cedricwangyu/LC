class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        board = []
        for i in range(n):
            board.append([0] * n)
        dirs = [(0,1), (1,0), (0,-1),(-1,0)]
        d = 0
        curr = [0,0]
        for i in range(1, n ** 2 + 1):
            board[curr[0]][curr[1]] = i
            nstep = [curr[0] + dirs[d][0], curr[1] + dirs[d][1]]
            if nstep[0] >= n or nstep[0] < 0 or nstep[1] >= n or nstep[1] < 0 or board[nstep[0]][nstep[1]] > 0:
                d = (d + 1) % 4
                curr = [curr[0] + dirs[d][0], curr[1] + dirs[d][1]]
            else: curr = nstep.copy()
        return board