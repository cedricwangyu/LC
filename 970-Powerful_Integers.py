class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        res = set()
        xp, yp = 1, 1
        while xp + yp <= bound:
            res.add(xp+yp)
            if y > 1: yp *= y
            else: 
                if x > 1: xp *= x
                else: return list(res)
            if xp + yp > bound: 
                if x == 1: return list(res)
                else: xp, yp = xp * x, 1
        return list(res)
            