class Solution:
    def __init__(self):
        self.dirs = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]
        
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[-1][-1] == 1: return -1
        R, C = len(grid), len(grid[0])
        state, curr, new = [[-2] * C for _ in range(R)], [(R - 1, C - 1)], []
        state[R - 1][C - 1], value = 0, 1
        while(len(curr) > 0):
            new.clear()
            for pos in curr:
                for d in self.dirs:
                    new_pos = (pos[0] + d[0], pos[1] + d[1])
                    if new_pos[0] >= 0 and new_pos[0] < R and new_pos[1] >= 0 and new_pos[1] < C and new_pos != pos and state[new_pos[0]][new_pos[1]] < 0 and grid[new_pos[0]][new_pos[1]] < 1:
                        state[new_pos[0]][new_pos[1]] = value
                        new.append(new_pos)
            curr.clear()
            curr.extend(new)
            value += 1
        return state[0][0] + 1
        
        