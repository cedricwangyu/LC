class Solution:
    def minKnightMoves(self, x: int, y: int) -> int:
        curr, res = [0, 0], 0
        while abs(abs(x) - curr[0]) > 2 or abs(abs(y) - curr[1]) > 2:
            if abs(abs(x) - curr[0]) >= abs(abs(y) - curr[1]): 
                curr[0], curr[1] = curr[0] + 2 * (2 * (abs(x) >= curr[0]) - 1), curr[1] + (2 * (abs(y) >= curr[1]) -1)
            else: curr[0], curr[1] = curr[0] + (2 * (abs(x) >= curr[0]) - 1), curr[1] + 2 * (2 * (abs(y) >= curr[1]) -1)
            res += 1
        curr[0], curr[1] = abs(abs(x) - curr[0]), abs(abs(y) - curr[1])
        if curr[0] + curr[1] == 0: return res
        elif curr[0] + curr[1] == 1:
            if res >= 1: return res + 1
            else: return 3
        elif curr[0] + curr[1] == 2: return res + 2
        elif curr[0] + curr[1] == 3: return res + 1
        elif res == 0: return 4
        else: return res + 2