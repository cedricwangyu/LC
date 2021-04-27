class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        p, res = {}, 0
        for row in wall:
            c = 0
            for w in row[:len(row)-1]:
                c += w
                if c in p: p[c] += 1
                else: p[c] = 1
                res = max(res, p[c])
        return len(wall) - res