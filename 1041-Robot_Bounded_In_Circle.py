class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr, dirs, d_idx = [0, 0], ((0, 1), (1, 0), (0, -1), (-1, 0)), 0
        for c in instructions:
            if c == "G": curr[0], curr[1] = curr[0] + dirs[d_idx][0], curr[1] + dirs[d_idx][1]
            elif c == "L": d_idx = (d_idx - 1) % 4
            else: d_idx = (d_idx + 1) % 4
        
        return True if (curr[0] == 0 and curr[1] == 0) or d_idx != 0 else False