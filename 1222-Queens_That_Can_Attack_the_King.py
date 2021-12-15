class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        p, res = set(tuple(q) for q in queens), []
        for d in ((-1,-1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)):
            pos = [king[0] + d[0], king[1] + d[1]]
            while 0 <= pos[0] < 8 and 0 <= pos[1] < 8:
                if tuple(pos) in p: 
                    res.append(pos)
                    break
                pos[0], pos[1] = pos[0] + d[0], pos[1] + d[1]
        return res
